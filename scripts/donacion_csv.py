
import csv
from donacion.models import DONACION,CAMPANIA

def feed_donacion():
    DONACION.objects.all().delete()    
    with open('data/donacion_csv1este.csv', encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')        
        for item in csv_dict_reader:
            # nombre_campania = campania.objects.get(pk=item['nombre_campania'])
            nombre_campania = CAMPANIA.objects.get(nombre_campania=item['nombre_campania'])
           #print("tipo vehiculo", item)
            variable = DONACION(nombre_campania=nombre_campania,
                                    usuario = item['usuario'],
                                    valor_donado = item['valor_donado'],
                                    fecha_donativo = item['fecha_donativo'],
                                    comentario = item['comentario']
                                    )
            
            variable.save() 
            print(f'item creado: {variable}')    

def run():
    feed_donacion()