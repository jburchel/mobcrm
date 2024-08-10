from django.contrib import admin
from .models import Contact, Church, Prospect, NonProspectInd

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'first_name', 'last_name', 'email')
    list_filter = ('type',)

class ChurchAdmin(admin.ModelAdmin):
    list_display = ('id', 'church_name', 'denomination', 'congregation_size')

class ProspectAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'home_country')

class NonProspectIndAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Church, ChurchAdmin)
admin.site.register(Prospect, ProspectAdmin)
admin.site.register(NonProspectInd, NonProspectIndAdmin)