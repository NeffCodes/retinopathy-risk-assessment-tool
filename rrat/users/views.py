from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages #Import messages module

# Registration view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect("/")  # Redirect to home or desired page after registration
    else:
        form = UserCreationForm()

    args = {"form": form}
    return render(request, "users/register.html", args)

# Login view
def login_view(request):
    error_message = None  # Initialize error message variable
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, f'Welcome back, {username}!')  # Add success message
                return redirect("home")  # Redirect to the home page
            else:
                error_message = "Invalid login credentials"  # Handle invalid credentials
        else:
            error_message = "Invalid login credentials"  # Handle invalid form submission
    else:
        form = AuthenticationForm()

    args = {
        "form": form,
        "error_message": error_message
    }
    return render(request, "users/login.html", args)

