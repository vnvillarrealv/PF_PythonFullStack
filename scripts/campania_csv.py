import csv
from donacion.models import CAMPANIA,CATEGORIAS

def feed_campania():
    CAMPANIA.objects.all().delete()    
    with open('data/2campania_csv1.csv', encoding='UTF-8') as csv_file:
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';')        
        for item in csv_dict_reader:
            categoria = CATEGORIAS.objects.get(pk = item['categoria'])
            print("campaña:", item)
            variable = CAMPANIA(categoria=categoria,
                                    nombre_campania = item['nombre_campania'],
                                    descripcion = item['descripcion'],
                                    beneficiario = item['beneficiario'],
                                    monto_a_recaudar = item['monto_a_recaudar'],
                                    monto_recaudado = item['monto_recaudado'],
                                    fecha_inicio = item['fecha_inicio'],
                                    fecha_cierre = item['fecha_cierre'],
                                    status = item['status'],
                                    imagen = item['imagen']
                                    )
            
            variable.save() 
            print(f'item creado: {variable}')

def run():
    feed_campania()
    
