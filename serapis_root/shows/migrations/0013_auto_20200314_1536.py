# Generated by Django 3.0.3 on 2020-03-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0012_auto_20200310_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='photo',
            field=models.ImageField(upload_to='member_photos'),
        ),
    ]
