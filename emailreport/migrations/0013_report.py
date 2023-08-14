# Generated by Django 4.1.1 on 2023-08-04 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emailreport', '0012_remove_serials_date_serials_commissioned_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_report', models.BooleanField(default=False)),
                ('weekly_report', models.BooleanField(default=False)),
                ('date_range_report', models.BooleanField(default=True)),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
