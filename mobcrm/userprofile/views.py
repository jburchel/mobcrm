from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")  # Redirect to home page after login
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="userprofile/login.html", context={"form":form})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user,
                organization_name=form.cleaned_data.get('organization_name'),
                role=form.cleaned_data.get('role')
            )
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserCreationForm()
    return render(request=request, template_name="userprofile/signup.html", context={"form":form})

@login_required
def user_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'userprofile/user_detail.html', {'user': user})

@login_required
def my_account(request):
    user = request.user
    profile = user.userprofile  # Assuming you have a OneToOneField relationship

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('userprofile:my_account')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'userprofile/my_account.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')  # or wherever you want to redirect after logout