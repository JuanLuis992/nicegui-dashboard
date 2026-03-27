import os
from nicegui import ui

# 1. Configuración de puerto para la nube
PORT = int(os.environ.get('PORT', 8081))

# --- PÁGINA DE TABLA ---
@ui.page('/')
def table_page():
    ui.label('Ciudades del Mundo').classes('text-2xl mb-4')
    
    # Definimos las filas
    rows = [
        {'name': 'New York', 'lat': 40.7119, 'lon': -74.0027},
        {'name': 'London', 'lat': 51.5074, 'lon': -0.1278},
        {'name': 'Tokyo', 'lat': 35.6863, 'lon': 139.7722},
    ]
    
    # Creamos la tabla
    ui.table(rows=rows).props('flat bordered') \
        .on('row-click', lambda e: ui.navigate.to(f'/map/{e.args["row"]["lat"]}/{e.args["row"]["lon"]}'))

# --- PÁGINA DE MAPA ---
@ui.page('/map/{lat}/{lon}')
def map_page(lat: float, lon: float):
    ui.label(f'Ubicación: {lat}, {lon}').classes('text-xl mb-2')
    
    # Es vital dar altura (h-96) al mapa para que no salga invisible
    ui.leaflet(center=(lat, lon), zoom=10).classes('h-96 w-full')
    
    ui.link('Volver a la tabla', '/').classes('mt-4 block')

# 2. Lanzamiento (Sin pasar 'root' ni nada parecido)
ui.run(host='0.0.0.0', port=PORT, reload=False, title='Mi Dashboard')