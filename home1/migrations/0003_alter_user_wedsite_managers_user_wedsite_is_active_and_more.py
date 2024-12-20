# Generated by Django 5.1.1 on 2024-10-16 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0002_alter_user_wedsite_managers_user_wedsite_last_login_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user_wedsite',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='user_wedsite',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user_wedsite',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_wedsite',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_wedsite',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
