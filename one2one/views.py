from django.shortcuts import render
from django.http import *
from datetime import *
from .models import *
from .forms import *


def form2(request):
    if request.method =='POST':
        form = useremp(request.POST)
        form1 = emp(request.POST, request.FILES)

        if form.is_valid() and form1.is_valid() :
            form.save()
            u = User.objects.get(username=form.cleaned_data['username'])
            f = form1.save(commit=False)
            f.user = u
            f.save()

            return HttpResponseRedirect('/detail/')

    else:
            form = useremp()
            form1 = emp()
    return render(request, 'home.html', { 'form': form, 'form1':form1 })


def detail(request):
    user = Emp.objects.all()

    return render(request, 'profile.html', {'usr':user})



# Create your views here.
