from django import forms
from .models import Profile, Order, Car
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Profile
        fields = ['address', 'phone']
class OrderForm(forms.ModelForm):
    car = forms.ModelChoiceField(queryset=Car.objects.all(), empty_label="Select Car")
    class Meta:
        model = Order
        fields = ['car', 'quantity']




