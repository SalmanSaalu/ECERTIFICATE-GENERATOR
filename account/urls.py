from django.urls import path


from . import views
from .views import send_json

urlpatterns = [
    
    # path('signin',signinView.as_view(),name='signin'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('send_json', send_json, name='send_json'),
# path('signin',views.signin,name='signin'),
]