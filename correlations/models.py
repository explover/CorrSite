# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class CorrBkg(models.Model):
    run = models.ForeignKey('CorrRun')
    bkg_corr = models.TextField()
    bkg_dist_corr = models.TextField()

    class Meta:
        managed = False
        db_table = 'corr_bkg'


class CorrBptypeParam(models.Model):
    bptype = models.CharField(db_column='bpType', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'corr_bpType_param'


class CorrChrom(models.Model):
    chrom = models.CharField(max_length=40)
    org_id = models.ForeignKey('CorrOrg')
    size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'corr_chrom'
        unique_together = ['org_id', 'chrom']


class CorrChromStat(models.Model):
    run = models.ForeignKey('CorrRun')
    chrom = models.ForeignKey(CorrChrom)
    track1_av = models.FloatField()
    track2_av = models.FloatField()
    cc = models.FloatField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'corr_chrom_stat'


class CorrComplfgParam(models.Model):
    complfg = models.CharField(db_column='complFg', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'corr_complFg_param'


class CorrCorrFg(models.Model):
    chrom = models.ForeignKey(CorrChrom)
    start = models.IntegerField()
    end = models.IntegerField()
    corr = models.FloatField()
    run = models.ForeignKey('CorrRun')

    class Meta:
        managed = False
        db_table = 'corr_corr_fg'


class CorrDevstage(models.Model):
    devstage = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'corr_devstage'


class CorrDistCorr(models.Model):
    chrom = models.ForeignKey(CorrChrom)
    dist = models.IntegerField()
    corr = models.FloatField()
    run = models.ForeignKey('CorrRun')

    class Meta:
        managed = False
        db_table = 'corr_dist_corr'


class CorrDistOutputParam(models.Model):
    dist_output = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'corr_dist_output_param'


class CorrInputTypeParam(models.Model):
    type = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'corr_input_type_param'


class CorrKernelTypeParam(models.Model):
    kernel_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'corr_kernel_type_param'


class CorrLab(models.Model):
    lab = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'corr_lab'


class CorrMark(models.Model):
    mark = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'corr_mark'


class CorrOrg(models.Model):
    org = models.CharField(max_length=100)
    version = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'corr_org'
        unique_together = ['org', 'version']


class CorrOutresParam(models.Model):
    outres = models.CharField(db_column='outRes', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'corr_outRes_param'


class CorrOutwigParam(models.Model):
    outwig = models.CharField(db_column='outWig', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'corr_outWig_param'


class CorrParam(models.Model):
    prof_path = models.CharField(max_length=100)
    track_path = models.CharField(max_length=100)
    res_path = models.CharField(max_length=100)
    map = models.CharField(max_length=100, blank=True, null=True)
    pcor_profile = models.CharField(max_length=100, blank=True, null=True)
    wsize = models.IntegerField(db_column='wSize')  # Field name made lowercase.
    wstep = models.IntegerField(db_column='wStep')  # Field name made lowercase.
    kernel_type_id = models.IntegerField()
    kernel_sigma = models.IntegerField()
    kernel_shift = models.IntegerField()
    kernel_ns = models.IntegerField(db_column='kernel_NS')  # Field name made lowercase.
    compl_fg_id = models.IntegerField(db_column='compl_Fg_id')  # Field name made lowercase.
    statistics = models.CharField(max_length=100)
    params_file = models.CharField(max_length=100, blank=True, null=True)
    aliases = models.CharField(max_length=100)
    log = models.CharField(max_length=100)
    chrom = models.CharField(max_length=100)
    na = models.IntegerField(blank=True, null=True)
    input_type_id = models.IntegerField()
    strand = models.IntegerField()
    scale_factor = models.FloatField()
    step = models.IntegerField()
    scale_id = models.IntegerField(blank=True, null=True)
    laauto = models.IntegerField(db_column='lAauto')  # Field name made lowercase.
    bptype_id = models.IntegerField(db_column='bpType_id', blank=True, null=True)  # Field name made lowercase.
    flanksize = models.IntegerField(db_column='flankSize')  # Field name made lowercase.
    noiselevel = models.FloatField(db_column='noiseLevel')  # Field name made lowercase.
    maxna = models.IntegerField(db_column='maxNA')  # Field name made lowercase.
    maxzero = models.IntegerField(db_column='maxZero')  # Field name made lowercase.
    nshuffle = models.IntegerField(db_column='nShuffle')  # Field name made lowercase.
    maxshuffle = models.IntegerField(db_column='maxShuffle')  # Field name made lowercase.
    mapiv = models.CharField(db_column='mapIv', max_length=50, blank=True, null=True)  # Field name made lowercase.
    threshold = models.IntegerField()
    corronly = models.IntegerField(db_column='corrOnly')  # Field name made lowercase.
    outres_id = models.IntegerField(db_column='outRes_id', blank=True, null=True)  # Field name made lowercase.
    outdistr = models.IntegerField(db_column='outDistr')  # Field name made lowercase.
    dist_output_id = models.IntegerField(blank=True, null=True)
    outthreshold = models.FloatField(db_column='outThreshold')  # Field name made lowercase.
    outspectr = models.IntegerField(db_column='outSpectr')  # Field name made lowercase.
    outchrom = models.IntegerField(db_column='outChrom')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'corr_param'


class CorrRun(models.Model):
    track1 = models.ForeignKey('CorrTrack', related_name="track1")
    track2 = models.ForeignKey('CorrTrack', related_name="track2")
    param = models.ForeignKey(CorrParam)
    prog_run_id = models.CharField(max_length=20)
    nfgr = models.IntegerField(db_column='nFgr')  # Field name made lowercase.
    bkg_av = models.FloatField(db_column='Bkg_av')  # Field name made lowercase.
    fg_av = models.FloatField(db_column='Fg_av')  # Field name made lowercase.
    bkg_sd = models.FloatField(db_column='Bkg_sd')  # Field name made lowercase.
    fg_sd = models.FloatField(db_column='Fg_sd')  # Field name made lowercase.
    tot_cor = models.FloatField()
    mann_z = models.FloatField()
    p_value = models.FloatField()
    pc = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'corr_run'


class CorrSample(models.Model):
    sample = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'corr_sample'


class CorrScaleParam(models.Model):
    scale = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'corr_scale_param'


class CorrTissue(models.Model):
    tissue = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'corr_tissue'


class CorrTrack(models.Model):
    tissue = models.ForeignKey(CorrTissue, blank=True, null=True)
    mark = models.ForeignKey(CorrMark)
    sample = models.ForeignKey(CorrSample)
    lab = models.ForeignKey(CorrLab, blank=True, null=True)
    devstage = models.ForeignKey(CorrDevstage, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corr_track'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = ['app_label', 'model']


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
