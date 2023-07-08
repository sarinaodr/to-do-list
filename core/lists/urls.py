from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = 'lists'

urlpatterns = [
    path('list/' , views.DoList.as_view() , name='do-list'),
    path('list/create' , views.ListCreateView.as_view() , name='list-create'),
    path('list/<int:pk>/edit/' , views.ListEditView.as_view() , name = 'list-edit'),
    path('list/<int:pk>/' , views.ListDeleteView.as_view() , name='list-delete')
]
