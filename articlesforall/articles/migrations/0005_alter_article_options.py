# Generated by Django 4.1 on 2022-09-09 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20220827_1124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-updated', 'created']},
        ),
    ]
