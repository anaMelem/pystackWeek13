# Generated by Django 3.2.25 on 2025-04-10 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorados', '0002_disponibilidadehorarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorados',
            name='token',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
    ]
