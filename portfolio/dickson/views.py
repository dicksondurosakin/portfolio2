from django.shortcuts import render
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, plain_text_content
import environ
# initialising the environ
env = environ.Env()
environ.Env.read_env()
# Create your views here.


def index(request):
    if request.method == 'POST':
        message = Mail(from_email='request.POST.get("email")',
                       to_emails='durosakindickson@gmail.com',
                       subject='Testing',
                       plain_text_content='Please work without much hassle',
                       html_content='<strong>I love that Gbemi girl</strong>')
        try:
            sg = SendGridAPIClient(env('sendgridkey'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
        print("dickson")
        print(request.POST.get('message'))
    return render(request, 'dickson/index.html')
