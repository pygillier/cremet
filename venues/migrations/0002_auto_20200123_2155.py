# Generated by Django 3.0.2 on 2020-01-23 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name_plural': 'cities'},
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('venue_type', models.CharField(choices=[('FF', 'Fast food'), ('BI', 'Bistro'), ('GA', 'Gastronomic')], default='BI', max_length=2)),
                ('delivery', models.BooleanField(default=False)),
                ('take_away', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venues', to='venues.City')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]