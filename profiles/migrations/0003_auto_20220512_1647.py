# Generated by Django 3.0 on 2022-05-12 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20220512_1633'),
    ]

    operations = [
        migrations.RunSQL("""
            UPDATE `sqlite_sequence`
            SET `seq` = (SELECT MAX(`id`) FROM 'lettings_address')
            WHERE `name` = 'lettings_address';
            """)
    ]
