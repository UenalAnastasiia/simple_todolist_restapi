# Generated by Django 4.0.6 on 2024-02-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
