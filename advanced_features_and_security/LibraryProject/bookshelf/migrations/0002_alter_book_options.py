# Generated by Django 5.2.4 on 2025-07-22 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_view', 'Can View Book'), ('can_create', 'Can Create Book'), ('can_edit', 'Can Edit Book'), ('can_delete', 'Can Delete Book')]},
        ),
    ]
