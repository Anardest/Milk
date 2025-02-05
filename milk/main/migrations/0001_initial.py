# Generated by Django 4.2.18 on 2025-02-05 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('password', models.CharField(max_length=16, verbose_name='Пароль')),
                ('email', models.EmailField(max_length=100, verbose_name='Почта')),
                ('company_name', models.CharField(max_length=100, verbose_name='Название компании')),
                ('role', models.CharField(choices=[('supplier', 'Поставщик'), ('recycler', 'Переработчик')], max_length=10, verbose_name='Роль')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='SupplierOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField(verbose_name='Объем молока')),
                ('distributed_volume', models.IntegerField(default=0, verbose_name='Распределённый объём')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('fat_percentage', models.FloatField(verbose_name='Процент жира')),
                ('supplier_location', models.CharField(max_length=250, verbose_name='Местонахождение поставщика')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Slug')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_orders', to='main.user', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Заявка поставщика',
                'verbose_name_plural': 'Заявки поставщиков',
            },
        ),
        migrations.CreateModel(
            name='RecyclerOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fat_percentage', models.FloatField(verbose_name='Требуемый процент жирности')),
                ('volume', models.IntegerField(verbose_name='Требуемый объем')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('recycler_location', models.CharField(max_length=100, verbose_name='Местонахождение переработчика')),
                ('status', models.CharField(choices=[('active', 'Активна'), ('completed', 'Завершена')], default='active', max_length=10, verbose_name='Статус')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('recycler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recycler_orders', to='main.user', verbose_name='Переработчик')),
                ('suppliers', models.ManyToManyField(related_name='recycler_orders', to='main.supplierorder', verbose_name='Заявки поставщиков')),
            ],
            options={
                'verbose_name': 'Заявка переработчика',
                'verbose_name_plural': 'Заявки переработчиков',
            },
        ),
    ]
