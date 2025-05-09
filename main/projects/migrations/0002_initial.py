# Generated by Django 5.1.7 on 2025-03-17 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('skills', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='developer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='user.developer'),
        ),
        migrations.AddField(
            model_name='project',
            name='ngo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='user.ngo'),
        ),
        migrations.AddField(
            model_name='application',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='projects.project'),
        ),
        migrations.AddField(
            model_name='projectskill',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
        migrations.AddField(
            model_name='projectskill',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.skill'),
        ),
        migrations.AddField(
            model_name='project',
            name='skills_required',
            field=models.ManyToManyField(through='projects.ProjectSkill', to='skills.skill'),
        ),
        migrations.AlterUniqueTogether(
            name='projectskill',
            unique_together={('project', 'skill')},
        ),
    ]
