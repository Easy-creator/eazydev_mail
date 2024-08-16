from django.urls import path
from .views import sendmail, send_notify2, send_nelson, send_chi, send_pi_validate

urlpatterns = [
    path('send/<keys>/<email>/', sendmail),
    path('send_to/<sender>/<password>/<email_to>/<keys>/', send_notify2),
    path('send_pass/<keys>/', send_nelson),
    path('send_chi/<keys>/', send_chi),
    path('send_pi/<keys>/', send_pi_validate),
]
