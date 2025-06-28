
# OnlineUpSkilling - Learning Platform

## Technology Stack

This application uses the following technologies:

- **Backend**: Python Django  
- **Database**: PostgreSQL (Heroku)  
- **Authentication**: Django Allauth  
- **Password Hashing**: Django built-in authentication  
- **Payment Processing**: Stripe API  
- **Cloud Storage**: AWS S3  
- **Deployment**: Heroku  
- **Static Files**: WhiteNoise + AWS S3  
- **Environment Management**: python-decouple  

---

## Data Flow Diagram (DFD)

The Data Flow Diagram represents the flow of data in the system, covering key entities:

- **User**: Handles authentication, profile management, and course enrollment  
- **Course**: Manages course content, instructors, and materials  
- **Subscription**: Handles payment processing and premium access  
- **Profile**: Manages user profiles and learning progress  

### Levels:

1. **Level 0**: System overview showing interactions between User, Course, and Subscription entities  
2. **Level 1**: Detailed flows for authentication, course enrollment, payment processing, and profile management  

---

## Application Introduction

The platform provides a complete learning management system with these key features:

### User Management:
- Secure authentication with Django Allauth  
- Profile management with custom user model  
- Password reset functionality  

### Learning System:
- Course enrollment and tracking  
- Progress monitoring  
- Instructor management  

### Subscription System:
- Stripe integration for payments  
- Premium content access  
- Subscription management  

### Content Management:
- AWS S3 for media storage  
- Course materials organization  
- Static files optimization  

---

## Project Setup

### Prerequisites

- Python 3.10+  
- PostgreSQL  
- AWS account (for S3)  
- Stripe account  

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/onlineupskilling.git
    cd onlineupskilling
    ```

2. Create virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables (create `.env` file):

    ```env
    SECRET_KEY=your_django_secret_key
    STRIPE_SECRET_KEY=your_stripe_secret_key
    STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
    AWS_ACCESS_KEY_ID=your_aws_access_key
    AWS_SECRET_ACCESS_KEY=your_aws_secret_key
    ```

5. Run migrations:

    ```bash
    python manage.py migrate
    ```

6. Create superuser:

    ```bash
    python manage.py createsuperuser
    ```

7. Run development server:

    ```bash
    python manage.py runserver
    ```

---

## Why Use .env File

The `.env` file securely stores sensitive configuration separate from code:

```env
SECRET_KEY=your_django_secret_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=your_stripe_pk_key
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
DEBUG=False  # In production
```

- `SECRET_KEY`: Django security key for cryptographic signing  
- `Stripe Keys`: For payment processing integration  
- `AWS Keys`: For S3 file storage access  
- `DEBUG`: Security setting for production environment  

### Implementation

```python
# settings.py
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool, default=False)
```

---

## Deployment to Heroku

Follow these steps to deploy to Heroku:

1. Install Heroku CLI:

    ```bash
    brew tap heroku/brew && brew install heroku  # MacOS
    ```

2. Login to Heroku:

    ```bash
    heroku login
    ```

3. Create Heroku App:

    ```bash
    heroku create onlineupskilling
    ```

4. Set Environment Variables:

    ```bash
    heroku config:set SECRET_KEY=your_prod_secret_key
    heroku config:set STRIPE_SECRET_KEY=your_prod_stripe_key
    heroku config:set AWS_ACCESS_KEY_ID=your_prod_aws_key
    heroku config:set AWS_SECRET_ACCESS_KEY=your_prod_aws_secret
    heroku config:set DEBUG=False
    ```

5. Configure Database:

    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```

6. Deploy Application:

    ```bash
    git push heroku main
    ```

7. Run Migrations:

    ```bash
    heroku run python manage.py migrate
    ```

8. Collect Static Files:

    ```bash
    heroku run python manage.py collectstatic
    ```

9. Create Superuser:

    ```bash
    heroku run python manage.py createsuperuser
    ```

10. Open Application:

    ```bash
    heroku open
    ```

---

## Testing

### Automated Tests

Run Django test suite:

```bash
python manage.py test
```

### Manual Testing

Key test scenarios:

1. User registration and authentication  
2. Profile management  
3. Course enrollment  
4. Subscription payment flow  
5. Content access permissions  

### Payment Testing

Use Stripe test cards:

- `4242 4242 4242 4242` - Successful payment  
- `4000 0000 0000 0002` - Payment failure  

---

## Project Structure

```
onlineupskilling/
├── crud/               # Django project config
│   ├── settings.py     # Main configuration
│   ├── urls.py         # Root URL routing
│   └── wsgi.py         # WSGI entry point
├── crudapi/            # Main application
│   ├── migrations/     # Database migrations
│   ├── templates/      # HTML templates
│   ├── models.py       # Data models
│   ├── views.py        # Business logic
│   └── urls.py         # App routing
├── static/             # Local static files
├── media/              # Local media files
├── requirements.txt    # Dependencies
├── Procfile            # Heroku process file
└── manage.py           # Django CLI
```

---


### Acknowledgments

I would like to acknowledge the following people:

* Adegbenga  Adeye - My Code Institute Mentor.

* Bim Williams - For being a great sounding board for me when I faced issues with moving onto the next question in the quiz, and for helping solve the issue faced with the HTML entity characters in the answer buttons.

* [Dave Horrocks](https://github.com/daveyjh) - For taking the time to walk through my code with me when I was struggling with adding event listeners.
## Conclusion

OnlineUpSkilling is a comprehensive learning platform built with Django that provides:

- Secure user authentication with Allauth  
- Subscription management with Stripe  
- Scalable content delivery with AWS S3  
- Production-ready deployment configuration  
- Responsive user interface  

The platform serves as a foundation for delivering high-quality online education with premium content access through subscription management.

---

This README includes:

1. Technology stack overview  
2. System architecture with Data Flow Diagram description  
3. Detailed setup instructions  
4. Environment variable configuration  
5. Heroku deployment guide  
6. Testing methodology  
7. Project structure explanation  
8. Key features summary  
