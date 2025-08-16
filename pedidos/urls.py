from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cadastro/', views.register_user, name='register_user'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name='logout'),
    path('fazer-pedido/', views.fazer_pedido, name='fazer_pedido'), 
    path('finalizar-pedido/<int:pedido_id>/', views.finalizar_pedido, name='finalizar_pedido'),
    path('pedido-finalizado/', views.pedido_finalizado, name='pedido_finalizado'),
    path('confirmar-pedido/<int:pedido_id>/', views.confirmar_pedido, name='confirmar_pedido'),
    path('confirmar-endereco/<int:pedido_id>/', views.confirmar_endereco, name='confirmar_endereco'),
    
    # URLs de redefinição de senha
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('finalizar-pagamento/<int:pedido_id>/', views.finalizar_pagamento, name='finalizar_pagamento'),
]