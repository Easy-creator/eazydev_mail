from django.contrib import admin
from .models import PassPhrase, Nel_PassPhrase
# Register your models here.
class YourModelAdmin(admin.ModelAdmin):
    readonly_fields = ('keys',)
    list_display = ('date', 'id',)
    search_fields = ('keys',)

admin.site.register(PassPhrase, YourModelAdmin)
admin.site.register(Nel_PassPhrase, YourModelAdmin)