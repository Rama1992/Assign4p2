from django.shortcuts import render
from ehbapp.models import EventHall
from django.contrib.auth.decorators import login_required
from ehbapp.decorators import employee_required, customer_required
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserLoginForm
from accounts.models import CustomUser
import datetime

# Create your views here.
def home(request):
    return render(request, 'ehbhome.html')

@login_required()
def loginview(request):
    return render(request, 'base.html')

def eventhall_list(request):
    halls_list = EventHall.objects.all()
    context = {
        'halls': halls_list
    }
    return render(request, 'hall_list.html', context)


def eventhall_detail(request, pk):
    hall = EventHall.objects.get(pk=pk)
    #hall = EventHall.objects.filter(hall_id)
    context = {
        'hall': hall
    }
    return render(request, 'hall_detail.html', context)

