# Generated by Django 2.2.2 on 2019-11-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safemode', '0002_auto_20191118_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='cover',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
