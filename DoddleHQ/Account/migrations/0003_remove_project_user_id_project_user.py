# Generated by Django 4.1.2 on 2023-03-30 09:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_card_checklist_project_project_list_list_table_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user_id',
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
