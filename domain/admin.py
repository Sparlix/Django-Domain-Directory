from django.contrib import admin
from .models import Domain
from .models import Contact

# Register your models here.
admin.site.register(Domain)
admin.site.register(Contact)