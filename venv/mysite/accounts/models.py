from django.db import models

class SampleDB(models.Model):
    class Meta:
        db_table = 'syain_info' # DB���Ŏg�p����e�[�u����
        verbose_name_plural = 'sample_table' # Admion�T�C�g�ŕ\������e�[�u����
    sample1 = models.IntegerField('sample1', null=True, blank=True) # ���l���i�[
    sample2 = models.CharField('sample2', max_length=255, null=True, blank=True) # ��������i�[
# Create your models here.
