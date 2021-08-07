# Generated by Django 2.2.3 on 2019-08-03 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('r_desc', models.CharField(max_length=5000)),
                ('discountCode', models.IntegerField(default=None)),
                ('r_image', models.ImageField(default='myapp/restaurant/default.png', upload_to='myapp/restaurant')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishName', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('m_desc', models.CharField(max_length=5000)),
                ('m_image', models.ImageField(default='myapp/menu/default.png', upload_to='myapp/menu')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offerCode', models.IntegerField(default=None)),
                ('offer_tnc', models.CharField(max_length=6000)),
                ('offerPer', models.IntegerField(default=0)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Menu')),
            ],
        ),
    ]
