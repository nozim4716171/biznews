from django.shortcuts import render
from .forms import LoginForm,UserRegistrationForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.urls import reverse


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                username = data['username'],
                password = data['password']
            )
            print(user)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('profile'))
                else:
                    return HttpResponse("<h2>Sizning akkauntingiz faol emas</h2>")
            else:
                return HttpResponse("<h2>Login yoki parolda xatolik mavjud</h2>")
    else:
        form = LoginForm()
        context = {
            'form' : form
        }
    return render(request, 'registration/login.html',context)


            
def dashboard(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'registration/dashboard.html', context)


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password1']
            )
            new_user.save()
            context = {
                'new_user': new_user
            }
            
            return render(request, 'registration/register_done.html',context)
        else:
            user_form = UserRegistrationForm()
            return render(request, 'registration/register.html',{'user_form': UserRegistrationForm()})
    else:
        user_form = UserRegistrationForm()
        context = {
            'user_form': user_form
        }
        return render(request, 'registration/register.html',context)