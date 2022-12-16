from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UserUpdateForm, ProfileForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form_2 = ProfileForm(request.POST)
        if form.is_valid() and form_2.is_valid():
            user = form.save()
            profile = form_2.save(commit=False)
            group = Group.objects.get_or_create(name='staff')
            user.groups.add(group[0])
            profile.seller = user
            profile.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()
        form_2 = ProfileForm()
    context = {
        'form': form,
        'form_2': form_2,
    }
    return render(request, 'user/register.html', context)


def profile(request):
    context = {

    }
    return render(request, 'user/profile.html', context)


def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'user/profile_update.html', context)