# Generated by Django 4.2.8 on 2024-05-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firmalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firma_adi', models.CharField(max_length=100)),
                ('telefon', models.FloatField()),
                ('Adet', models.PositiveIntegerField()),
                ('sha', models.PositiveIntegerField()),
                ('cinsi_1', models.CharField(max_length=100)),
                ('cinsi_2', models.CharField(max_length=100)),
                ('renk', models.CharField(max_length=50)),
                ('demir_capi', models.FloatField()),
                ('temiz_capi', models.FloatField()),
                ('boy', models.FloatField()),
                ('kilo', models.FloatField()),
                ('kilo_fiyati', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tutar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('durumu', models.TextField()),
                ('not_bilgisi', models.TextField()),
                ('muhasebe_not_bilgisi', models.TextField()),
                ('tarih', models.DateField()),
            ],
        ),
    ]
