# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Teacher, Student ,Comment ,Subscription



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    is_teacher = forms.BooleanField(required=False, label='Register as Teacher')
    is_student = forms.BooleanField(required=False, label='Register as Student')
    
    class Meta:
        model = User
        fields = [ 'username','email', 'password1', 'password2', 'is_teacher', 'is_student']

class TeacherProfileForm(forms.ModelForm):
    
    class Meta:
        
        model = Teacher
        fields = '__all__'
        widgets = {
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        exclude = ['user']
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['prof_img'].widget.attrs.update({'class': 'form-control'})
              

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['prof_img', 'college', 'address', 'state', 'Country', 'city', 'pin_code', 'phone']
        widgets = {
            'college': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'Country': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prof_img'].widget.attrs.update({'class': 'form-control'})
        # Add placeholders if needed
        self.fields['phone'].widget.attrs.update({'placeholder': 'Enter 10-digit phone number'})
        self.fields['pin_code'].widget.attrs.update({'placeholder': '6-digit postal code'})
 
       
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['plan']

    
