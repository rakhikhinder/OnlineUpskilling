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
        exclude = ['user']
              

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
 
       
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['plan']

    
