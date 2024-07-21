from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country_of_origin', 'established_date')
    search_fields = ('name', 'country_of_origin')
    list_filter = ('country_of_origin',)
    
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Additional Information', {
            'fields': ('country_of_origin', 'established_date', 'logo', 'website'),
            'classes': ('collapse',)
        }),
    )

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'is_electric')
    search_fields = ('name', 'car_make__name', 'type')
    list_filter = ('type', 'year', 'is_electric')
    
    fieldsets = (
        (None, {
            'fields': ('car_make', 'name', 'type', 'year')
        }),
        ('Additional Information', {
            'fields': ('description', 'price', 'is_electric', 'photo'),
            'classes': ('collapse',)
        }),
    )

# Registering models with their respective admins
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
