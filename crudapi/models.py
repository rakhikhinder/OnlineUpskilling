
# Expert , admin and student models 
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialty = models.CharField(max_length=100)
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    grade_level = models.CharField(max_length=50)
    interests = models.TextField()
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = 'categories'
  
  
class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	description = models.CharField(max_length=250, default='', blank=True, null=True)
	image = models.ImageField(upload_to='product/')

	def __str__(self):
		return self.name

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.name}'

class Subscription(models.Model):
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('basic', 'Basic'),
        ('premium', 'Premium'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default='free')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan}"









