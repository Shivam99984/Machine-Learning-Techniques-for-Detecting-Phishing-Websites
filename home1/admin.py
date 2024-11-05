from django.contrib import admin

from  home1.models import User_wedsite
class User_wedsiteAdmin(admin.ModelAdmin):
   list_display = ('email', 'password')

admin.site.register(User_wedsite, User_wedsiteAdmin)

# Register your models here.
