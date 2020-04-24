from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.FileUploadView.as_view()),
    path('users/', views.join),
    path('users/<int:pk>/', views.user_detail),
    path('login/', views.login),
    path('cars/', views.car),
    path('cars/<int:num>/', views.car_datail),
    path('cars/company/<str:company>/', views.car_company_list),
    path('cars/name/<str:name>/', views.car_name_list),
    # path('cars/company_list/', views.car_companyAll)
]
