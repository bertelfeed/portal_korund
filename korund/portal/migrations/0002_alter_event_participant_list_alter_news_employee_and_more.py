# Generated by Django 5.0.6 on 2024-06-17 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='participant_list',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.employee'),
        ),
        migrations.AlterField(
            model_name='news',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.topic'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='led_projects', to='portal.employee'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='portal.employee'),
        ),
    ]
