from django.shortcuts import render
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, plain_text_content
import environ

# initialising the environ
# your environment variable must be in the same folder where your setting.py is
# spaces are not allowed in env file ensure that there is no space in your env file
env = environ.Env()
environ.Env.read_env()
# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        sender = request.POST.get("email")
        body = request.POST.get('message')
        # if you change the from_email to an email that not registered as the from on your twilio account then it will flag you
        message = Mail(from_email="durosakindickson@gmail.com",
                       # when you make an error in typing twillio is just going to say('ForbiddenError' object has no attribute 'message')
                       to_emails="femimathias39@gmail.com",
                       subject=f"From {name}",
                       plain_text_content=f"Sender: {sender}\n\n{body}")
        try:
            sg = SendGridAPIClient(env('sendgridkey'))
            response = sg.send(message)
            print(response.status_code)
        except Exception as e:
            print(e.message)

    return render(request, 'dickson/index.html')
