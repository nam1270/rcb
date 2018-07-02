from django.contrib import admin
from .models import Resident, Cottage
# Register your models here.
@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','cottage')
@admin.register(Cottage)
class CottageAdmin(admin.ModelAdmin):
    list_display = ('cottage_number','payment_status')