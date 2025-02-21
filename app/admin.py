from django.contrib import admin
from app.models import Car, Brand
# Register your models here for the admin view.


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') #O que vai ser mostrado para o admin
    search_fields = ('model',) #La na tela de admins, vou poder fazer uma pesquisa pelo modelo do carro 
    
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
