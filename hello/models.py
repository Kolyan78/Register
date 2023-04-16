from django.db import models


class Master(models.Model):
    # surname = models.CharField(max_length=20)
    name = models.CharField(max_length=20, verbose_name="Имя мастера")
    email = models.EmailField(verbose_name="E-mail")
    # phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=40, verbose_name="Имя клиента")
    email = models.EmailField(verbose_name="E-mail")
    # phone = models.CharField(max_length=20)
    rest = models.IntegerField(default=0, verbose_name="Остаток депозита")
    discount = models.IntegerField(default=0, verbose_name="Скидка")

    def __str__(self):
        return self.name


class StatusPay(models.Model):
    status = models.CharField(max_length=30, verbose_name="Статус")
    sign = models.CharField(null=True, max_length=1)

    def __str__(self):
        return self.status


class Register(models.Model):
    date = models.DateField(null=True, blank=True, verbose_name="Дата")  # дата заказа
    client = models.ForeignKey(Client, related_name="client",
                               on_delete=models.CASCADE, null=False, default=1,
                               verbose_name="Клиент")  # номер клиента
    ordername = models.CharField(max_length=100, verbose_name="Название заказа")  # название заказа
    price = models.FloatField(default=0, verbose_name="Цена заказа")  # цена заказа
    discount = models.IntegerField(default=0, verbose_name="Скидка")  # скидка
    mprice = models.FloatField(default=0, verbose_name="Цена для мастера")  # цена для мастера
    master = models.ForeignKey(Master, related_name="master",
                               on_delete=models.CASCADE, null=False, default=1,
                               verbose_name="Мастер")  # номер мастера
    ready = models.BooleanField(default=False, verbose_name="Готовность")   # Готовность
    invoice = models.IntegerField(default=0, verbose_name="Номер счета")  # Номер счета
    statuspay = models.ForeignKey(StatusPay, related_name="s_pay",
                                  on_delete=models.CASCADE, null=False, default=1,
                                  verbose_name="Оплата")  # статус оплаты заказа
    mpay = models.ForeignKey(StatusPay, related_name="m_pay",
                             on_delete=models.CASCADE, null=False, default=1,
                             verbose_name="Оплата мастеру")  # статус оплаты мастеру

    def __str__(self):
        return self.ordername

# Create your models here.
