# Generated by Django 4.0 on 2024-10-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadJsonCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars', models.CharField(help_text='Give me religions of cars', max_length=100)),
                ('speed', models.IntegerField(verbose_name='speed')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mileage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image_car', models.ImageField(upload_to='cars')),
            ],
        ),
    ]
