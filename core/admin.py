from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('rut_completo', 'email', 'nombre_completo', 'edad', 'tel',)
    search_fields = ('rut', 'nombre', 'apellido', 'email',)
    list_filter = ('edad',)

    @admin.display(description='rut')
    def rut_completo(self, obj):
        return ('%s-%s' % (obj.rut, obj.dv))

    @admin.display(description='nombre')
    def nombre_completo(self, obj):
        return ('%s %s' % (obj.nombre, obj.apellido))

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id_mascota', 'usuario_duennyo', 'nombre', 'edad', 'tipo', 'raza', 'sexo', 'enfermedad',)
    search_fields = ('id_mascota', 'rut_usuario', 'nombre', 'tipo', 'raza',)
    list_filter = ('tipo', 'raza', 'enfermedad', 'sexo',)
    
    @admin.display(description='dueño')
    def usuario_duennyo(self, obj):
        url = reverse('admin:%s_%s_change' % (obj.rut_usuario._meta.app_label, obj.rut_usuario._meta.model_name), args=[obj.rut_usuario.pk])
        return format_html('<a href="%s">%s</a>' % (url, obj.rut_usuario.rut))

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id_region', 'descripcion',)
    search_fields = ('descripcion',)
    
    def get_ordering(self, request):
        return ['id_region']

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id_ciudad', 'region', 'descripcion',)
    search_fields = ('descripcion',)
    list_filter = ('id_region',)

    def get_ordering(self, request):
        return ['id_ciudad']

    @admin.display(description='region')
    def region(self, obj):
        return ('%s' % (obj.id_region))

class TipoMascotaAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_mascota', 'descripcion')
    search_fields = ('descripcion',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre')
    search_fields = ('id_producto',)

admin.site.register(Usuario, UserAdmin)
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Tipo_mascota, TipoMascotaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Boleta)
admin.site.register(detalle_boleta)
admin.site.register(descuento)