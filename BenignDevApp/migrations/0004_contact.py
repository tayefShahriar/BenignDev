# Generated by Django 4.2.4 on 2023-08-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BenignDevApp', '0003_alter_member_mimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
