from django.urls import path
from . import views


urlpatterns = [
    path('', views.root_redirect),
    path('owner/<int:owner_id>/', views.owner_detail, name='owner_detail'),
    path('owner/list/', views.owners_list, name='owners_list'),
    path('car/list/', views.CarsListView.as_view(), name='cars_list'),
    path('car/<int:car_id>/', views.CarDetailView.as_view(), name='car_detail'),
    path('owner/create/', views.create_owner, name='create_owner'),
    path('owner/edit/<int:owner_id>/', views.edit_owner, name='edit_owner'),
    path('owner/delete/<int:owner_id>/', views.delete_owner, name='delete_owner'),
]
