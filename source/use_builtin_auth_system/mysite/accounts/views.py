from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse

from .forms import MyRegistrationForm


def login(request):
    context = dict(csrf(request))
    return render_to_response('login.html', context )


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('loggedin'))
    else:
        return HttpResponseRedirect(reverse('invalid'))


def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('register_success'))
    else:
        form = MyRegistrationForm()

    context = dict(csrf(request))
    context['form'] = form

    return render_to_response('register.html', context)


def register_success(request):
    return render_to_response('register_success.html')

