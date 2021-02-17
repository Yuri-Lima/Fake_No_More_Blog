# Generated by Django 3.1.5 on 2021-02-17 19:01

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_post_content_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_post',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, help_text='Paste here the link, witch you saw that news ou inspirations?'),
        ),
    ]
