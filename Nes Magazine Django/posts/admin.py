from django.contrib import admin
from .models import *
# Register your models here.
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Tech, MyModelAdmin)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(HeaderPost, MyModelAdmin)



class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Showbiz, MyModelAdmin)



class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Travel, MyModelAdmin)



class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Sport, MyModelAdmin)


# admin.site.register(Tech)
# admin.site.register(HeaderPost)
# admin.site.register(Showbiz)
# admin.site.register(Travel)
# admin.site.register(Sport)
# admin.site.register(Video)


#   createsuperuser credencials

#   username = e
#   password = e