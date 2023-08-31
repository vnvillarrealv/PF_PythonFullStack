#pylint: disable=all
import csv
from donacion.models import CATEGORIAS

def feed_principal():
    CATEGORIAS.objects.all().delete() #primero se le ejecuta el metodo delete a todos los registros del modelo TipoVehiculo (la clase quee asta en models de alquiler )   
    with open('data/1categorias_csv1.csv', encoding='UTF-8') as csv_file:#con context manager abrmos el csv que esta l caroeta data por eso data\nombrearchivo.csv
        csv_dict_reader = csv.DictReader(csv_file, delimiter=';') #aqui creamos un diccionario con los datos del csv que llamamos csv_file con el context mangaer     
        for item in csv_dict_reader:
            elemento = CATEGORIAS(categoria=item['categoria'])
            elemento.save()
            print(f'item creado: {elemento}')

def run():
    feed_principal()

