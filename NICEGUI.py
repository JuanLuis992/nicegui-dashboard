import os
from nicegui import ui

ui.label('Servidor en Railway 🚀')

port = int(os.environ.get('PORT', 8081))

ui.run(host='0.0.0.0', port=port)