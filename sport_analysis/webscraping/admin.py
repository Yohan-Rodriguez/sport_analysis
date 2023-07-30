from django.contrib import admin
from .models import League 
from .models import Links_leagues

# Administrar el modelo desde el panel de administración que otorga django
admin.site.register(League)
admin.site.register(Links_leagues)
