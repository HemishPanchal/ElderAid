from django.shortcuts import render, redirect
from elder_services.models import user_info
from .forms import SignupForm,LoginForm

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()  # Saves uname and pwd to user_info table
            return redirect("login_page")
    else:
        form = SignupForm()

    return render(request, "registration/signup.html", {"form": form})


# Login view with cookie setting
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data["uname"]
            pwd = form.cleaned_data["pwd"]

            try:
                user = user_info.objects.get(uname=uname, pwd=pwd)
                request.session["user_id"] = user.id
                request.session["uname"] = user.uname
                return redirect("get_service")
            except user_info.DoesNotExist:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "registration/login.html", {"form": form})

def logout_view(request):
    request.session.flush()  # Clears all session data
    return redirect('home')  # Or 'home' if you want to go to the home page
