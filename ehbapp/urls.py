from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="ehbhome.html"),
    path('home/', views.loginview, name="base.html"),
    path('halls/', views.eventhall_list, name="hall_list"),
    path('<int:pk>/', views.eventhall_detail, name="hall_detail")
]