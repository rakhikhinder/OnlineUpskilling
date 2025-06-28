
# OnlineUpSkilling - Learning Platform
Visit the deployed site: OnlineUpSkilling

Empowering learners through accessible, scalable, and secure online education. OnlineUpSkilling is a modern learning platform with subscription-based premium content access, secure authentication, and cloud media delivery.
![OnlineUpSkilling-Learning Platform](https://github.com/rakhikhinder/OnlineUpskilling/blob/card/image%201%20.jpeg)

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
  * [Features](#features)
    * [The Home Page](#the-home-page)
    * [The login Page](#the-login-page)
    * [The subscription Page](#the-subscription-page)
    * [The 404 Error Page](#the-404-error-page)
    * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)
  * [Solved Bugs](#solved-bugs)
  * [Known Bugs](#known-bugs)
  
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

- - -
![onlineupskilling]()

## User Experience (UX)

### User Stories




User Experience (UX)
User Stories
First Time Visitor Goals
I want to browse available courses and understand what the platform offers.

I want to register an account securely and enroll in free or premium courses.

I want to trust the payment process for upgrading to premium.

Returning Visitor Goals
I want to log in and continue with my progress.

I want to view my profile and manage my courses or subscription.

Frequent Visitor Goals
I want to monitor my learning progress.

I want to manage my subscription or change my payment method.

#### Frequent Visitor Goals
I want to monitor my learning progress.

I want to manage my subscription or change my payment method.

## Design

### Colour Scheme
A clean, modern palette with contrasting elements for readability:

#ffffff – primary background

#202124 – dark header/footer

#4CAF50 – call-to-action (CTA), buttons

#f44336 – warnings, delete actions

Text primarily uses black/grey with proper contrast

 ### Typography
Headings: Poppins – modern, readable sans-serif

Body Text: Roboto – for clarity and web-optimized readability

 ### Wireframes
Created using Balsamiq:

Home Page

Course Detail Page

User Dashboard

Subscription Checkout
### Features
### User Management
Registration, login, password reset (Django Allauth)

Custom user profiles with learning stats

Admin interface for managing users
Features
User Management
Registration, login, password reset (Django Allauth)

Custom user profiles with learning stats

 Admin interface for managing users

### Learning System
Course listing, enrollment, and tracking

Course progress view

Instructors can upload/manage content

### Subscription System
Stripe API for secure payments

Premium access logic via subscription status

Billing management via Stripe dashboard

### Media & Static Content
AWS S3 for user uploads and course media

Static file handling via WhiteNoise and S3

Optimized file delivery and caching

### Error Pages
Custom 404 and 500 pages with navigation options
#### The Home Page
Level up your skills and unlock your potential — one course at a time.

OnlineUpSkilling is a modern learning platform designed to help individuals and teams improve their knowledge and stay ahead in today’s fast-paced digital world. Whether you're just starting out or looking to deepen your expertise, we offer a range of courses from trusted instructors to suit every level.

#### 🧠 Learn anytime, anywhere
#### 📚 Track your progress
#### 💳 Access premium content with ease
#### 🌍 Built for individuals and teams


### 🔐 Login Page 
Welcome Back to OnlineUpSkilling!
Log in to continue your learning journey.

Access your enrolled courses

Track your progress and achievements

Manage your profile and settings

View your current subscription status

### 👋 Don’t have an account yet? Sign Up here

### 🛠️ Forgot your password? Reset it here

### 💳 Subscription Page Text
Unlock Premium Learning with OnlineUpSkilling+
Ready to take your learning to the next level?

With a Premium Subscription, you’ll gain access to:

### ✅ All premium courses and modules
### ✅ Exclusive instructor-led masterclasses
### ✅ Downloadable materials and certificates
### ✅ Priority support and early access to new content

Just £X.XX/month — cancel anytime.
### Future Implementations
Course ratings and feedback

Email notifications for new content

Quiz module with auto-grading

Leaderboards for gamified learning

Mobile-native app with same backend

Accessibility
Efforts made to enhance accessibility:

Semantic HTML5 tags

Descriptive alt text for all images

Sufficient color contrast

Keyboard-accessible forms and buttons

Responsive layout on all devices

Planned enhancements:

ARIA attributes for screen readers

Captions/transcripts for media

### Technologies Used
Languages
HTML, CSS, JavaScript (for interactivity)

Python (Django)

Backend & Database
Django

PostgreSQL (Heroku addon)

Authentication
Django Allauth

Password hashing via Django default system

Payment & Media
Stripe API

AWS S3

DevOps
### Heroku deployment

python-decouple for managing environment variables

WhiteNoise for static file management

Deployment & Local Development
Deployment
Deployed to Heroku: OnlineUpSkilling

Steps to deploy:

Set up Heroku CLI

Create app: heroku create onlineupskilling

Set config vars:
heroku config:set SECRET_KEY=... STRIPE_SECRET_KEY=... AWS_ACCESS_KEY_ID=...
Add Heroku Postgres:
heroku addons:create heroku-postgresql:hobby-dev
Push to Heroku: git push heroku main

Run migrations: heroku run python manage.py migrate

Create superuser: heroku run python manage.py createsuperuser

Collect static: heroku run python manage.py collectstatic

Local Development
How to Fork
Log in to GitHub and open the repo

Click the "Fork" button (top-right)

How to Clone
bash
Copy
Edit
git clone https://github.com/yourusername/onlineupskilling.git
cd onlineupskilling
Create .env:

env
SECRET_KEY=...
DEBUG=True
STRIPE_SECRET_KEY=...
AWS_ACCESS_KEY_ID=...
Create virtual environment:
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate for Windows
pip install -r requirements.txt
Run migrations and start server:
python manage.py migrate
python manage.py runserver
Testing
Automated Testing
To run all tests:
python manage.py test
Includes:

User model/unit tests

Subscription logic

Payment callback handlers

### Manual Testing
User registration/login/password reset

Payment flow with Stripe test cards

Course access control

### Media upload/viewing

Admin dashboard access and restrictions

Stripe test card:

4242 4242 4242 4242 – success

4000 0000 0000 0002 – decline

### Project Structure
bash
Copy
Edit
onlineupskilling/
├── crud/               # Django project config
├── crudapi/            # Application logic
│   ├── models.py       # Data models
│   ├── views.py        # Logic and views
│   ├── urls.py         # Routing
│   ├── templates/      # HTML files
├── static/             # Static assets
├── media/              # Uploaded media files
├── requirements.txt
├── .env
├── Procfile            # Heroku-specific
└── manage.py
Credits
Code Resources
Django Allauth Docs

Stripe Python SDK

AWS S3 Django Integration

Heroku Django Deployment

Media & Icons
All icons from FontAwesome

Stock images via Unsplash

### Acknowledgments
Special thanks to:

Adegbenga Adeye – Code Institute Mentor

Bim Williams – For debugging and deployment advice

Dave Horrocks – Technical guidance

Abi Harrison – UX and accessibility suggestions


n  
- Static files optimization  

---

## Project Setup

### Prerequisites

- Python 3.10+  
- PostgreSQL  
- AWS account (for S3)  
- Stripe account  

