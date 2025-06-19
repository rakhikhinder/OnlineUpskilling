# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Teacher, Student,Comment, Product



class UserRegisterForm(UserCreationForm):
    is_teacher = forms.BooleanField(required=False, label='Register as Teacher')
    is_student = forms.BooleanField(required=False, label='Register as Student')
    
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'is_teacher', 'is_student']

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['specialty', 'bio']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['grade_level', 'interests']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        
        
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    
