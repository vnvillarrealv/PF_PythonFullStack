#pylint: disable=all
import json
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from .models import CAMPANIA, DONACION, SOLICITUDES_CAMPANIAS, CATEGORIAS
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
#paypal
from django.urls import reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
import json


#PAGINA DE INICIO
def index(request):
    campania_mayor_recaudacion = CAMPANIA.objects.order_by('-monto_recaudado').first()#el - es para que sea descendente
    return render(request,'index.html',{'campaña':campania_mayor_recaudacion})

#CATALOGO DE CAMPAÑAS
def catalogo_camp(request):
    filtro_categoria = request.GET.get('categoria_CAMP_filtro')
    fecha_actual = datetime.now().date()

    if filtro_categoria:
        categoria_todo = CAMPANIA.objects.filter(categoria__categoria=filtro_categoria).order_by('-id')
    else:
        categoria_todo = CAMPANIA.objects.all().order_by('-id')

    return render(request, 'catalogo_camp.html',{'lista_campañas': categoria_todo,'fecha_actual':fecha_actual})

#PERFIL DE CADA CAMPAÑA
def perfil_detallado_camp(request, camp_id):
    camp = get_object_or_404(CAMPANIA, pk=camp_id)
    fecha_actual = datetime.now().date()
    return render(request, 'perfil_detallado_camp.html', {'campaña': camp, 'fecha_actual':fecha_actual})

#PARA INICIAR SESION
def do_login(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        user = authenticate(username=payload.get('username'), password=payload.get('password'))#authenticate devolverá una instancia del modelo de usuario, se utiliza para verificar si ese usuario esta e los usuaios de la base de datos y asi poder darle ingreso en caso de no encotrar nada devuelve None
        if user is not None:
            login(request, user)
            result = {'login': True, 'msg': 'Sesión iniciada'}#para crear una respuesta HTTP JSON que contiene el diccionario result. Esta respuesta JSON se envía al cliente como resultado de la solicitud.
            return JsonResponse(result)#le damos respuesta al usuario. esto seria com evniar un status 200 es deci,r que todo esta ok
        else:
            result = {'login': False, 'msg': 'Usuario o contraseña incorrectas'}
            return JsonResponse(result, status=401)#un erro de tipo 400 indica que hay un error por parte dEL usuario, en este caso, credencales incorrectas
    return render(request, 'signin.html')

#PARA REGISTRARSE COMO USUARIO NUEVO
def do_signup(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        if User.objects.filter(email=payload.get('email')).exists():
            result = {'success': False, 'msg': 'Ya existe un usuario registrado con el email ' + payload.get('email') }
            return JsonResponse(result, status=400)
        
        new_user = User(
                    username=payload.get('email'),
                    password=make_password(payload.get('password')),
                    is_superuser=False,
                    first_name=payload.get('nombre'),
                    last_name=payload.get('apellido'),
                    email=payload.get('email'),
                    is_staff=False,
                    is_active=True,
                    date_joined=datetime.now()
                )
        new_user.save()        
        result = {'success': True, 'msg': 'Usuario registrado'}
        return JsonResponse(result)
    
    return render(request, 'signup.html')

#CIERRE DE SESION
def do_logout(request):
    logout(request)
    return redirect('index')


#FORMULARIO PARA DONAR
@login_required(login_url='/login')
def checkout(request,camp3_id):
    camp = get_object_or_404(CAMPANIA, pk=camp3_id)
    fecha_actual = datetime.now().date()
    fecha_formateada = fecha_actual.isoformat()#formatear aqui, por alguna razon no me enviaba la fecha como año-mes-dia pero en los otros views si.
    return render(request, 'checkout.html',{'fecha_actual':fecha_formateada, 'campaña':camp})

#VENTANA VERIFICAICION DE DONACION
@login_required(login_url='/login')
def ventana_aporte(request,camp2_id):
    camp = get_object_or_404(CAMPANIA, pk=camp2_id)
    valor_donado = request.POST.get('valor_donado')

    detalles_dict = {
        'campaña':camp,
        'valor_donado':request.POST.get('valor_donado')
        
    }

    form_dict = {
        'nombre_campania' : camp.nombre_campania,
        'usuario' : request.POST.get('usuario'),
        'nombre' : request.POST.get('nombre'),
        'apellido' : request.POST.get('apellido'),
        'valor_donado' : request.POST.get('valor_donado'),
        'fecha_donativo' : request.POST.get('fecha_donativo'),
        'comentario' : request.POST.get('comentario')
    }

    form_dict_json = json.dumps(form_dict)#se pasa a json para poder pasarlo en la url de return
    host = request.get_host()
    return_url = 'http://{}{}?form_dict={}'.format(host, reverse('payment_done'), form_dict_json)

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': valor_donado,
        'item_name': camp,
        'invoice': camp2_id,
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url': return_url,
        'cancel_return': 'http://{}{}'.format(host,reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'ventana_aporte.html',{'form':form,'donacion': detalles_dict})

#PLANTILLA SI PAGO EXITOSO
@csrf_exempt
def payment_done(request):

    form_dict_json = request.GET.get('form_dict')
    form_dict = json.loads(form_dict_json)
    nombre_campania = form_dict.get('nombre_campania')
    camp = CAMPANIA.objects.get(nombre_campania=nombre_campania)

    nueva_donacion = DONACION(
        nombre_campania = camp,
        usuario = form_dict.get('usuario'),
        valor_donado = form_dict.get('valor_donado'),
        fecha_donativo = form_dict.get('fecha_donativo'),
        comentario = form_dict.get('comentario')
    )
    nueva_donacion.save()
    return render(request, 'payment-success.html')

#PLANTILLA SI PAGO CANCELADO O FALLIDO
@csrf_exempt
def payment_canceled(request):
	return render(request, 'payment-fail.html')


def do_aboutus(request):
    return render(request, 'nosotros.html')

def do_contact(request):
    return render(request, 'contacto.html')

def campania_registrada(request):
    filtro_categoria = request.POST.get('categoria_CAMP_filtro')

    categoria = CATEGORIAS.objects.get(categoria = filtro_categoria)
    categoria2 = CATEGORIAS.objects.get(pk = categoria.id)

    nueva_campania = SOLICITUDES_CAMPANIAS(
        categoria = categoria2,
        nombre = request.POST.get('nombre'),
        apellido = request.POST.get('apellido'),
        email = request.POST.get('email'),
        nombre_campania = request.POST.get('campania'),
        descripcion = request.POST.get('descripcion'),
        beneficiario = request.POST.get('beneficiario'),
        monto_a_recaudar= request.POST.get('monto_a_recaudar'),
        direccion = request.POST.get('direccion'),
        telefono = request.POST.get('telefono')
    )
    nueva_campania.save()

    return render(request, 'campania_registrada.html')

@login_required(login_url='/login')
def solicitud_campania(request):
    return render(request, 'solicitud_campania.html')


def consejos(request):
    return render(request, 'consejos.html')

def logros(request):
    categoria_todo = CAMPANIA.objects.all().order_by('-id')
    return render(request, 'logros.html',{'lista_campañas': categoria_todo})

def do_terms(request):
    return render(request, 'terms.html')
