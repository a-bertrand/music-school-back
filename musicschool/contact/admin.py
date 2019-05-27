from django.contrib import admin
from musicschool.contact.models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'email'
    )


admin.site.register(Contact, ContactAdmin)