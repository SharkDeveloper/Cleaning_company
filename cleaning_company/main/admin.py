from django.contrib import admin
from .models import Clients,Orders,Services

# Register your models here.
admin.site.register(Clients)
admin.site.register(Orders)
admin.site.register(Services)