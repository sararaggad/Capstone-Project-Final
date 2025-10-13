from django.contrib import messages
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Car
from .forms import CarForm

def car_list(request):
    return render(request, 'car_list.html', {'cars': Car.objects.all()})

def car_detail(request, pk):
    return render(request, 'car_detail.html', {'car': get_object_or_404(Car, pk=pk)})

@login_required
def car_create(request):
    form = CarForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save(); return redirect('car_list')
    return render(request, 'car_form.html', {'form': form})

@login_required
def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarForm(request.POST or None, instance=car)
    if request.method == 'POST' and form.is_valid():
        form.save(); return redirect('car_list')
    return render(request, 'car_form.html', {'form': form})

@login_required
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete(); return redirect('car_list')
    return render(request, 'car_confirm_delete.html', {'car': car})
from django.core.paginator import Paginator

def car_list(request):
    qs = Car.objects.all()
    q = request.GET.get('q', '')
    status = request.GET.get('status', '')
    if q:
        qs = qs.filter(models.Q(brand__icontains=q) | models.Q(title__icontains=q) | models.Q(plate_no__icontains=q))
    if status:
        qs = qs.filter(status=status)
    paginator = Paginator(qs, 8)  # 8 عناصر بالصفحة
    page = request.GET.get('page')
    cars = paginator.get_page(page)
    return render(request, 'car_list.html', {'cars': cars, 'q': q, 'status': status})
messages.success(request, "Saved")     # بعد form.save()
messages.success(request, "Deleted")   # بعد delete()
