# Generated by Django 5.1.6 on 2025-02-22 10:09

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_doorlog_mode_alter_doorlog_direction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_logs', to='dashboard.pet')),
            ],
        ),
    ]
