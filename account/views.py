from email import message
from django.shortcuts import redirect, render,HttpResponse
from django.views import View
from  django.contrib.auth.models import User,auth
from django.http import HttpResponse, JsonResponse
from home.models import status

# Create your views here.
def signup(request):
    try:
        if request.method=="POST":
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']


                   
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            ww=status.objects.create(statusname=request.user.id)
            ww.save()
            return redirect('/')
    except:
        return redirect('/')

# class signinView(View):
def signin(request):
        try:
            p1=request.GET.get('password',None)
            username=request.GET.get('username',None)
            # r=User.object.get(id=request.user.id)
            # if(p1==r.password):
            user=auth.authenticate(username=username,password=p1)
            if user:
                
                # print('worj')
                auth.login(request,user)
                p='**successfully loggined'
                response={'password':p}
                return JsonResponse(response)
            else:
                p='**please type the password correctly'
                response={'password':p}
                return JsonResponse(response)

            # return redirect(request.META['HTTP_REFERER'])
        except:
            pass


def logout(request):
    auth.logout(request)
    return  redirect('/')


def send_json(request):
       print('work')
       data = [{'name': 'Peter', 'email': 'peter@example.org'},
            {'name': 'Julia', 'email': 'julia@example.org'}]

       return JsonResponse(data, safe=False)
        