# Generated by Django 3.0.7 on 2020-09-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imageAlt',
            field=models.CharField(default='A sunrise in Jamestown, RI, USA', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='abstract',
            field=models.TextField(default='A blog post on MooreLevesque.com'),
        ),
    ]
