from django.contrib import admin
from Gjob.models import GovJobPost, BookPost1 , BookPost2 , BookPost3

# Register your models here.
# admin.site.register(GovJobPost)

admin.site.register(BookPost1)
admin.site.register(BookPost2)
admin.site.register(BookPost3)

@admin.register(GovJobPost)
class GovJobPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyinject.js',)

