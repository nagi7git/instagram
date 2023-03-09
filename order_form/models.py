from django.db import models


class Product(models.Model):
    order = models.CharField('Заказы', max_length=500)
    price = models.IntegerField('Цена')
    
    def __str__(self):
        return self.order
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Size(models.Model):
    size = models.CharField('Размер', max_length=20)

    def __str__(self):
        return self.size
    
    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'



GENDER_CHOICES = (
    ('MAN', 'Man'),
    ('WOMAN', 'Woman'),
    ('BI', 'Bi'),
    ('OTHER', 'Other')
)


class Order(models.Model):
    order = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Заказы')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='Размер')
    nick_instagram = models.CharField('Ник в инстаграмме', max_length=50)
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='OTHER')
    phone_number = models.IntegerField('Номер телефона ')
    phone_number2 = models.IntegerField('Второй номер телефона ')
    payment_receipt = models.ImageField('Квитанция об оплате', upload_to='image/', blank=True, null=True, )
    delivery_address = models.CharField('Адрес доставки', max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField('Дата заказа', auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'