# Generated by Django 4.0.5 on 2022-07-03 19:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learnm', '0002_listblog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='name_content',
            field=models.TextField(),
        ),
    ]
