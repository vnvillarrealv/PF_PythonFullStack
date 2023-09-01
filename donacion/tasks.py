from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from .models import CAMPANIA


def actualizar_status():
    now = datetime.now().date()
    print("fecha tasks:",now)
    campanias_a_cerrar = CAMPANIA.objects.filter(fecha_cierre__lte=now, status=True)
    for campania in campanias_a_cerrar:
        campania.status = False
        campania.save()

    print("Tarea en segundo plano: Verificación y actualización de status de campañas completada.")

def start_task():
    scheduler = BackgroundScheduler (daemon=True)
    scheduler.add_job(actualizar_status,'cron', hour=00,minute=00)
    scheduler.start()

