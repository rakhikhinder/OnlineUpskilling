from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Teacher, Student, Product, Subscription
from .forms import (
    UserRegisterForm,
    TeacherProfileForm,
    StudentProfileForm,
    CommentForm,
    SubscriptionForm,
)
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY

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
            return redirect('product', pk=product.pk)
    else:
        form = CommentForm()
    return render(request, 'product.html', {'product': product, 'comments': comments, 'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            if form.cleaned_data.get('is_teacher'):
                Teacher.objects.create(user=user)
                user.is_teacher = True
            elif form.cleaned_data.get('is_student'):
                Student.objects.create(user=user)
                user.is_student = True
            user.save()

            Subscription.objects.create(user=user, plan='free')
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
        form = form_class(request.POST, request.FILES, instance=request.user.teacher if request.user.is_teacher else request.user.student)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = form_class(instance=request.user.teacher if request.user.is_teacher else request.user.student)
    return render(request, 'profile_complete.html', {'form': form})

@login_required
def profile_show(request):
    try:
        if hasattr(request.user, 'teacher'):
            profile = request.user.teacher
            profile_type = 'teacher'
        elif hasattr(request.user, 'student'):
            profile = request.user.student
            profile_type = 'student'
        else:
            return HttpResponse("You don't have a profile.")

        return render(request, 'profileshow.html', {
            'profile': profile,
            'profile_type': profile_type,
        })
    except ObjectDoesNotExist:
        return HttpResponse("Profile does not exist.")

@csrf_exempt
def create_payment_intent(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            amount = data.get('amount')
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                metadata={'integration_check': 'accept_a_payment'},
            )
            return JsonResponse({'clientSecret': intent['client_secret']})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        customer_email = session.get('customer_email')
        plan_id = session['display_items'][0]['plan']['id'] if 'display_items' in session else None
        try:
            user = User.objects.get(email=customer_email)
            subscription = Subscription.objects.get(user=user)
            if 'basic' in plan_id:
                subscription.plan = 'basic'
            elif 'premium' in plan_id:
                subscription.plan = 'premium'
            subscription.active = True
            subscription.save()
        except Exception:
            pass

    return HttpResponse(status=200)

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out... Thanks for stopping by...")
    return redirect('dashboard')

def admin_dashboard(request):
    return HttpResponse("Welcome to the Admin Dashboard!")

@login_required
def subscribe(request):
    if request.method == 'POST':
        plan = request.POST.get('plan')
        price_lookup = {
            'basic': 'price_1RdrPSRoiR3JrmosCz8947M6',
            'premium': 'price_1RdrQ0RoiR3JrmosBYfBLpHD',
        }

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode='subscription',
            line_items=[{
                'price': price_lookup.get(plan),
                'quantity': 1,
            }],
            success_url=request.build_absolute_uri('/subscribe/success/'),
            cancel_url=request.build_absolute_uri('/subscribe/cancel/'),
            customer_email=request.user.email,
        )

        return redirect(session.url)

    return render(request, 'subscribe.html')

@login_required
def subscription_success(request):
    return render(request, 'subscription_success.html')

def about(request):
    return render(request, 'about.html')
    
@login_required
def subscription_cancel(request):
    return render(request, 'subscription_cancel.html')
