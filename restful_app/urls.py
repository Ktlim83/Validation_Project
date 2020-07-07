from django.urls import path
from . import views

urlpatterns = [
    # local8000/shows
    path('', views.index),
    
    # local8000/shows/new
    path('new',views.new),
    
    # local8000/shows/create
    path('create',views.create),
    
    # local8000/shows/<show_id>/edit
    path('<int:show_id>/edit', views.edit),
    
    # local8000/shows/<show_id>/update
    path('<int:show_id>/update', views.update),
    
    # local8000/shows/<show_id>/delete
    path('<int:show_id>/delete', views.delete),
    
    # local8000/shows/<shows_id>
    path('<int:show_id>',views.show),
    
    
]

