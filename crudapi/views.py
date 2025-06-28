from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Teacher, Student
from .forms import UserRegisterForm, TeacherProfileForm, StudentProfileForm
def dashboard(request):
     products = [
       
         {"name": "Django Programming", "price": 18.75, "image": "django.jpg"},
         {"name": "Django Programming", "price": 18.75, "image": "django.jpg"},
         {"name": "Django Programming", "price": 18.75, "image": "django.jpg"},
         {"name": "Django Programming", "price": 18.75, "image": "django.jpg"},
         {"name": "Django Programming", "price": 18.75, "image": "django.jpg"},
         {"name": "Django Programming", "price": 18.75, "image": "django.jpg"},
        
    ]
     
     return render(request, 'dashboard.html', {'products': products})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Create profile based on user type
            if form.cleaned_data.get('is_teacher'):
                Teacher.objects.create(user=user)
                user.is_teacher = True
            elif form.cleaned_data.get('is_student'):
                Student.objects.create(user=user)
                user.is_student = True
            user.save()
            
            login(request, user)
            return redirect('profile_complete')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile_complete(request):
    if request.user.is_teacher:
        form_class = TeacherProfileForm
    elif request.user.is_student:
        form_class = StudentProfileForm
    else:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = form_class(request.POST, instance=request.user.teacher if request.user.is_teacher else request.user.student)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = form_class(instance=request.user.teacher if request.user.is_teacher else request.user.student)
    
    return render(request, 'profile_complete.html', {'form': form})



