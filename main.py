import datetime as dt
from src.models.event import event
from src.storage.db import init_db, insert_event, fetch_events, update_event, delete_event

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

if __name__ == "__main__":
    test()