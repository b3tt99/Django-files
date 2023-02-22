from django.shortcuts import render
from .forms import UserReg
from .forms import MembersReg


def reg(request):
    submit_button = request.POST.get("sam")
    name = ''
    email = ''
    password = ''

    reg_form = UserReg(request.POST or None)
    if reg_form.is_valid():
        name = reg_form.cleaned_data.get("name")
        email = reg_form.cleaned_data.get("email")
        password = reg_form.cleaned_data.get("password")
    context = {'reg_form': reg_form, 'name': name, 'email': email, 'submit_button': submit_button}

    return render(request, 'register.html', context)


def reg_members(request):
    submit_members = request.POST.get("members")
    name = ''
    age = ''
    phone = ''
    city = ''
    country = ''

    member_form = MembersReg(request.POST or None)
    if member_form.is_valid():
        name = member_form.cleaned_data.get("name")
        age = member_form.cleaned_data.get("age")
        phone = member_form.cleaned_data.get("phone")
        city = member_form.cleaned_data.get("city")
        country = member_form.cleaned_data.get("country")
    context = {'member_form':member_form, 'name':name, 'age':age, 'phone':phone, 'city':city, 'country':country,'submit_members':submit_members }
    return render(request, 'members.html', context)
