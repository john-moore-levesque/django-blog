# Generated by Django 3.0.7 on 2020-07-06 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200626_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
