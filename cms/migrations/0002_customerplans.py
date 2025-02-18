# Generated by Django 5.0.6 on 2024-05-08 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.customer')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.plan')),
            ],
        ),
    ]
