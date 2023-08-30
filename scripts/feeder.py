#pylint: disable=all
import csv
from donacion.models import principal,animal,salud,humanitaria,educacion

def feed(dato1,dato2):
    dato1.objects.all().delete()    
    with open(f'data/{dato2}', encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')        
        for item in csv_dict_reader:
            categoria = principal.objects.get(pk=item['categoria'])
           #print("tipo vehiculo", item)
            variable = dato1(categoria=categoria,
                                    first_name = item['first_name'],
                                    last_name = item['last_name'],
                                    valor_donado = item['valor_donado'],
                                    fecha_donacion = item['fecha_donacion'],)
            
            variable.save() 
            print(f'{dato2} creado: {variable}')          

def run():
    # feed(salud,'cruz_roja_en_accion.csv')
    # feed(humanitaria,'recoleccion_de_alimentos.csv')
    # feed(educacion,'educando_a_lo_lejos.csv')
    feed()
    
