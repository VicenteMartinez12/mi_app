# mi_app/__init__.py

# Importar el modelo Producto si deseas que sea accesible desde `mi_app`
from .models import Producto  

# Asegurar que Django reconozca correctamente la aplicación
default_app_config = "mi_app.apps.MiAppConfig"
