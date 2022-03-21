from django import forms

class CartAddForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=9,widget=(forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'quantity'})), label='')


class CouponApplyForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Coupon'}))