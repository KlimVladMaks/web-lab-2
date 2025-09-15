from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Owner, Car
from .forms import OwnerForm


def root_redirect(request):
    return redirect('owners_list')


def owner_detail(request, owner_id):
    """
    Представление для отображения детальной информации о владельце автомобиля.
    """
    try:
        owner = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Владелец автомобиля не найден")
    
    return render(request, 'owner_detail.html', {'owner': owner})


def owners_list(request):
    """
    Представление для отображения списка всех владельцев автомобилей.
    """
    owners = Owner.objects.all()
    return render(request, 'owners_list.html', {'owners': owners})


def create_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owners_list')
    else:
        form = OwnerForm()
    return render(request, 'create_owner.html', {'form': form})


def edit_owner(request, owner_id):
    owner = get_object_or_404(Owner, id_owner=owner_id)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owners_list')
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'edit_owner.html', {'form': form, 'owner': owner})


class CarsListView(ListView):
    model = Car
    template_name = 'cars_list.html'
    context_object_name = 'cars'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'
    pk_url_kwarg = 'car_id'
