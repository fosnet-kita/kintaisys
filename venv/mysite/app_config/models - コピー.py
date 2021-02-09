from django.db import models

class SampleDB(models.Model):
    class Meta:
        db_table = 'TORIHIKISAKI_LIST' # DB内で使用するテーブル名
        verbose_name_plural = 'TORIHIKISAKI_LIST' # Admionサイトで表示するテーブル名
    CUSTOMNAME = models.CharField('CUSTOMNAME', max_length=16, default='sic')
# Create your models here.
