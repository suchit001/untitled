# Generated by Django 2.0.6 on 2018-07-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_remove_announcement_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenseapplication',
            name='amount',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
