from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView
from django.views.generic.base import View
from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


def ForgetFormView(request):
    if (request.method=='POST'):
        try:
            user = get_object_or_404(CustomUser,username=request.POST['username'])
        except:

            error_message = "Username does not exists. Try again."
            return render(request,'ForgetForm.html',context={'error_message':error_message})
        else:
            user
            return redirect('users:SecurityQuestion',pk=user.pk)

    else:
        return render(request,'ForgetForm.html')


def SecurityQuestion(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    error_message='Wrong answer. Try again'
    if request.method=="GET":

        context={
            'user':user,
        }
        return render(request,'SecurityQuestion.html',context=context)

    else:
        if(user.answer == request.POST['sec_ans']):

            request.session['semaphore']=True

            return redirect('users:NewPass', pk=pk)
        else:
            context = {
                'user': user,
                'error_message': error_message
            }
            return render(request, 'SecurityQuestion.html', context=context)


def NewPass(request, pk):
    '''
    print ("entering newpass")
    semaphore= request.session.get('semaphore')
    print (semaphore)
    if (semaphore== None or semaphore==False):

        return redirect('login')
    else:
        request.session['semaphore']=False
        user = get_object_or_404(CustomUser, pk=pk)
        if request.method=='POST':
            print("req == post")
            if(request.POST['pass1']==request.POST['pass2']):
                user.set_password(request.POST['pass1'])
                user.save()
                print('User saved')
                return HttpResponse("hello")
            else:
                return render(request,'NewPass.html',{'error':'Passwords didnt match'})

        else:
            print("rendering newpass")
            return render(request,'NewPass.html')
            '''
    if request.method=="GET":
        semaphore = request.session.get('semaphore')
        if (semaphore == None or semaphore == False):
            return redirect('login')
        else:
            print("rendering newpass")
            return render(request,'NewPass.html')

    else:
        request.session['semaphore'] = False
        user = get_object_or_404(CustomUser, pk=pk)
        if (request.POST['pass1'] == request.POST['pass2']):
            user.set_password(request.POST['pass1'])
            user.save()
            print('User saved')
            return HttpResponse("hello")
        else:
            return render(request, 'NewPass.html', {'error': 'Passwords didnt match'})







