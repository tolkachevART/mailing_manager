from django.contrib import admin

from mailing.models import Client, Mailing, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment')
    search_fields = ('email', 'name')
    list_filter = ('name',)
@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'periodicity', 'status')
    search_fields = ('created_at',)
    list_filter = ('status', 'created_at')
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body')
    search_fields = ('subject', 'body')
    list_filter = ('subject',)

