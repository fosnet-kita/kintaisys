from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

class project_work(models.Model):
    class Meta:
        db_table = 'project_work' # DB内で使用するテーブル名
    projectname = models.CharField('projectname', max_length=16,unique=True)
    kouteicd = models.CharField('kouteicd', max_length=8, default='0001')
    kouteiname = models.CharField('kouteiname', max_length=32, default='テスト')
    workcd = models.CharField('workcd', max_length=8, default='00001')
    workname = models.CharField('workname', max_length=32, default='仕様書作成')
    projectcd = models.CharField('projectcd', max_length=8,  default='')
    def __str__(self):
       return self.projectname
       
    def __str__str(self2):
       return self2.workname
# Create your models here.

class torihikisaki_list(models.Model):
    class Meta:
        db_table = 'torihikisaki_list' # DB内で使用するテーブル名
    customname = models.CharField('customname', max_length=16)
    def __str__(self):
       return self.customname
# Create your models here.

class trans_info(models.Model):
    class Meta:
        db_table = 'trans_info' # DB内で使用するテーブル名
    tourokukbn = models.CharField('shinseikbn', max_length=16, default='申請済')
    tourokuno = models.CharField('tourokunon', max_length=16, default='0001')
    syaincd = models.CharField('syaincd', max_length=16, default='0001')
    syainname = models.CharField('syaincd', max_length=16, default='')
    tourokudate = models.DateField('tourokudate', max_length=16, default='TODAY')
    startdate = models.DateField('startdate', max_length=16, default='TODAY')
    enddate = models.DateField('enddate', max_length=16, default='TODAY')
    homon = models.CharField('homon', max_length=16,default='a')
    kamoku = models.CharField('kamoku', max_length=16,default='交通費')
    syudan = models.CharField('syudan', max_length=16,default='電車')
    transport = models.IntegerField('transport',default=0)
    k_seikyu = models.CharField('transport',max_length=2,default='')
    customname = models.CharField('customname',max_length=16,default='')
    seisan_kbn = models.CharField('seisan_kbn',max_length=16,default='現金')
# Create your models here.

class syain_info(models.Model):
    class Meta:
        db_table = 'syain_info' # DB内で使用するテーブル名
    syaincd = models.CharField('syaincd', max_length=8)
    syainname = models.CharField('syainname', max_length=16)
    password = models.CharField('password', max_length=16,validators=[MinLengthValidator(8, '8文字以上です！'),
                                            RegexValidator(r'^[a-zA-Z0-9]*$', '英数字のみです！')])
    def __str__str(self1):
       return self1.syaincd
       
    def __str__str(self2):
       return self2.password
       
    def __str__str(self3):
       return self3.syainname
       
class kintai_touroku_info(models.Model):
    class Meta:
        db_table = 'kintai_touroku_info' # DB内で使用するテーブル名
    syaincd = models.CharField('syaincd', max_length=8)
    syainname = models.CharField('syainname', max_length=16)
    ymd = models.DateField('ymd',  default='2020-11-20')
    starttime = models.TimeField('starttime',  default='09:00')
    endtime = models.TimeField('endtime',  default='17:30')
    worktime = models.DecimalField('worktime' ,max_digits=5, decimal_places=2, default=0)
    overtime = models.DecimalField('overtime', max_digits=5, decimal_places=2 , default=0)
    mntime          = models.DecimalField('mntime',max_digits=5, decimal_places=2 ,  default=0)
    mnovertime      = models.DecimalField('movertime',max_digits=5, decimal_places=2 ,  default=0)
    morning         = models.DecimalField('morning',max_digits=5, decimal_places=2 ,  default=0)
    paidtime        = models.DecimalField('paidtime',max_digits=5, decimal_places=2 ,  default=0)
    resttime        = models.DecimalField('resttime',max_digits=5, decimal_places=2 ,  default=0)
    attkbn          = models.IntegerField('mntime',  default=0)
    holidaykbn      = models.IntegerField('movertime', default=0)
    holidayriyu     = models.CharField('holidayriyu', max_length=32, default=0)
    todokekbn       = models.IntegerField('todokekbn', default=0)
    todoke_tikoku   = models.IntegerField('todoke_tikoku', default=0)
    todoke_soutai   = models.IntegerField('todoke_soutai', default=0)
    todoke_midnight = models.IntegerField('todoke_midnight',  default=0)
    todoke_hayade   = models.IntegerField('todoke_hayade',  default=0)
    todoke_irregular= models.IntegerField('todoke_irregular',  default=0)
    todoke_holiwork = models.IntegerField('todoke_holiwork',  default=0)
    projectname1 = models.CharField('projectname', max_length=16,  default='')
    kouteiname1 = models.CharField('kouteiname', max_length=16, default='')
    workname1 = models.CharField('workname', max_length=32,  default='')
    start1 = models.TimeField('start1',  default='')
    end1 = models.TimeField('end1',    default='')
    rest1 = models.DecimalField('rest1',max_digits=5, decimal_places=2,  default=0)
    projectcd1 = models.CharField('projectcd1', max_length=8,  default='')
    kouteicd1 = models.CharField('kouteicd1', max_length=8, default='')
    workcd1 = models.CharField('workcd1', max_length=8,  default='')
    
    projectname2 = models.CharField('projectname2', max_length=8,  default='')
    kouteiname2 = models.CharField('kouteiname2', max_length=8, default='')
    workname2 = models.CharField('workname2', max_length=8,  default='')
    start2 = models.TimeField('start2',  default='')
    end2 = models.TimeField('end2',  default='')
    rest2 = models.DecimalField('rest2',max_digits=5, decimal_places=2,  default=0)
    projectcd2 = models.CharField('projectcd2', max_length=8,  default='')
    kouteicd2 = models.CharField('kouteicd2', max_length=8, default='')
    workcd2 = models.CharField('workcd2', max_length=8,  default='')
    
    
    projectname3 = models.CharField('projectname3', max_length=16,  default='')
    kouteiname3 = models.CharField('kouteiname3', max_length=16, default='')
    workname3 = models.CharField('workname3', max_length=32,  default='')
    start3 = models.TimeField('start3', default='')
    end3 = models.TimeField('end3',  default='')
    rest3 = models.DecimalField('rest3',max_digits=5, decimal_places=2,  default=0)
    projectcd3 = models.CharField('projectcd3', max_length=8,  default='')
    kouteicd3 = models.CharField('kouteicd3', max_length=8, default='')
    workcd3 = models.CharField('workcd3', max_length=8,  default='')
    
    
    projectname4 = models.CharField('projectname4', max_length=16, default='')
    kouteiname4 = models.CharField('kouteiname4', max_length=16, default='')
    workname4 = models.CharField('workname4', max_length=32,  default='')
    start4 = models.TimeField('start4',  default='')
    end4 = models.TimeField('end4',  default='')
    rest4 = models.DecimalField('rest4',max_digits=5, decimal_places=2,  default=0)
    projectcd4 = models.CharField('projectcd4', max_length=8,  default='')
    kouteicd4 = models.CharField('kouteicd4', max_length=8, default='')
    workcd4 = models.CharField('workcd4', max_length=8,  default='')
    
    
    
    
    
class project_uchiwake(models.Model):
    class Meta:
        db_table = 'project_uchiwake' # DB内で使用するテーブル名
    tourokuno = models.CharField('tourokuno', max_length=16)
    projectname = models.CharField('projectname', max_length=16)
    kouteiname = models.CharField('kouteiname',  max_length=32)
    workname = models.CharField('worktime',  max_length=32)
    starttime = models.TimeField('starttime',  default='09:00')
    endtime = models.TimeField('endtime',  default='17:30')
    resttime        = models.DecimalField('resttime',max_digits=5, decimal_places=2 ,  default=0)
    
