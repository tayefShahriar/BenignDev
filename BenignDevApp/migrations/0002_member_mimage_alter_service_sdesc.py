# Generated by Django 4.2.4 on 2023-08-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BenignDevApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='mimage',
            field=models.ImageField(default='member/default.png', upload_to='member'),
        ),
        migrations.AlterField(
            model_name='service',
            name='sdesc',
            field=models.TextField(blank=True, null=True),
        ),
    ]