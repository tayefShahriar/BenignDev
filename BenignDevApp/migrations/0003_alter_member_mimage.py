# Generated by Django 4.2.4 on 2023-08-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BenignDevApp', '0002_member_mimage_alter_service_sdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mimage',
            field=models.ImageField(blank=True, default='member/default.png', upload_to='member'),
        ),
    ]
