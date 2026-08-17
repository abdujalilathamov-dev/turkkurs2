from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dars/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('dars/<int:pk>/test/', views.lesson_test, name='lesson_test'),

    path('imtihon/', views.exam_info, name='exam_info'),
    path('imtihon/topshirish/', views.exam_take, name='exam_take'),

    path('sertifikat/<int:pk>/', views.certificate_view, name='certificate_view'),
    path('sertifikatlarim/', views.my_certificates, name='my_certificates'),
    path('sertifikat-tekshirish/', views.certificate_verify, name='certificate_verify'),

    path('reyting/', views.leaderboard, name='leaderboard'),
    path('royxatdan-otish/', views.register, name='register'),
    path('boshqaruv/', views.admin_dashboard, name='admin_dashboard'),
]
