import datetime as dt
import random
from src.models.event import event
from src.storage.db import init_db, insert_event, fetch_events, update_event, delete_event
from src.ui.main_window import *

def test():
    #inicializo db
    init_db()

    print("=== 1. CREANDO Y GUARDANDO EVENTO ===")
    mi_evento = event(
        title="Reunión de prueba",
        description="Probando el ciclo de vida CRUD con SQLite",
        s_date=dt.date(2026, 10, 15),
        e_date=dt.date(2026, 10, 15),
        s_time=dt.time(10, 0),
        e_time=dt.time(11, 30),
        category_id=1
    )
    
    insert_event(mi_evento)
    print(f"Evento guardado con ID asignado: {mi_evento.id}")

    print("\n=== 2. LEYENDO EVENTOS DE LA BASE DE DATOS ===")
    eventos = fetch_events()
    for e in eventos:
        print(f"ID: {e.id} | Título: {e.title} | Fecha: {e.s_date} | Hora: {e.s_time}")

    print("\n=== 3. ACTUALIZANDO EVENTO ===")
    mi_evento.title = "Reunión de prueba (ACTUALIZADA)"
    update_event(mi_evento)
    
    eventos_actualizados = fetch_events()
    print(f"Título tras update: {eventos_actualizados[0].title}")

    print("\n=== 4. PROBANDO VALIDACIÓN (MODELO) ===")
    try:
        evento_invalido = event(
            title="",  # Título vacío para forzar el error
            description="Debería fallar",
            s_date=dt.date(2026, 10, 15),
            e_date=dt.date(2026, 10, 15),
            s_time=dt.time(12, 0),
            e_time=dt.time(10, 0)  # Fin antes que inicio
        )
    except ValueError as err:
        print(f"Validación funcionando correctamente. Errores capturados:\n{err}")

    print("\n=== 5. ELIMINANDO EVENTO ===")
    delete_event(mi_evento.id)
    eventos_finales = fetch_events()
    print(f"Cantidad de eventos en la BD tras borrar: {len(eventos_finales)}")

def seed_test_events():
    """Genera eventos aleatorios para pruebas en la base de datos."""
    init_db()  # Aseguramos que la tabla exista antes de insertar
    
    today = dt.date.today()
    sample_titles = ["Reunión de trabajo", "Cita médica", "Gimnasio", "Proyecto Python", "Cumpleaños", "Comprar víveres"]
    categories = [1, 2, 3]

    for i in range(10):
        days_offset = random.randint(-15, 15)
        event_date = today + dt.timedelta(days=days_offset)
        
        title = random.choice(sample_titles)
        description = f"Descripción de prueba para {title}"
        s_time = dt.time(random.randint(8, 18), 0)
        e_time = dt.time(s_time.hour + 1, 0)
        cat_id = random.choice(categories)

        # Crear la instancia del evento
        nuevo_evento = event(
            title=title,
            description=description,
            s_date=event_date,
            e_date=event_date,
            s_time=s_time,
            e_time=e_time,
            category_id=cat_id
        )
        
        # Guardarlo en SQLite
        insert_event(nuevo_evento)

    print("¡Eventos de prueba insertados con éxito!")

if __name__ == "__main__":
    # 1. Poblamos la base de datos con eventos aleatorios
    seed_test_events()

    # 2. Iniciamos la aplicación PySide6
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()