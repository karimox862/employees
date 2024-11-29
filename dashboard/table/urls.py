from django.urls import path
from . import views
from .views import generate_pdf

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('generate-pdf/<int:employee_id>/', generate_pdf, name='generate_pdf'),
    path('test-404/', views.test_404, name='test_404'),
]
