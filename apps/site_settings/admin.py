from django.contrib import admin
from site_settings.models import Setting

class SettingAdmin(admin.ModelAdmin):
    list_display = ['name','label','value','scope','scope_category']
    search_fields = ['name','label']
    list_filter = ['scope_category']
    fieldsets = (
        (None, {'fields': ('value',)}),
    )    
        
    def queryset(self, request):
        qs = super(SettingAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(client_editable=True)
    
admin.site.register(Setting, SettingAdmin)