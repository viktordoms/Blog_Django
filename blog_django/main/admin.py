from django.contrib import admin
from .models import Users


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('id',)


admin.site.register(Users, UserAdmin)
