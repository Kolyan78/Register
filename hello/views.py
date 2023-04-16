from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.template.response import TemplateResponse
import datetime
from random import randint
from .models import Master, Register, Client, StatusPay
from faker import Faker
fake = Faker(locale="ru_RU")


def index(request):
    date = datetime.date.today()
    m = ["", "Января", "Февраля", "Марта", "Апреля", "Мая", "Июня",
         "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]
    w = ["", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    d = f"{w[date.weekday() + 1]}, {date.day} {m[date.month]} {date.year} года"
    # num = randint(1, 15000)
    # Master.objects.create(surname=fake.last_name_male(),
    #                       name=fake.first_name_male(),
    #                       email=fake.email(),
    #                       phone=fake.phone_number())
    masters = Master.objects.all()
    register = Register.objects.all()
    clients = Client.objects.all()
    statuspay = StatusPay.objects.all()
    num = Register.objects.count()
    mas = Master.objects.count()
    cli = Client.objects.count()
    data = {"d": d, "num": num, "mas": mas, "cli": cli, "w": w,
            "masters": masters, "register": register, "clients": clients, "status_pay": statuspay}
    return render(request, "index.html", data)


def create(request):
    if request.method == "POST":
        master = Master()
        master.surname = request.POST.get("surname")
        master.name = request.POST.get("name")
        master.email = request.POST.get("email")
        master.phone = request.POST.get("phone")
        master.save()
    return HttpResponseRedirect("/")


def edit(request, id):
    try:
        master = Master.objects.get(id=id)
        if request.method == "POST":
            master.surname = request.POST.get("surname")
            master.name = request.POST.get("name")
            master.email = request.POST.get("email")
            master.phone = request.POST.get("phone")
            master.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"master": master})
    except Master.DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")


def delete(request, id):
    try:
        master = Master.objects.get(id=id)
        master.delete()
        return HttpResponseRedirect("/")
    except Master.DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
