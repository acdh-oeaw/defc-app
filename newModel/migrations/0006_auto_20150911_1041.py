# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0005_auto_20150911_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchevent',
            name='project',
        ),
        migrations.AddField(
            model_name='researchevent',
            name='project_id',
            field=models.CharField(help_text='Project unique identifier.', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='researchevent',
            name='project_leader',
            field=models.CharField(help_text='Leader of the research project.', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='researchevent',
            name='project_name',
            field=models.CharField(help_text='Name of project.', max_length=100, null=True, blank=True),
        ),
        migrations.RemoveField(
            model_name='interpretation',
            name='production_type',
        ),
        migrations.AddField(
            model_name='interpretation',
            name='production_type',
            field=models.ManyToManyField(help_text='Types of production for which evidence was found.', to='newModel.DC_interpretation_productiontype', blank=True),
        ),
        migrations.RemoveField(
            model_name='interpretation',
            name='subsistence_type',
        ),
        migrations.AddField(
            model_name='interpretation',
            name='subsistence_type',
            field=models.ManyToManyField(help_text='Types of livelihood for which evidence was found.', to='newModel.DC_interpretation_subsistencetype', blank=True),
        ),
        migrations.RemoveField(
            model_name='researchevent',
            name='institution',
        ),
        migrations.AddField(
            model_name='researchevent',
            name='institution',
            field=models.ManyToManyField(help_text='Organisation that carried out a research project at the site.', to='newModel.DC_researchevent_institution', blank=True),
        ),
        migrations.RemoveField(
            model_name='researchevent',
            name='research_type',
        ),
        migrations.AddField(
            model_name='researchevent',
            name='research_type',
            field=models.ManyToManyField(help_text='Methods used for researching the site.', to='newModel.DC_researchevent_researchtype', blank=True),
        ),
        migrations.RemoveField(
            model_name='researchevent',
            name='special_analysis',
        ),
        migrations.AddField(
            model_name='researchevent',
            name='special_analysis',
            field=models.ManyToManyField(help_text='Analyses other than excavation that were carried out to research the site.', to='newModel.DC_researchevent_special_analysis', blank=True),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
