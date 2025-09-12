from django.http import Http404
from django.shortcuts import render
from .models import CarOwner


def owner_detail(request, owner_id):
    """
    Представление для отображения детальной информации о владельце автомобиля.
    """
    try:
        owner = CarOwner.objects.get(pk=owner_id)
    except CarOwner.DoesNotExist:
        raise Http404("Владелец автомобиля не найден")
    
    return render(request, 'owner.html', {'owner': owner})
