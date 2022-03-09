from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserCreationForm, VerifyCodeForm
from utils import send_otp_code
from .models import User, OtpCode
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin



class RegisterView(View):
    form_class = UserCreationForm
    
    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # Sending otp code to verify user 
            send_otp_code(cd['phone_number'])
            # Save user info in sessions
            request.session['user_registration_info'] = {
                'phone_number': cd['phone_number'],
                'email': cd['email'],
                'full_name': cd['full_name'],
                'password': cd['password2'],
            }
            return redirect('accounts:verify_code')
        return render(request, 'accounts/register.html', {'form': form})


class VerifyCodeView(View):
    form_class = VerifyCodeForm
    
    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify_code.html', {'form': form})

    def post(self, request):
        user_sessions = request.session['user_registration_info']
        sent_code = OtpCode.objects.get(
            phone_number=user_sessions['phone_number'])
        form = self.form_class(request.POST)
        # Creating expiration code using datetime
        code_created_time = int(sent_code.created.strftime("%Y%m%d%H%M%S"))
        now = int(datetime.now().strftime("%Y%m%d%H%M%S"))
        time_passing  = now - code_created_time
        expire_time = 30
        if form.is_valid():
            cd = form.cleaned_data
            if time_passing > expire_time:
                messages.error(request, 'code expired', 'danger')
                sent_code.delete()

            elif time_passing < expire_time and cd['code'] == sent_code.code:
                User.objects.create_user(
                    phone_number=user_sessions['phone_number'], email=user_sessions['email'], full_name=user_sessions['full_name'], password=user_sessions['password'])

                sent_code.delete()

                messages.success(
                    request, 'You registered successfully', 'success')
                return redirect('products:home')

            elif cd['code'] != sent_code.code:
                messages.error(request, 'This code is wrong', 'danger')
                return render(request, 'accounts/verify_code.html', {'form': form})
            
            else:
                return render(request, 'accounts/verify_code.html', {'form': form})
            
        return render(request, 'accounts/verify_code.html', {'form': form})


class SendVerifyCodeAgain(View):

    def get(self, request):
        user_sessions = request.session['user_registration_info']
        previous_code = OtpCode.objects.get(phone_number=user_sessions['phone_number'])
        if previous_code:
            previous_code.delete()
        send_otp_code(phone_number = user_sessions['phone_number'])
        return redirect('accounts:verify_code')


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    # overriding get_form class to customize froms in UserLOginView: here using bootstrap
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone number'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'})
        return form

class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = 'products:home'