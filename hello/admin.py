from django.contrib import admin
from .models import Master, Client, StatusPay, Register


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    ordering = ('id',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'rest', 'discount')
    ordering = ('id',)


@admin.register(StatusPay)
class StatusPayAdmin(admin.ModelAdmin):
    list_display = ('status', 'sign')


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'client', 'ordername', 'price', 'discount', 'mprice', 'master', 'ready', 'invoice',
                    'statuspay', 'mpay')
    ordering = ('id',)


# Register your models here.
