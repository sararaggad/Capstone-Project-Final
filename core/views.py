from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Car
from .forms import CarForm


def car_list(request):
    qs = Car.objects.all().order_by('-created_at')
    q = request.GET.get('q', '')
    status = request.GET.get('status', '')
    if q:
        qs = qs.filter(Q(brand__icontains=q) | Q(title__icontains=q) | Q(plate_no__icontains=q))
    if status:
        qs = qs.filter(status=status)
    cars = Paginator(qs, 8).get_page(request.GET.get('page'))
    return render(request, 'car_list.html', {'cars': cars, 'q': q, 'status': status})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_detail.html', {'car': car})


@login_required
def car_create(request):
    form = CarForm(request.POST or None, files=request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        car = form.save()
        messages.success(request, 'Saved')
        return redirect('car_list')
    return render(request, 'car_form.html', {'form': form})


@login_required
def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarForm(request.POST or None, instance=car)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Saved')
        return redirect('car_detail', pk=car.pk)
    return render(request, 'car_form.html', {'form': form})


@login_required
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        messages.success(request, 'Deleted')
        return redirect('car_list')
    return render(request, 'car_confirm_delete.html', {'car': car})
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Account created")
        return redirect("car_list")
    return render(request, "registration/signup.html", {"form": form})
from django.contrib.auth.decorators import login_required


