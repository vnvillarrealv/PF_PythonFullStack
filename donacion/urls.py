from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),#muestra la pantalla principal
    path('catalogo_camp/',views.catalogo_camp, name='catalogo_camp'),#muesra el catalogo de las campañas
    path('perfil_detallado_camp/<int:camp_id>/',views.perfil_detallado_camp, name='perfil_detallado_camp'),#muestra la info de cada campaña
    path('ventana_aporte/<int:camp2_id>/', views.ventana_aporte, name ='ventana_aporte'),
    path('checkout/<int:camp3_id>/', views.checkout, name ='checkout'),
    path('login/', views.do_login, name ='login'),
    path('signup/', views.do_signup, name='signup'),
    path('logout/', views.do_logout, name ='logout'),    
    # path('do_donacion_paypal/<int:camp2_id>/', views.do_donacion_paypal, name ='do_donacion_paypal'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('aboutus/', views.do_aboutus, name ='aboutus'),
    path('contact/', views.do_contact, name ='contact'),
    path('terms/', views.do_terms, name ='terms'),    
]
