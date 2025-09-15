from django.http import Http404
from django.shortcuts import render
from .models import CarOwner, Car
from django.views.generic import ListView, DetailView


def owner_detail(request, owner_id):
    """
    Представление для отображения детальной информации о владельце автомобиля.
    """
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Владелец автомобиля не найден")
    
    return render(request, 'owner_detail.html', {'owner': owner})


def owners_list(request):
    """
    Представление для отображения списка всех владельцев автомобилей.
    """
    owners = CarOwner.objects.all()
    return render(request, 'owners_list.html', {'owners': owners})


def owner_create():
    pass


class CarsListView(ListView):
    model = Car
    template_name = 'cars_list.html'
    context_object_name = 'cars'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'
    pk_url_kwarg = 'car_id'
