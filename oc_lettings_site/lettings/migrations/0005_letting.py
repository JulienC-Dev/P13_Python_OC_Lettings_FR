# Generated by Django 3.0 on 2022-05-12 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0004_auto_20220512_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='lettings.Address')),
            ],

        ),
        migrations.RunSQL("""
                INSERT INTO lettings_letting (
                    id,
                    title,
                    address_id
                )
                SELECT
                    id,
                    title,
                    address_id
                FROM
                    oc_lettings_site_letting;
            """, reverse_sql="""
                INSERT INTO oc_lettings_site_letting (
                    id,
                    title,
                    address_id
                )
                SELECT
                    id,
                    title,
                    address_id
                FROM
                    lettings_letting;
            """)
    ]
