from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from users.models import Messages, Users

def LoginView(request):
    """View to render the login view
    Returns:
        response: with a render of login.html if request method isn't POST,
                  a render of home if user is logged or an error message if
                  data login are wrong
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # check if username + password are valid and login the user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect to home - react frontend
            return redirect('chat')
        else:
            return render(request, 'login.html', {'error': 'Invalid Username or Password'})
    return render(request, 'login.html')

@login_required
def ChatView(request):
    return render(request, 'chat.html')

@login_required
def LogoutView(request):
    logout(request)
    return redirect('login')


def SignupView(request):

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirmation']
        # Validations Pass
        if password != password_confirm:
            error = 'The passwords do not match.'
            return render(request, 'signup.html', {'error': error})
        # email filter
        user_with_email = User.objects.filter(email=email)
        # email exist?
        if user_with_email:
            error = f'There is another account using {email}'
            return render(request, 'signup.html', {'error': error})
        # user filter
        us = User.objects.filter(username=username)
        # user exist?
        if us:
            error = f'There is another account using {username}'
            return render(request, 'signup.html', {'error': error})
        # creating user
        try:
            user = User.objects.create_user(username=username, password=password)
            print('uno')
            user.save()
            new_user = Users(user=user)
            print('dos')
            new_user.first_name = request.POST['firstname']
            new_user.last_name = request.POST['lastname']
            new_user.email = email
            new_user.save()
            login(request, user)
            # if create is complete, redirect to chat view
            return redirect('chat') 
        except IntegrityError as ie:
            error = f'There is another account using {username}'
            return render(request, 'signup.html', {'error': error})

    return render(request, 'signup.html')
