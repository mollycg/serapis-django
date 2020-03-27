# Generated by Django 3.0.3 on 2020-03-25 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0019_auto_20200325_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_category',
            field=models.CharField(choices=[('HS', 'Home page photo'), ('GY', 'Photo gallery')], default='GY', max_length=2),
        ),
    ]