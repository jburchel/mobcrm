from django.contrib import admin
from .models import Contact, Church, Prospect, NonProspectInd

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'type', 'get_specific_type')
    list_filter = ('type',)
    search_fields = ('first_name', 'last_name', 'email')

    def get_specific_type(self, obj):
        try:
            if obj.type == 'church':
                return 'Church'
            elif obj.type == 'prospect':
                return 'Prospect'
            elif obj.type == 'non_prospect_individual':
                return 'Non-Prospect Individual'
            else:
                return 'Unknown'
        except:
            return 'Error'
    get_specific_type.short_description = 'Specific Type'

admin.site.register(Contact, ContactAdmin)

class ChurchAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'denomination', 'congregation_size')
    search_fields = ('first_name', 'last_name', 'email', 'denomination')

class ProspectAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'home_country', 'spouse_recruit')
    search_fields = ('first_name', 'last_name', 'email', 'home_country')

class NonProspectIndAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')

admin.site.register(Church, ChurchAdmin)
admin.site.register(Prospect, ProspectAdmin)
admin.site.register(NonProspectInd, NonProspectIndAdmin)