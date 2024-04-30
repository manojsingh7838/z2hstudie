from django.shortcuts import render ,redirect
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Feedback ,Enrollment
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    user=User.objects.all()
    context={
        user: user,
    }
    return render(request, 'form/index.html',context)

def login_view(request): 
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect('index')
        else:
            
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'form/login.html')

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        password_confirm = request.POST.get('pass2')
        email = request.POST.get('email')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'form/singin.html', {'error': 'Username already exists'})
        
        if password == password_confirm:
            try:
                
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                
                
                subject = 'Account Creation Confirmation'
                message = f'Hello {username},\n\nYour account has been successfully created. Thank you for registering!'
                from_email = settings.EMAIL_HOST_USER
                to_email = [email]
                send_mail(subject, message, from_email, to_email)
                
                return render(request, 'form/singin.html', {'success': 'Account created successfully. Please check your email for confirmation.'})
            except IntegrityError:
                return render(request, 'form/singin.html', {'error': 'Failed to create user'})
        else:
            return render(request, 'form/singin.html', {'error': 'Passwords do not match'})
    return render(request, 'form/singin.html')
def logout_view(request):
    logout(request)
    return redirect('index') 

def connect_view(request):
    if request.method == 'POST':
        name = request.POST.get('uname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        msg = request.POST.get('msg', '')

        try:
            # Save form data
            fomet = Feedback(name=name, email=email, phone=phone, msg=msg)
            fomet.save()

            # Send email
            subject = 'New Feedback from {}'.format(name)
            message = 'Name: {}\nEmail: {}\nPhone: {}\nMessage: {}'.format(name, email, phone, msg)
            from_email = settings.EMAIL_HOST_USER
            to_email = ['sushantkumar1060@gmail.com',
                        ]  
            send_mail(subject, message, from_email, to_email)

            
            enrollment_success = "Enrollment successful!"
            email_success = "Email sent successfully!"
            return render(request, 'form/form.html', {'enrollment_success': enrollment_success, 'email_success': email_success})
        except Exception as e:
            
            enrollment_error = "An error occurred while saving the data to the database."
            email_error = f"An error occurred while sending the email: {str(e)}"
            return render(request, 'form/form.html', {'enrollment_error': enrollment_error, 'email_error': email_error})
    
    return render(request, 'form/form.html')





@login_required
def webdev(request):
    enrollment_error = None
    email_error = None
    enrollment_success = None
    email_success = None

    if request.method == 'POST':
        username = request.POST.get('username', '')
        payment_date = request.POST.get('payment_date', '')
        transaction_id = request.POST.get('transaction_id', '')
        whatsapp_no = request.POST.get('whatsapp_no', '')

        
        try:
            enrollment = Enrollment.objects.create(
                username=username,
                payment_date=payment_date,
                transaction_id=transaction_id,
                whatsapp_no=whatsapp_no
            )
            enrollment.save()
            enrollment_success = "Enrollment successful!"
        except Exception as e:
            enrollment_error = "An error occurred while saving the data to the database."

        
        subject = 'New Web Development Course Enrollment'
        message = f'Username: {username}\nPayment Date: {payment_date}\nTransaction ID: {transaction_id}\nWhatsApp No: {whatsapp_no}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['sushantkumar1060@gmail.com']

        try:
            send_mail(subject, message, from_email, recipient_list)
            email_success = "Email sent successfully!"
        except Exception as e:
            email_error = f"An error occurred while sending the email: {str(e)}"


    return render(request, 'form/reg1.html', {'enrollment_error': enrollment_error, 'email_error': email_error, 'enrollment_success': enrollment_success, 'email_success': email_success})

@login_required
def python(request):
    enrollment_error = None
    email_error = None
    enrollment_success = None
    email_success = None

    if request.method == 'POST':
        username = request.POST.get('username', '')
        payment_date = request.POST.get('payment_date', '')
        transaction_id = request.POST.get('transaction_id', '')
        whatsapp_no = request.POST.get('whatsapp_no', '')

        
        try:
            enrollment = Enrollment.objects.create(
                username=username,
                payment_date=payment_date,
                transaction_id=transaction_id,
                whatsapp_no=whatsapp_no
            )
            enrollment.save()
            enrollment_success = "Enrollment successful!"
        except Exception as e:
            enrollment_error = "An error occurred while saving the data to the database."

        
        subject = 'New python Course Enrollment'
        message = f'Username: {username}\nPayment Date: {payment_date}\nTransaction ID: {transaction_id}\nWhatsApp No: {whatsapp_no}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['sushantkumar1060@gmail.com']

        try:
            send_mail(subject, message, from_email, recipient_list)
            email_success = "Email sent successfully!"
        except Exception as e:
            email_error = f"An error occurred while sending the email: {str(e)}"

    return render(request, 'form/reg2.html', {'enrollment_error': enrollment_error, 'email_error': email_error, 'enrollment_success': enrollment_success, 'email_success': email_success})

@login_required
def datasci(request):
    enrollment_error = None
    email_error = None
    enrollment_success = None
    email_success = None

    if request.method == 'POST':
        username = request.POST.get('username', '')
        payment_date = request.POST.get('payment_date', '')
        transaction_id = request.POST.get('transaction_id', '')
        whatsapp_no = request.POST.get('whatsapp_no', '')

        
        try:
            enrollment = Enrollment.objects.create(
                username=username,
                payment_date=payment_date,
                transaction_id=transaction_id,
                whatsapp_no=whatsapp_no
            )
            enrollment.save()
            enrollment_success = "Enrollment successful!"
        except Exception as e:
            enrollment_error = "An error occurred while saving the data to the database."

        
        subject = 'New datasic Course Enrollment'
        message = f'Username: {username}\nPayment Date: {payment_date}\nTransaction ID: {transaction_id}\nWhatsApp No: {whatsapp_no}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['sushantkumar1060@gmail.com']
        
        try:
            send_mail(subject, message, from_email, recipient_list)
            email_success = "Email sent successfully!"
        except Exception as e:
            email_error = f"An error occurred while sending the email: {str(e)}"

    return render(request, 'form/reg3.html', {'enrollment_error': enrollment_error, 'email_error': email_error, 'enrollment_success': enrollment_success, 'email_success': email_success})

@login_required
def machine(request):
    enrollment_error = None
    email_error = None
    enrollment_success = None
    email_success = None

    if request.method == 'POST':
        username = request.POST.get('username', '')
        payment_date = request.POST.get('payment_date', '')
        transaction_id = request.POST.get('transaction_id', '')
        whatsapp_no = request.POST.get('whatsapp_no', '')

        
        try:
            enrollment = Enrollment.objects.create(
                username=username,
                payment_date=payment_date,
                transaction_id=transaction_id,
                whatsapp_no=whatsapp_no
            )
            enrollment.save()
            enrollment_success = "Enrollment successful!"
        except Exception as e:
            enrollment_error = "An error occurred while saving the data to the database."

        
        subject = 'New ML Course Enrollment'
        message = f'Username: {username}\nPayment Date: {payment_date}\nTransaction ID: {transaction_id}\nWhatsApp No: {whatsapp_no}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['sushantkumar1060@gmail.com']
        try:
            send_mail(subject, message, from_email, recipient_list)
            email_success = "Email sent successfully!"
        except Exception as e:
            email_error = f"An error occurred while sending the email: {str(e)}"

    return render(request, 'form/reg4.html', {'enrollment_error': enrollment_error, 'email_error': email_error, 'enrollment_success': enrollment_success, 'email_success': email_success})

@login_required
def datatc(request):
    enrollment_error = None
    email_error = None
    enrollment_success = None
    email_success = None

    if request.method == 'POST':
        username = request.POST.get('username', '')
        payment_date = request.POST.get('payment_date', '')
        transaction_id = request.POST.get('transaction_id', '')
        whatsapp_no = request.POST.get('whatsapp_no', '')

        
        try:
            enrollment = Enrollment.objects.create(
                username=username,
                payment_date=payment_date,
                transaction_id=transaction_id,
                whatsapp_no=whatsapp_no
            )
            enrollment.save()
            enrollment_success = "Enrollment successful!"
        except Exception as e:
            enrollment_error = "An error occurred while saving the data to the database."

        
        subject = 'New data anilist Course Enrollment'
        message = f'Username: {username}\nPayment Date: {payment_date}\nTransaction ID: {transaction_id}\nWhatsApp No: {whatsapp_no}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['sushantkumar1060@gmail.com']

        try:
            send_mail(subject, message, from_email, recipient_list)
            email_success = "Email sent successfully!"
        except Exception as e:
            email_error = f"An error occurred while sending the email: {str(e)}"

    return render(request, 'form/reg5.html', {'enrollment_error': enrollment_error, 'email_error': email_error, 'enrollment_success': enrollment_success, 'email_success': email_success})
@login_required
def sql(request):
    enrollment_error = None
    email_error = None
    enrollment_success = None
    email_success = None

    if request.method == 'POST':
        username = request.POST.get('username', '')
        payment_date = request.POST.get('payment_date', '')
        transaction_id = request.POST.get('transaction_id', '')
        whatsapp_no = request.POST.get('whatsapp_no', '')

        # Save data to the database
        try:
            enrollment = Enrollment.objects.create(
                username=username,
                payment_date=payment_date,
                transaction_id=transaction_id,
                whatsapp_no=whatsapp_no
            )
            enrollment.save()
            enrollment_success = "Enrollment successful!"
        except Exception as e:
            enrollment_error = "An error occurred while saving the data to the database."

        # Send email
        subject = 'New sql Course Enrollment'
        message = f'Username: {username}\nPayment Date: {payment_date}\nTransaction ID: {transaction_id}\nWhatsApp No: {whatsapp_no}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['sushantkumar1060@gmail.com']

        try:
            send_mail(subject, message, from_email, recipient_list)
            email_success = "Email sent successfully!"
        except Exception as e:
            email_error = f"An error occurred while sending the email: {str(e)}"
            
    return render(request, 'form/reg6.html', {'enrollment_error': enrollment_error, 'email_error': email_error, 'enrollment_success': enrollment_success, 'email_success': email_success})
