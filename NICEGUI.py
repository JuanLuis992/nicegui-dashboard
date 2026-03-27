import os
from nicegui import ui

# 1. Configuración de puerto dinámico para Render
PORT = int(os.environ.get('PORT', 8081))

# Tu lógica original
slider = ui.slider(min=0, max=100, value=50)
ui.label().bind_text_from(slider, 'value').classes('text-2xl mt-4')

# 2. Configuración de ejecución CRÍTICA para la nube
# host='0.0.0.0' permite que el servidor sea visible en internet
# port=PORT usa el puerto que Render le asigne
ui.run(host='0.0.0.0', port=PORT, title='Mi App con Slider', reload=False)