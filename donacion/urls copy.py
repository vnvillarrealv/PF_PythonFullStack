from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),#muestra la pantalla principal
    path('catalogo_camp/',views.catalogo_camp, name='catalogo_camp'),#muesra el catalogo de las campañas
    path('perfil_detallado_camp/<int:camp_id>/',views.perfil_detallado_camp, name='perfil_detallado_camp'),#muestra la info de cada campaña
    path('ventana_aporte/', views.ventana_aporte, name ='ventana_aporte'),
    path('login/', views.do_login, name ='login'),
    path('signup/', views.do_signup, name='signup'),
    path('logout/', views.do_logout, name ='logout'),
    # path('comentar/', views.comentario, name ='comentario'),
]
