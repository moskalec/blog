# Generated by Django 2.0.6 on 2018-07-02 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0003_auto_20180625_0803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['comments'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-articles'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]