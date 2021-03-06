# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-23 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorrBkg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bkg_corr', models.TextField()),
                ('bkg_dist_corr', models.TextField()),
            ],
            options={
                'db_table': 'corr_bkg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrBptypeParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bptype', models.CharField(db_column='bpType', max_length=10)),
            ],
            options={
                'db_table': 'corr_bpType_param',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrChrom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chrom', models.CharField(max_length=40)),
                ('size', models.IntegerField()),
            ],
            options={
                'db_table': 'corr_chrom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrChromStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track1_av', models.FloatField()),
                ('track2_av', models.FloatField()),
                ('cc', models.FloatField()),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'corr_chrom_stat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrComplfgParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complfg', models.CharField(db_column='complFg', max_length=20)),
            ],
            options={
                'db_table': 'corr_complFg_param',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrCorrFg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('corr', models.FloatField()),
            ],
            options={
                'db_table': 'corr_corr_fg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrDevstage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devstage', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'corr_devstage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrDistCorr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist', models.IntegerField()),
                ('corr', models.FloatField()),
            ],
            options={
                'db_table': 'corr_dist_corr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrDistOutputParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist_output', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'corr_dist_output_param',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrInputTypeParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'corr_input_type_param',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrKernelTypeParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kernel_type', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'corr_kernel_type_param',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrLab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'corr_lab',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'corr_mark',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'corr_org',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrOutresParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outres', models.CharField(db_column='outRes', max_length=10)),
            ],
            options={
                'db_table': 'corr_outRes_param',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrOutwigParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outwig', models.CharField(db_column='outWig', max_length=20)),
            ],
            options={
                'db_table': 'corr_outWig_param',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_path', models.CharField(max_length=100)),
                ('track_path', models.CharField(max_length=100)),
                ('res_path', models.CharField(max_length=100)),
                ('map', models.CharField(blank=True, max_length=100, null=True)),
                ('pcor_profile', models.CharField(blank=True, max_length=100, null=True)),
                ('wsize', models.IntegerField(db_column='wSize')),
                ('wstep', models.IntegerField(db_column='wStep')),
                ('kernel_type_id', models.IntegerField()),
                ('kernel_sigma', models.IntegerField()),
                ('kernel_shift', models.IntegerField()),
                ('kernel_ns', models.IntegerField(db_column='kernel_NS')),
                ('compl_fg_id', models.IntegerField(db_column='compl_Fg_id')),
                ('statistics', models.CharField(max_length=100)),
                ('params_file', models.CharField(blank=True, max_length=100, null=True)),
                ('aliases', models.CharField(max_length=100)),
                ('log', models.CharField(max_length=100)),
                ('chrom', models.CharField(max_length=100)),
                ('na', models.IntegerField(blank=True, null=True)),
                ('input_type_id', models.IntegerField()),
                ('strand', models.IntegerField()),
                ('scale_factor', models.FloatField()),
                ('step', models.IntegerField()),
                ('scale_id', models.IntegerField(blank=True, null=True)),
                ('laauto', models.IntegerField(db_column='lAauto')),
                ('bptype_id', models.IntegerField(blank=True, db_column='bpType_id', null=True)),
                ('flanksize', models.IntegerField(db_column='flankSize')),
                ('noiselevel', models.FloatField(db_column='noiseLevel')),
                ('maxna', models.IntegerField(db_column='maxNA')),
                ('maxzero', models.IntegerField(db_column='maxZero')),
                ('nshuffle', models.IntegerField(db_column='nShuffle')),
                ('maxshuffle', models.IntegerField(db_column='maxShuffle')),
                ('mapiv', models.CharField(blank=True, db_column='mapIv', max_length=50, null=True)),
                ('threshold', models.IntegerField()),
                ('corronly', models.IntegerField(db_column='corrOnly')),
                ('outres_id', models.IntegerField(blank=True, db_column='outRes_id', null=True)),
                ('outdistr', models.IntegerField(db_column='outDistr')),
                ('dist_output_id', models.IntegerField(blank=True, null=True)),
                ('outthreshold', models.FloatField(db_column='outThreshold')),
                ('outspectr', models.IntegerField(db_column='outSpectr')),
                ('outchrom', models.IntegerField(db_column='outChrom')),
            ],
            options={
                'db_table': 'corr_param',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog_run_id', models.CharField(max_length=20)),
                ('nfgr', models.IntegerField(db_column='nFgr')),
                ('bkg_av', models.FloatField(db_column='Bkg_av')),
                ('fg_av', models.FloatField(db_column='Fg_av')),
                ('bkg_sd', models.FloatField(db_column='Bkg_sd')),
                ('fg_sd', models.FloatField(db_column='Fg_sd')),
                ('tot_cor', models.FloatField()),
                ('mann_z', models.FloatField()),
                ('p_value', models.FloatField()),
                ('pc', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'corr_run',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'corr_sample',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrScaleParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'corr_scale_param',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrTissue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tissue', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'corr_tissue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CorrTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'corr_track',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('user_id', models.IntegerField()),
                ('content_type_id', models.IntegerField(blank=True, null=True)),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
    ]
