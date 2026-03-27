import os
from nicegui import ui

# 1. Agregado: Leer el puerto dinámico de la nube
PORT = int(os.environ.get('PORT', 8081))

def root():
    ui.sub_pages({
        '/': table_page,
        '/map/{lat}/{lon}': map_page,
    }).classes('w-full')

def table_page():
    ui.table(rows=[
        {'name': 'New York', 'lat': 40.7119, 'lon': -74.0027},
        {'name': 'London', 'lat': 51.5074, 'lon': -0.1278},
        {'name': 'Tokyo', 'lat': 35.6863, 'lon': 139.7722},
    ]).props('flat bordered') \
        .on('row-click', lambda e: ui.navigate.to(f'/map/{e.args[1]["lat"]}/{e.args[1]["lon"]}'))

def map_page(lat: float, lon: float):
    ui.leaflet(center=(lat, lon), zoom=10)
    ui.link('Back to table', '/')

# 2. Modificado: Pasar host='0.0.0.0', el puerto de la nube y desactivar reload
ui.run(root, host='0.0.0.0', port=PORT, reload=False)