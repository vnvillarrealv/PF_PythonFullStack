#pylint: disable=all
import json
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from .models import categorias, campania, donacion, Comentarios
from django.contrib.auth.hashers import make_password 
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

# def catalogo_camp(request):
#     categoria_todo = categorias.objects.all()
#     return render(request, 'catalogo_camp.html',{'lista_categoria': categoria_todo})


# def catalogo_camp(request):
#     filtro_categoria = request.GET.get('categoria_CAMP_filtro') #
#     print("filtro seleccionado",filtro_categoria)
#     if filtro_categoria:
#         categoria_todo = campania.objects.filter(categoria__categoria=filtro_categoria).order_by('-id')
#         print("categoria:",categoria_todo)
#     else:
#         categoria_todo = campania.objects.all().order_by('-id')
#     return render(request, 'catalogo_camp.html',{'lista_categoria': categoria_todo})

def catalogo_camp(request):
    filtro_categoria = request.GET.get('categoria_CAMP_filtro') #
    print("filtro seleccionado",filtro_categoria)
    fecha_actual = datetime.now().date()
    if filtro_categoria:
        categoria_todo = campania.objects.filter(categoria__categoria=filtro_categoria).order_by('-id')
        print("categoria:",categoria_todo)
    else:
        categoria_todo = campania.objects.all().order_by('-id')
    return render(request, 'catalogo_camp.html',{'lista_campañas': categoria_todo,'fecha_actual':fecha_actual})

# def perfil_detallado_camp(request):
#     return render(request, 'perfil_detallado_camp.html')

def perfil_detallado_camp(request, camp_id):
    camp = get_object_or_404(campania, pk=camp_id)
    #camp = get_object_or_404(donacion, pk=camp_id)
    fecha_actual = datetime.now().date()
    print("fecha actual",fecha_actual)
    return render(request, 'perfil_detallado_camp.html', {'campaña': camp, 'fecha_actual':fecha_actual})

@login_required(login_url='/login')
def ventana_aporte(request):
    return render(request, 'ventana_aporte.html')

def do_login(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        user = authenticate(username=payload.get('username'), password=payload.get('password'))#authenticate devolverá una instancia del modelo de usuario, se utiliza para verificar si ese usuario esta e los usuaios de la base de datos y asi poder darle ingreso en caso de noencotrar nada devuelve None
        if user is not None:
            login(request, user)
            result = {'login': True, 'msg': 'Sesión iniciada'}#para crear una respuesta HTTP JSON que contiene el diccionario result. Esta respuesta JSON se envía al cliente como resultado de la solicitud.
            return JsonResponse(result)#le damos respuesta al usuario. esto seria com evniar un status 200 es deci,r que todo esta ok
        else:
            result = {'login': False, 'msg': 'Usuario o contraseña incorrectas'}
            return JsonResponse(result, status=401)#un erro de tipo 400 indica que hay un error por parte dle usuario, en este caso, credencales incorrectas
    return render(request, 'signin.html')

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

def do_logout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='/login')
def comentario(request):
    return render(request, 'comentar.html')

