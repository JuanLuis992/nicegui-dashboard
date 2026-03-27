import os
from nicegui import ui
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN DE RENDER ---
# Render asigna un puerto dinámico. Si no existe, usamos el 8081 por defecto.
PORT = int(os.environ.get('PORT', 8081))

def create_chart():
    """Crea un gráfico simple de ejemplo"""
    plt.figure(figsize=(4, 2))
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], color='darkblue', marker='o')
    plt.title('Rendimiento del Sistema')
    plt.tight_layout()
    return plt

@ui.page('/')
def main_page():
    # --- BARRA DE NAVEGACIÓN ---
    with ui.header().classes('items-center justify-between bg-primary'):
        ui.label('NiceGUI Dashboard').classes('text-2xl font-bold')
        with ui.row():
            ui.button('Inicio', on_click=lambda: ui.notify('Ya estás aquí'))
            ui.button('Configuración', icon='settings')

    # --- CUERPO DEL DASHBOARD ---
    with ui.column().classes('w-full p-8'):
        ui.label('Panel de Control en la Nube').classes('text-3xl mb-4')

        # Tarjetas de métricas
        with ui.row().classes('w-full justify-around mb-8'):
            with ui.card().classes('p-4 bg-blue-100'):
                ui.label('Usuarios Activos').classes('text-sm text-gray-500')
                ui.label('1,240').classes('text-2xl font-bold')
            
            with ui.card().classes('p-4 bg-green-100'):
                ui.label('Estado del Servidor').classes('text-sm text-gray-500')
                ui.label('Online').classes('text-2xl font-bold text-green-600')

            with ui.card().classes('p-4 bg-orange-100'):
                ui.label('Alertas').classes('text-sm text-gray-500')
                ui.label('0').classes('text-2xl font-bold')

        # Sección de Gráficos
        with ui.row().classes('w-full items-center justify-center'):
            with ui.card().classes('p-4'):
                ui.label('Estadísticas en Tiempo Real').classes('text-lg mb-2')
                ui.pyplot(create_chart())

        ui.button('Actualizar Datos', on_click=lambda: ui.notify('Datos actualizados!'), icon='refresh')

# --- LANZAMIENTO ---
# Importante: host='0.0.0.0' es CRÍTICO para Render
ui.run(title='Mi Dashboard', host='0.0.0.0', port=PORT, reload=False)