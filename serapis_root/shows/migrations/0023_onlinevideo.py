# Generated by Django 3.0.7 on 2020-07-26 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0022_auto_20200326_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
