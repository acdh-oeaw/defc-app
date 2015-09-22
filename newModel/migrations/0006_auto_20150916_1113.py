# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newModel', '0005_auto_20150914_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='comment',
            field=models.TextField(help_text='Additional information not covered in any other field.', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='site',
            name='comment',
            field=models.TextField(help_text='Additional information on the site not covered in any other field.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='settlement_structure',
            field=models.ManyToManyField(help_text='Layout of settlement.', to='newModel.DC_area_settlementstructure', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='amount',
            field=models.ForeignKey(blank=True, to='newModel.DC_finds_amount', help_text='Amount of finds.', null=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='animal_remains_completeness',
            field=models.ForeignKey(blank=True, to='newModel.DC_finds_animal_remains_completeness', help_text='Condition of the zoological sample / find (complete or part).', null=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='animal_remains_part',
            field=models.ManyToManyField(help_text='Part of the species the sample / find belongs to.', to='newModel.DC_finds_animal_remains_part', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='animal_remains_species',
            field=models.ManyToManyField(help_text='Species the zoological sample / find belongs to.', to='newModel.DC_finds_animal_remains_species', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='botany_species',
            field=models.ManyToManyField(help_text='Species the botanical sample / find belongs to.', to='newModel.DC_finds_botany_species', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='comment',
            field=models.TextField(help_text='Additional information not covered in any other field.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='finds_type',
            field=models.ForeignKey(blank=True, to='newModel.DC_finds_type', help_text='Type of the finds.', null=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='lithics_cores',
            field=models.ManyToManyField(help_text='Type of the cores.', to='newModel.DC_finds_lithics_core', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='lithics_debitage',
            field=models.ManyToManyField(help_text='Which basic form used (for tools).', to='newModel.DC_finds_lithics_debitage', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='lithics_modified_tools',
            field=models.ManyToManyField(help_text='Kind of tool which was made out of the debitage.', to='newModel.DC_finds_lithics_modified_tools', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='lithics_technology',
            field=models.ManyToManyField(help_text='Which technology was used to produce the debitage or tools.', to='newModel.DC_finds_lithics_technology', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='material',
            field=models.ManyToManyField(help_text='Material used for find.', to='newModel.DC_finds_material', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='pottery_decoration',
            field=models.ManyToManyField(help_text='Type of decoration.', to='newModel.DC_finds_pottery_decoration', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='pottery_detail',
            field=models.ManyToManyField(help_text='Pottery type.', to='newModel.DC_finds_pottery_detail', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='pottery_form',
            field=models.ManyToManyField(help_text='Form of pottery.', to='newModel.DC_finds_pottery_form', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='reference',
            field=models.ManyToManyField(help_text='Relevant resources on the finds.', to='newModel.Reference', blank=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='research_event',
            field=models.ForeignKey(blank=True, to='newModel.ResearchEvent', help_text='Related research event.', null=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='small_finds_category',
            field=models.ForeignKey(blank=True, to='newModel.DC_finds_small_finds_category', help_text='Either a tool, jewellery or figurines', null=True),
        ),
        migrations.AlterField(
            model_name='finds',
            name='small_finds_type',
            field=models.ManyToManyField(help_text='Type of small find.', to='newModel.DC_finds_small_finds_type', blank=True),
        ),
        migrations.AlterField(
            model_name='interpretation',
            name='comment',
            field=models.TextField(help_text='Additional information on subsistence and production not covered in any other field.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='interpretation',
            name='reference',
            field=models.ManyToManyField(help_text='Bibliographic and web-based reference(s)to publications and other relevant resources on industry & subsistence of the site/phase of the site.', to='newModel.Reference', blank=True),
        ),
        migrations.AlterField(
            model_name='period',
            name='comment',
            field=models.TextField(help_text='Additional information on the chronology not covered in any other field.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='period',
            name='dating_method',
            field=models.ManyToManyField(help_text='Method used for dating the site.', to='newModel.DC_period_datingmethod', blank=True),
        ),
    ]
