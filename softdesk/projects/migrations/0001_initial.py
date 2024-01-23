# Generated by Django 5.0.1 on 2024-01-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_given_permission', models.DateField(blank=True, null=True)),
                ('role', models.CharField(choices=[('author', 'Author'), ('contributor', 'Contributor')], default='contributor', max_length=20)),
                ('permission', models.CharField(choices=[('can_view', 'Can_View'), ('can_edit', 'Can_Edit'), ('can_delete', 'Can_Delete')], max_length=20)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('project_type', models.CharField(choices=[('back-end', 'Back-end'), ('front-end', 'Front-end'), ('android', 'Android'), ('ios', 'IOS')], max_length=20)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'permissions': [],
            },
        ),
    ]
