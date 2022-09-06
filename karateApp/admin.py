from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(items, MyModelAdmin)
admin.site.register(associate_members)
admin.site.register(galleryfolder)
admin.site.register(gallery)
admin.site.register(affiliation)
