from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Contact, Church, Prospect, NonProspectInd

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'type')
    list_filter = ('type',)
    search_fields = ('first_name', 'last_name', 'email')

class ChurchAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'get_email', 'get_phone', 'denomination', 'congregation_size')
    search_fields = ('contact_ptr__name', 'denomination', 'contact_ptr__email')

    def get_name(self, obj):
        return obj.contact_ptr.name
    get_name.short_description = 'Name'

    def get_email(self, obj):
        return obj.contact_ptr.email
    get_email.short_description = 'Email'

    def get_phone(self, obj):
        return obj.contact_ptr.phone
    get_phone.short_description = 'Phone'

class ContactTypeFilter(SimpleListFilter):
    title = 'Contact Type'
    parameter_name = 'contact_type'

    def lookups(self, request, model_admin):
        return Contact.TYPE_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contact_ptr__type=self.value())
        return queryset

class ProspectAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'get_email', 'get_phone', 'get_status', 'source')
    search_fields = ('contact_ptr__first_name', 'contact_ptr__last_name', 'contact_ptr__email')

    def get_first_name(self, obj):
        return obj.contact_ptr.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.contact_ptr.last_name
    get_last_name.short_description = 'Last Name'

    def get_email(self, obj):
        return obj.contact_ptr.email
    get_email.short_description = 'Email'

    def get_phone(self, obj):
        return obj.contact_ptr.phone
    get_phone.short_description = 'Phone'

    def get_status(self, obj):
        return obj.status
    get_status.short_description = 'Status'

class NonProspectIndAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'get_email', 'get_phone')
    search_fields = ('contact_ptr__first_name', 'contact_ptr__last_name', 'organization', 'contact_ptr__email')

    def get_first_name(self, obj):
        return obj.contact_ptr.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.contact_ptr.last_name
    get_last_name.short_description = 'Last Name'

    def get_email(self, obj):
        return obj.contact_ptr.email
    get_email.short_description = 'Email'

    def get_phone(self, obj):
        return obj.contact_ptr.phone
    get_phone.short_description = 'Phone'

admin.site.register(Contact, ContactAdmin)
admin.site.register(Church, ChurchAdmin)
admin.site.register(Prospect, ProspectAdmin)
admin.site.register(NonProspectInd, NonProspectIndAdmin)