# Generated by Django 5.1.2 on 2024-10-31 18:46

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_uploadjsoncar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalCar',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('cars', models.CharField(help_text='Give me religions of cars', max_length=100)),
                ('speed', models.IntegerField(verbose_name='speed')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mileage', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('image_car', models.TextField(max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical car',
                'verbose_name_plural': 'historical cars',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
