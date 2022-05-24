from django.urls import path


from . import views
from .views import issueCertificate,Certificateparttwo


urlpatterns=[
    path('',views.first,name='first'),
    path('issuecertificate',issueCertificate.as_view(),name='issuecertificate'),
    path('certificateparttwo',Certificateparttwo.as_view(),name='certificateparttwo'),
    path('status',views.status,name='status')
    
    
    ]