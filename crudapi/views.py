from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Teacher, Student,Product
from .forms import UserRegisterForm, TeacherProfileForm, StudentProfileForm, CommentForm,SubscriptionForm
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.http import HttpResponse
import json
from .models import Subscription

def dashboard(request):
     products = Product.objects.all()
     
     return render(request, 'dashboard.html', {'products': products})

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('product', pk = product.pk)
    else:
        form = CommentForm
    product = Product.objects.get(id = pk)
    return render(request, 'product.html',{'product': product,'comments': comments, 'form': form}) 


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
stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_payment_intent(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            amount = data.get('amount')  # In cents
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                metadata={'integration_check': 'accept_a_payment'},
            )
            return JsonResponse({'clientSecret': intent['client_secret']})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

def admin_dashboard(request):
    return HttpResponse("Welcome to the Admin Dashboard!")
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription, created = Subscription.objects.get_or_create(user=request.user)
            subscription.plan = form.cleaned_data['plan']
            subscription.active = True
            subscription.save()
            return redirect('subscription_success')
    else:
        form = SubscriptionForm()
    return render(request ,'subscription_success.html',{'form': form})
def subscription_success(request):
    return render(request, 'subscription_success.html')






