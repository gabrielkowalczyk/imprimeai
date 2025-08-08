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
    path('pedido-finalizado/', views.pedido_finalizado, name='pedido_finalizado'),
]