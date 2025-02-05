from django.db import models
from slugify import slugify

class User(models.Model):
    """
    Модель для хранения информации о пользователях (поставщиках и переработчиках).
    """

    ROLE_CHOICES = [
        ('supplier', 'Поставщик'),
        ('recycler', 'Переработчик'),
    ]

    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    password = models.CharField(max_length=16, verbose_name="Пароль")
    email = models.EmailField(max_length=100, verbose_name="Почта")
    company_name = models.CharField(max_length=100, verbose_name="Название компании")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, verbose_name="Роль")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.surname}-{self.name}-{self.id}-user")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.surname} {self.name} ({self.company_name})"
    
    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "Пользователи"
    
class SupplierOrder(models.Model):
    """
    Модель для хранения заявок поставщиков.
    """

    supplier = models.ForeignKey(User, on_delete=models.CASCADE, related_name="supplier_orders", verbose_name="Поставщик")
    volume = models.IntegerField(verbose_name="Объем молока")
    distributed_volume = models.IntegerField(default=0, verbose_name="Распределённый объём")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    fat_percentage = models.FloatField(verbose_name="Процент жира")
    supplier_location = models.CharField(max_length=250, verbose_name="Местонахождение поставщика")
    slug = models.SlugField(unique=True, blank=True, verbose_name="Slug")

    def __str__(self):
        return f"Заявка #{self.id} от {self.supplier.company_name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"#{self.id}-{self.supplier.company_name}-supplier")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Заявка поставщика"
        verbose_name_plural = "Заявки поставщиков"

class RecyclerOrder(models.Model):
    """
    Модель для хранения заявок переработчиков.
    """

    STATUS_CHOICES = [
        ("active", "Активна"),
        ("completed", "Завершена")
    ]

    suppliers = models.ManyToManyField(SupplierOrder, related_name="recycler_orders", verbose_name="Заявки поставщиков")
    recycler = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recycler_orders", verbose_name="Переработчик")
    fat_percentage = models.FloatField(verbose_name="Требуемый процент жирности")
    volume = models.IntegerField(verbose_name="Требуемый объем")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    recycler_location = models.CharField(max_length=100, verbose_name="Местонахождение переработчика")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name="Статус")
    slug = models.SlugField(verbose_name="Slug")
    
    def __str__(self):
        return f"Заявка #{self.id} от {self.recycler.company_name}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"#{self.id}-{self.recycler.company_name}-recycler")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Заявка переработчика"
        verbose_name_plural = "Заявки переработчиков"

