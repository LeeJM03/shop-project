
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from .models import Member
from .forms import LoginForm

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        name = request.POST.get('name', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        email = request.POST.get('email', None)

        res_data = {}
        if not (name and username and password and re_password and email):
            res_data['error'] = 'Please enter all the values!'

        elif password != re_password:
            res_data['error'] = "The password doesn't match!"
            print(res_data)

        else:
            member = Member (
                name = name,
                username = username,
                email = email,
                password = make_password(password),
            )
            member.save()
            return redirect('/shop')

        return render(request, 'register.html', res_data)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # session_code 검증하기
            request.session['user'] = form.user_id
            return redirect('/shop')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})