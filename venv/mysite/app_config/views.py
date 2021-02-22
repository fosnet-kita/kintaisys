from django.http import HttpResponse
from django.template import RequestContext
from app_folder.models import syain_info
from app_folder.models import project_work
from app_folder.models import torihikisaki_list
from app_folder.models import trans_info
from app_folder.models import kintai_touroku_info
from django.db.models import Avg, Max, Min, Sum
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads,dumps
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from .forms import CustomUserCreateForm
from django.contrib.auth.views import LoginView
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http.response import JsonResponse

#from google2authtest.apps.utils import get_secret, get_image_b64, get_auth_url

#from cms.models.two_auth import TwoAuth



from .forms import CustomLoginForm
from . import utils
from django_otp.admin import OTPAdminSite
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin
from django.core.mail import send_mail
from twilio.rest import Client
import urllib.request

import datetime
import calendar
import locale
import os
import secrets
import qrcode
import pyotp
import time
import webbrowser

import sys
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib, ssl
import tkinter as tk
import tkinter.simpledialog as simpledialog
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders
from os.path import basename

User = get_user_model()
#win = tk.Tk()

import subprocess


text_name = ""


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render( None, request))
    
def login(request):
    template = loader.get_template('registration/login.html')
    
    
    return HttpResponse(template.render( None, request))
    
def password(request):
    template = loader.get_template('registration/password_change.html')
    print('pass')
    return HttpResponse(template.render( None, request))
    
def passwordchange(request):
    template = loader.get_template('registration/password_change.html')    
    id = request.POST.get('UserId','')
    passw =request.POST.get('Password','')
    passn =request.POST.get('APassword','')
    passk =request.POST.get('KPassword','')
    list =  syain_info.objects.all()
    context = {}
    if(len(passn) < 8):
       context.update({
              'shorterror': '新パスワードは8文字以上で入力してください',
       })
       
    if (passn != passk):
       context.update({
             'kakuninerror': '新パスワード,確認パスワードが一致しません',
         })
    if (passn == passw):
       context.update({
             'sameerror': '新パスワードと旧パスワードが同じです',
         })
    sameflg = False
    for i in range(len(list)):
      syaincd1=list[i].syaincd
      password1=list[i].password
      if (id != syaincd1 or passw != password1):
        continue        
      sameflg = True     
      if(passn == passk and passn != passw and len(passn) >= 8):
           p =  syain_info.objects.filter(syaincd = syaincd1)
           print(p)
           p.update(password = passn)
           return render(request, 'registration/login.html')
           
    if not sameflg:
       context.update({
              'matcherror': 'ユーザーidまたはパスワードが違います',
       })
    return render(request, 'registration/password_change.html', context)
    
def koutuhilist(request):
    template = loader.get_template('registration/koutuhi_itiran.html')
    id = request.session.get('User','')
    data = trans_info.objects.filter(syaincd = id)
    print(data)
    my_dict2 = {
        'data':  data
    }
    return render(request, 'registration/koutuhi_itiran.html', my_dict2)
    
def koutuhi(request):
    template = loader.get_template('registration/koutuhi.html')
    listtori =  torihikisaki_list.objects.all()
    request.session['User'] = request.POST['User']
    request.session['Pass'] = request.POST['Pass']
    id = request.POST['User']
    passw = request.POST['Pass']
    
    list =  syain_info.objects.all()

    for i in range(len(list)):
      syaincd=list[i].syaincd
      password=list[i].password
      email=list[i].email
      print(list[i].syaincd)
      print(list[i].password)
      print(list[i].email)
      if (id == syaincd and passw == password):
         #current_site = get_current_site(self.request)
         #domain = current_site.domain
         #
         context = {
                   'user':id,
              }
         # ユーザーに渡す乱数を作成
         random_base32 = pyotp.random_base32()
         # uriを作成
         uri = pyotp.totp.TOTP('base32secret3232').provisioning_uri(name="j1409032@yahoo.co.jp",issuer_name="サンプルアプリ")
         # QRコードを作成
         img = qrcode.make(uri)
         img.save('qr_code.png')
         
         webbrowser.open_new_tab('http://127.0.0.1:8000/accounts/kintai/')

         # OneTimePasswordを表示
         totp = pyotp.TOTP('base32secret3232')
         print(totp.now())
         print('open')
         gmail_account = "j1409032@gmail.com"
         gmail_password = "mamoka1212"
         ## メールの送信先 --- (*2)
         mail_to = email
         subject = "2要素認証です"
         body = "添付ファイルのQRコードを読み取ってください"
         encoding = 'utf-8'
         msg = MIMEMultipart()
         msg["Subject"] = Header(subject, encoding)
         msg["To"] = mail_to
         msg["From"] = gmail_account
         msg.attach(MIMEText(body, 'plain', encoding))
         
         # ファイルを添付
         path = "./qr_code.png"
         with open(path, "rb") as f:
            part = MIMEApplication(
            f.read(),
            Name=basename(path)
            )
 
         part['Content-Disposition'] = 'attachment; filename="%s"' % basename(path)
         msg.attach(part)
         
         # Gmailに接続 --- (*6)
         server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
         context=ssl.create_default_context())
         server.login(gmail_account, gmail_password)
         server.send_message(msg) # メールの送信
         
         
         root = tk.Tk()
         
         root.withdraw()
         
         time.sleep(5)
         
         inputdata = simpledialog.askstring("Input Box", "QRコードに表示される認証コードを入力してください",)
         print("simpledialog",inputdata)
         
         root.destroy()
         server.quit()
         if(inputdata == totp.now()):
            print('OK')
            return render(request, 'registration/koutuhi.html', context)
         else:
            print('NG')
            context = {
              'error': '認証コードが違います',
            }
            return render(request, 'registration/login.html', context)
    context = {
              'error': 'ユーザーIDまたはパスワードが違います',
        }
    return render(request, 'registration/login.html', context)

def koutuhisubmit(request):
    template = loader.get_template('registration/koutuhi.html')
    list =  torihikisaki_list.objects.all()
    ida = request.session.get('User','')
    name = syain_info.objects.get(syaincd=ida).syainname
    torihiki = request.POST.get('torihiki', '')

    if request.method == 'POST':
      tourokuno = request.POST.get('tourokuno', '')
      kbn = request.POST['tourokukbn']
      date = datetime.date.today()
      
      
      startdatelist = []
      enddatelist = []
      homonlist = []
      kamokulist = []
      syudanlist = []
      transportlist = []
      seikyulist = []
      count = 0
      seisan = request.POST['seisan']
      
      
      for i in range(len(request.POST.getlist('homonlist', None))):
         start = request.POST.getlist('startdatelist', None)[i]
         end = request.POST.getlist('enddatelist', None)[i]
         startstr = start[:4] + '-' + start[4:6] + '-' + start[6:]
         endstr = end[:4] + '-' + end[4:6] + '-' + end[6:]
         homon = request.POST.getlist('homonlist', None)[i]
         kamoku = request.POST.getlist('kamokulist', None)[i]
         syudan = request.POST.getlist('syudanlist', None)[i]
         transport = request.POST.getlist('transportlist', None)[i]
         seikyu = request.POST.getlist('seikyulist', None)[i]
         startdatelist.append(startstr)
         enddatelist.append(endstr)
         homonlist.append(homon)
         kamokulist.append(kamoku)
         syudanlist.append(syudan)
         transportlist.append(transport)
         seikyulist.append(seikyu)

         tourokuid = '10' + str(trans_info.objects.count())

         
         if (kbn == '削除'):
            print('delete')
            b = trans_info.objects.filter(tourokuno = str(tourokuno))
            b.delete()
         if (kbn == '修正'):
            print('update')
            b = trans_info.objects.filter(tourokuno = str(tourokuno))
            b.update(tourokukbn = kbn,tourokudate = date,customname = torihiki,homon = homonlist[i],tourokuno = tourokuid,
             startdate = startdatelist[i], enddate = startdatelist[i],kamoku = kamokulist[i], 
             syudan = syudanlist[i],transport = transportlist[i], k_seikyu = seikyulist[0], seisan_kbn = seisan)
         if (kbn == '登録'):
            print('set')
            b = trans_info(syaincd = ida,syainname = name,tourokukbn = kbn,customname = torihiki, tourokudate = date,
            homon = homonlist[i],tourokuno = tourokuid, startdate = startdatelist[i], enddate = startdatelist[i],
            kamoku = kamokulist[i], syudan = syudanlist[i],transport = transportlist[i], k_seikyu = seikyulist[0], 
            seisan_kbn = seisan)
            b.save()
    cus = {
               'cus': list,
               'message': '処理が完了しました',
          }
    return render(request, 'registration/koutuhi.html', cus)
def appearrance(request):
    template = loader.get_template('registration/syukketsusentaku.html')
    return HttpResponse(template.render( None, request))


# 一覧出力画面(年月選択前)
def output(request):
    template = loader.get_template('registration/output_ichiran.html')
    
    return HttpResponse(template.render( None, request))

# 一覧出力画面(年月選択後)
def output2(request):
    
    datelist = []
    weeklist = []
    monthyear =request.POST['monthselect']
    year = monthyear[:4]
    month = monthyear[5:7]
    monthz = monthyear[5:6]
    ida = request.session.get('User','')

    # 選択月の0埋めを無効化
    month_range = calendar.monthrange(int(year), int(month))
 
    listf = kintai_touroku_info.objects.filter(ymd__month = month,syaincd = ida).order_by('ymd')
    listmmm = []
    listweek = []
    
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    # 日数分ループ
    for i in range(1,month_range[1] + 1):
       listmmm.append(i)
       date = datetime.date(int(year), int(month),i)
       print(date.strftime('%a'))
       listweek.append(i)
    
    
    # DB格納日数分ループ
    for i in range(len(listf)):
       mmmm = listf[i].ymd.day
       listmmm[mmmm - 1] = listf[i] # DBのデータ格納
       

    # DB未格納箇所を日付型に変換
    for i in range(1,month_range[1] + 1):
       if  i in listmmm:
            listmmm[i - 1] = str(year) + str(month) + str(format(i, '02'))
            listmmm[i - 1] = datetime.datetime.strptime(listmmm[i - 1], '%Y%m%d')

    # 休暇理由、届出種類を数値から日本語に変換
    for i in range(len(listf)):
           kanmaflg = False
           if (listf[i].holidayriyu  == "0"):
              listf[i].holidayriyu = str(listf[i].holidayriyu)
              listf[i].holidayriyu = ""
              
              
           if (listf[i].todoke_tikoku  == 0):
              listf[i].todoke_tikoku = str(listf[i].todoke_tikoku)
              listf[i].todoke_tikoku = ""
              
           if (listf[i].todoke_soutai  == 0):
              listf[i].todoke_soutai = str(listf[i].todoke_soutai)
              listf[i].todoke_soutai = ""
              
           if (listf[i].todoke_midnight  == 0):
              listf[i].todoke_midnight = str(listf[i].todoke_midnight)
              listf[i].todoke_midnight = ""
              
           if (listf[i].todoke_hayade  == 0):
              listf[i].todoke_hayade = str(listf[i].todoke_hayade)
              listf[i].todoke_hayade = ""
              
           if (listf[i].todoke_irregular  == 0):
              listf[i].todoke_irregular = str(listf[i].todoke_irregular)
              listf[i].todoke_irregular = ""
              
           if (listf[i].todoke_holiwork  == 0):
              listf[i].todoke_holiwork = str(listf[i].todoke_holiwork)
              listf[i].todoke_holiwork = ""
              
           if (listf[i].todoke_tikoku  == 1):
              listf[i].todoke_tikoku = str(listf[i].todoke_tikoku)
              listf[i].todoke_tikoku = "遅刻"
              kanmaflg = True
           if (listf[i].todoke_soutai  == 1):
              listf[i].todoke_soutai = str(listf[i].todoke_soutai)
              if kanmaflg:
                listf[i].todoke_soutai = ",早退"
              else:
                listf[i].todoke_soutai = "早退"
              kanmaflg = True
              
           if (listf[i].todoke_midnight  == 1):
              listf[i].todoke_midnight = str(listf[i].todoke_midnight)
              if kanmaflg:
                listf[i].todoke_midnight = ",深夜"
              else:
                listf[i].todoke_midnight = "深夜"
              kanmaflg = True
              
           if (listf[i].todoke_hayade  == 1):
              listf[i].todoke_hayade = str(listf[i].todoke_hayade)
              if kanmaflg:
                listf[i].todoke_hayade = ",早出"
              else:
                listf[i].todoke_hayade = "早出"
              kanmaflg = True
              
           if (listf[i].todoke_irregular  == 1):
              listf[i].todoke_irregular = str(listf[i].todoke_irregular)
              if kanmaflg:
                listf[i].todoke_irregular = ",変則出勤"
              else:
                listf[i].todoke_irregular = "変則出勤"
              kanmaflg = True
              
           if (listf[i].todoke_holiwork  == 1):
              listf[i].todoke_holiwork = str(listf[i].todoke_holiwork)
              if kanmaflg:
                listf[i].todoke_holiwork = ",休日出勤"
              else:
                listf[i].todoke_holiwork = "休日出勤"

    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    sumwork = float(0.0);
    overwork = float(0.0);
    resttime = float(0.0);
    
    for l in listf:
        sumwork = sumwork + float(l.worktime)
        overwork = overwork + float(l.overtime)
        resttime = resttime + float(l.resttime)
    
    sumwork = round(sumwork,2)
    overwork = round(overwork,2)
    resttime = round(resttime,2)
    context = {
         'monthselect' : monthyear,
         'listaaaa': listmmm,
         'sumwork': sumwork,
         'overwork': overwork,
         'resttime': resttime,
    }
    return render(request, 'registration/output_ichiran.html', context)
    

def project(request):
    template = loader.get_template('registration/projecttouroku.html')
    list =  project_work.objects.all().distinct('projectname')
    projectselect1 =  request.session.get('project1', '')
    projectselect2 =  request.session.get('project2', '')
    projectselect3 =  request.session.get('project3', '')
    projectselect4 =  request.session.get('project4', '')
    request.session['abs'] = request.POST.get('absproject', '')
    request.session['chikoku'] = request.POST.get('chikokuproject', '')
    request.session['hayade'] = request.POST.get('hayadeproject', '')
    request.session['soutai'] = request.POST.get('soutaiproject', '')
    request.session['hensoku'] = request.POST.get('hensokuproject', '')
    request.session['midnight'] = request.POST.get('midnightproject', '')
    request.session['holiday'] = request.POST.get('holidayproject', '')
    request.session['holidaykbn'] = request.POST.get('holidaykbnproject', '')
    request.session['riyu'] = request.POST.get('riyuproject', '')
    request.session['starttime'] = request.POST.get('starttime', '')
    request.session['endtime'] = request.POST.get('endtime', '')
    request.session['overtime'] = request.POST.get('overtime', '')
    cont = {
        'pro': list,
        'projectselect1': projectselect1,
        'projectselect2': projectselect2,
        'projectselect3': projectselect3,
        'projectselect4': projectselect4,
    }
    return render(request, 'registration/projecttouroku.html', context=cont)
    
# 出欠選択画面
def kintaiabs(request):
    template = loader.get_template('registration/kintai.html')
    request.session['Absentkbn'] = request.POST['Absentkbn']
    abskbn = ""
        
    kbn = request.POST.get('holidaykbn', '')
    abs = request.POST.get('Absentkbn', '')
    if (abs == '0'):
        abskbn = "出勤"
    if (abs == '1'):
        abskbn = "欠勤"
        
    context = {}
    if(abs == ''):
        context.update({
                  'riyuerror': '出欠区分を選択してください',
           })
        return render(request, 'registration/syukketsusentaku.html', context)
        

    riyu = request.POST.get('riyu', '')
    
    chikoku = request.POST['Todokede0']
    hayade  = request.POST['Todokede1']
    soutai  = request.POST['Todokede2']
    hensoku = request.POST['Todokede3']
    midnight = request.POST['Todokede4']
    holiday = request.POST['Todokede5']
    

    value1 = project_work.objects.filter(projectname=request.session.get('touroku1', '')).distinct('kouteiname')
    value2 = project_work.objects.filter(projectname=request.session.get('touroku2', '')).distinct('kouteiname')
    value3 = project_work.objects.filter(projectname=request.session.get('touroku3', '')).distinct('kouteiname')
    if(abs == '1'  and (kbn == '' or riyu == '')):
       if(kbn == ''):
           context.update({
                  'holierror': '休暇区分を選択してください',
           })
       if(riyu == ''):
           context.update({
                  'riyuerror': '休暇理由を選択してください',
           })
       return render(request, 'registration/syukketsusentaku.html', context)
    kanmaflg = False
    
    if(chikoku != ''):
        kanmaflg = True
    if(hayade != ''):
        if kanmaflg:
            hayade = ',早出有'
        else:
            hayade = '早出有'        
    kanmaflg = True
    
    if(soutai != ''):
        if kanmaflg:
            soutai = ',早退'
        else:
            soutai = '早退'        
    kanmaflg = True
    
    if(hensoku != ''):
        if kanmaflg:
            hensoku = ',変則勤務'
        else:
            hensoku = '変則勤務'        
    kanmaflg = True
    
    if(midnight!= ''):
        if kanmaflg:
            midnight= ',深夜有'
        else:
            midnight= '深夜有'        
    kanmaflg = True
    
    if(holiday!= ''):
        if kanmaflg:
            holiday= ',休日出勤'
        else:
            holiday= '休日出勤'        
    kanmaflg = True

    context = {
                'ymd': request.session.get('dateselect', ''),
                'starttime': request.session.get('starttime', ''),
                'endtime': request.session.get('endtime', ''),
                'overtime': request.session.get('overtime', ''),
                'projectname1': request.session.get('touroku1', ''),
                'projectname2': request.session.get('touroku2', ''),
                'projectname3': request.session.get('touroku3', ''),
                'koutei1': value1,
                'koutei2': value2,
                'koutei3': value3,
                'abs'    : abskbn,
                'chikoku' : chikoku,
                'hayade'  : hayade,
                'soutai'  : soutai,
                'hensoku' : hensoku,
                'midnight': midnight,
                'holiday' : holiday,
          }
    return render(request, 'registration/kintai.html', context)

      
def kintaiproject(request):
    template = loader.get_template('registration/kintai.html')
    dateselect = request.session.get('dateselect', '')
    abs = request.session.get('abs', '')
    hol = request.session.get('holidaykbn','')
    riyu = request.session.get('riyu','')
    todo0 = request.session.get('chikoku','')
    todo1 = request.session.get('hayade','')
    todo2 = request.session.get('soutai','')
    todo3 = request.session.get('hensoku','')
    todo4 = request.session.get('midnight','')
    todo5 = request.session.get('holiday','')
    ida = request.session.get('User','')
    
    value = project_work.objects.all().distinct('workname')
    value1 = project_work.objects.filter(projectname=request.POST['touroku1']).distinct('kouteiname')
    value2 = project_work.objects.filter(projectname=request.POST['touroku2']).distinct('kouteiname')
    value3 = project_work.objects.filter(projectname=request.POST['touroku3']).distinct('kouteiname')
    value4 = project_work.objects.filter(projectname=request.POST['touroku4']).distinct('kouteiname')  
    
    touroku1 = request.POST['touroku1']
    touroku2 = request.POST['touroku2']
    touroku3 = request.POST['touroku3']
    touroku4 = request.POST['touroku4']
    print("touroku1 " + touroku1)
    request.session['touroku1'] = request.POST['touroku1']
    request.session['touroku2'] = request.POST['touroku2']
    request.session['touroku3'] = request.POST['touroku3']
    request.session['touroku4'] = request.POST['touroku4']
    if request.method == 'POST':
      context = {
                'ymd': dateselect,
                'starttime': request.session.get('starttime', ''),
                'endtime': request.session.get('endtime', ''),
                'overtime': request.session.get('overtime', ''),
                'projectname1': touroku1,
                'projectname2': touroku2,
                'projectname3': touroku3,
                'projectname4': touroku4,
                'koutei1': value1,
                'koutei2': value2,
                'koutei3': value3,
                'koutei4': value4,
                'abs': abs,
                'chikoku' : todo0,
                'hayade'  : todo1,
                'soutai'  : todo2,
                'hensoku' : todo3,
                'midnight': todo4,
                'holiday' : todo5,
                'holidaykbn': hol,
                'riyu' : riyu,
                'user' : ida,
          }
      return render(request, 'registration/kintai.html', context)
    return HttpResponse(template.render( None, request))
    
#勤怠登録押下、工程選択時    
def kintaitouroku(request):
    template = loader.get_template('registration/kintai.html')
    btt = request.POST.get('btnExecH','')
    abs  = request.POST.get('abs','')
    nowyear = str(datetime.date.today().year)
    nowmonth = str(format(datetime.date.today().month,'02'))
    nowday = str(format(datetime.date.today().day,'02'))
    nowdate = nowyear + "-" +  nowmonth +  "-" + nowday
    timestr = request.POST.get('dateselect',nowdate)
    
    ida = request.session.get('User','')
    listf = kintai_touroku_info.objects.filter(ymd = timestr,syaincd = ida)
    errflg = False
    context = {}   
    syainname =  syain_info.objects.all()   
    start = request.POST.get('starttime', '')
    end = request.POST.get('endtime', '')
    over = request.POST.get('overtime', '')

    tourokuope = request.POST.get('tourokuope','')
    if(tourokuope != ''):
        t1 = request.POST.get('project1','')
        t2 = request.POST.get('project2','')
        t3 = request.POST.get('project3','')
        t4 = request.POST.get('project4','')
        request.session['project1'] = request.POST.get('project1','')
        request.session['project2'] = request.POST.get('project2','')
        request.session['project3'] = request.POST.get('project3','')
        request.session['project4'] = request.POST.get('project4','')
    else:
        t1 = request.POST.get('projectname1','')
        t2 = request.POST.get('projectname2','')
        t3 = request.POST.get('projectname3','')
        t4 = request.POST.get('projectname4','')
    
    pcd1 = project_work.objects.filter(projectname = t1)
    pcd2 = project_work.objects.filter(projectname = t2)
    pcd3 = project_work.objects.filter(projectname = t3)
    pcd4 = project_work.objects.filter(projectname = t4)
    
    if (len(pcd1) != 0):
        projectcd1 = pcd1[0].projectcd
    else:
        projectcd1 = ""
    print("projectcd1" + projectcd1)
    
    if (len(pcd2) != 0):
        projectcd2 = pcd2[0].projectcd
    else:
        projectcd2 = ""
    print("projectcd2" + projectcd2)
    
    if (len(pcd3) != 0):
        projectcd3 = pcd3[0].projectcd
    else:
        projectcd3 = ""
    print("projectcd3" + projectcd3)
    
    if (len(pcd4) != 0):
        projectcd4 = pcd4[0].projectcd
    else:
        projectcd4 = ""
    print("projectcd4" + projectcd4)

    koutei1 = request.POST.get('kouteiname1','')
    koutei2 = request.POST.get('kouteiname2','')
    koutei3 = request.POST.get('kouteiname3','')
    koutei4 = request.POST.get('kouteiname4','')
    kcd1 = project_work.objects.filter(kouteiname = koutei1)
    kcd2 = project_work.objects.filter(kouteiname = koutei2)
    kcd3 = project_work.objects.filter(kouteiname = koutei3)
    kcd4 = project_work.objects.filter(kouteiname = koutei4)
    if (len(kcd1) != 0):
        kouteicd1 = kcd1[0].kouteicd
    else:
        kouteicd1 = ""
    
    if (len(kcd2) != 0):
        kouteicd2 = kcd2[0].kouteicd
    else:
        kouteicd2 = ""
    
    if (len(kcd3) != 0):
        kouteicd3 = kcd3[0].kouteicd
    else:
        kouteicd3 = ""
    
    if (len(kcd4) != 0):
        kouteicd4 = kcd4[0].kouteicd
    else:
        kouteicd4 = ""
    
    gyomuselect1 = request.POST.get('workname1','')
    gyomuselect2 = request.POST.get('workname2','')
    gyomuselect3 = request.POST.get('workname3','')
    gyomuselect4 = request.POST.get('workname4','')
    gcd1 = project_work.objects.filter(workname = gyomuselect1)
    gcd2 = project_work.objects.filter(workname = gyomuselect2)
    gcd3 = project_work.objects.filter(workname = gyomuselect3)
    gcd4 = project_work.objects.filter(workname = gyomuselect4)
    
    if (len(gcd1) != 0):
        workcd1 = gcd1[0].workcd
    else:
        workcd1 = ""
    print("workcd1" + workcd1)
    
    if (len(gcd2) != 0):
        workcd2 = gcd2[0].workcd
    else:
        workcd2 = ""
    print("workcd2" + workcd2)
    
    if (len(gcd3) != 0):
        workcd3 = gcd3[0].workcd
    else:
        workcd3 = ""
    print("workcd3" + workcd3)
    
    if (len(gcd4) != 0):
        workcd4 = gcd4[0].workcd
    else:
        workcd4 = ""
    print("workcd4" + workcd4)
    
    value1 = project_work.objects.filter(projectname=t1).distinct('kouteiname')
    value2 = project_work.objects.filter(projectname=t2).distinct('kouteiname')
    value3 = project_work.objects.filter(projectname=t3).distinct('kouteiname')
    value4 = project_work.objects.filter(projectname=t4).distinct('kouteiname')
    gyomu1 = project_work.objects.filter(projectname=t1,kouteiname=koutei1)
    gyomu2 = project_work.objects.filter(projectname=t2,kouteiname=koutei2)
    gyomu3 = project_work.objects.filter(projectname=t3,kouteiname=koutei3)
    gyomu4 = project_work.objects.filter(projectname=t4,kouteiname=koutei4)
    
    starttime1 = request.POST.get('starttime1','00:00')
    starttime2 = request.POST.get('starttime2','00:00')
    starttime3 = request.POST.get('starttime3','00:00')
    starttime4 = request.POST.get('starttime4','00:00')
    endtime1 = request.POST.get('endtime1','00:00')
    endtime2 = request.POST.get('endtime2','00:00')
    endtime3 = request.POST.get('endtime3','00:00')
    endtime4 = request.POST.get('endtime4','00:00')
    resttime1 = request.POST.get('resttime1','0')
    resttime2 = request.POST.get('resttime2','0')
    resttime3 = request.POST.get('resttime3','0')
    resttime4 = request.POST.get('resttime4','0')

    hol = request.POST.get('holidaykbn','')
    riyu = request.POST.get('riyu','')
    todo0 = request.POST.get('chikoku','')
    todo1 = request.POST.get('hayade','')
    todo2 = request.POST.get('soutai','')
    todo3 = request.POST.get('hensoku','')
    todo4 = request.POST.get('midnight','')
    todo5 = request.POST.get('holiday','')

    if(btt != '勤怠登録'):

        if (abs == '欠勤'):
            context = {
                        'ymd': timestr,
                        'abs': abs,
                        'chikoku' : todo0,
                        'hayade'  : todo1,
                        'soutai'  : todo2,
                        'hensoku' : todo3,
                        'midnight': todo4,
                        'holiday' : todo5,
                        'holidaykbn': hol,
                        'riyu' : riyu,  
                        'user' : ida,
                      }
            return render(request, 'registration/kintai.html', context)

        request.session['kouteiname1'] = request.POST.get('kouteiname1','')
        request.session['kouteiname2'] = request.POST.get('kouteiname2','')
        request.session['kouteiname3'] = request.POST.get('kouteiname3','')
        request.session['kouteiname4'] = request.POST.get('kouteiname4','')
        context = {
                    'starttime': start,
                    'endtime': end,
                    'overtime': over,
                    'projectname1': t1,
                    'projectname2': t2,
                    'projectname3': t3,
                    'projectname4': t4,
                    'starttime1': request.POST.get('starttime1',''),
                    'starttime2': request.POST.get('starttime2',''),
                    'starttime3': request.POST.get('starttime3',''),
                    'starttime4': request.POST.get('starttime4',''),
                    'endtime1': request.POST.get('endtime1',''),
                    'endtime2': request.POST.get('endtime2',''),
                    'endtime3': request.POST.get('endtime3',''),
                    'endtime4': request.POST.get('endtime4',''),
                    'resttime1': request.POST.get('resttime1',''),
                    'resttime2': request.POST.get('resttime2',''),
                    'resttime3': request.POST.get('resttime3',''),
                    'resttime4': request.POST.get('resttime4',''),
                    'koutei1': value1,
                    'koutei2': value2,
                    'koutei3': value3,
                    'koutei4': value4,
                    'kouteiselect1': koutei1,
                    'kouteiselect2': koutei2,
                    'kouteiselect3': koutei3,
                    'kouteiselect4': koutei4,
                    'gyomu1': gyomu1,
                    'gyomu2': gyomu2,
                    'gyomu3': gyomu3,
                    'gyomu4': gyomu4,
                    'gyomuselect1': gyomuselect1,
                    'gyomuselect2': gyomuselect2,
                    'gyomuselect3': gyomuselect3,
                    'gyomuselect4': gyomuselect4,
                    'ymd':      timestr,
                    'abs': abs,
                    'chikoku' : todo0,
                    'hayade'  : todo1,
                    'soutai'  : todo2,
                    'hensoku' : todo3,
                    'midnight': todo4,
                    'holiday' : todo5,
                    'holidaykbn': hol,
                    'riyu' : riyu,  
                    'user' : ida,
             }
        return render(request, 'registration/kintai.html', context)

    name = syain_info.objects.get(syaincd=ida).syainname
    worktime = 0.0
    rest = 0.0
    holdb = 0
    todok = 0
    if(hol == "取得なし"):
        holdb = 0
        
    if(hol == "有給休暇"):
        holdb = 1

    if(hol == "特休・その他休暇"):
        holdb = 2

    if(hol == "代休"):
        holdb = 3
        
    if(hol == "その他"):
        holdb = 4
        
    if(hol == "半休等"):
        holdb = 5
        
    if(abs == '出勤'):
        absdb = 0
    if(abs == '欠勤'):
        absdb = 1
        


    if(abs == '出勤' or abs == ''):
    
        if (resttime1 == ''):
            resttime1 = 0
        if (resttime2 == ''):
            resttime2 = 0
        if (resttime3 == ''):
            resttime3 = 0
        if (resttime4 == ''):
            resttime4 = 0
        resttime = float(resttime1) +  float(resttime2) +  float(resttime3) + float(resttime4)
        midtime = 0
        midover = 0
        paidtime = 0
        morningtime = 0
        
        if( abs == '' ):
            context.update({
                  'absnerror': '出欠選択されていません',
                  'starttime': start,
                  'endtime': end,
                  'overtime': over,
                  'projectname1': t1,
                  'projectname2': t2,
                  'projectname3': t3,
                  'projectname4': t4,
                  'starttime1': request.POST.get('starttime1',''),
                  'starttime2': request.POST.get('starttime2',''),
                  'starttime3': request.POST.get('starttime3',''),
                  'starttime4': request.POST.get('starttime4',''),
                  'endtime1': request.POST.get('endtime1',''),
                  'endtime2': request.POST.get('endtime2',''),
                  'endtime3': request.POST.get('endtime3',''),
                  'endtime4': request.POST.get('endtime4',''),
                  'resttime1': request.POST.get('resttime1',''),
                  'resttime2': request.POST.get('resttime2',''),
                  'resttime3': request.POST.get('resttime3',''),
                  'resttime4': request.POST.get('resttime4',''),
                  'koutei1': value1,
                  'koutei2': value2,
                  'koutei3': value3,
                  'koutei4': value4,
                  'kouteiselect1': koutei1,
                  'kouteiselect2': koutei2,
                  'kouteiselect3': koutei3,
                  'kouteiselect4': koutei4,
                  'gyomu1': gyomu1,
                  'gyomu2': gyomu2,
                  'gyomu3': gyomu3,
                  'gyomu4': gyomu4,
                  'gyomuselect1': gyomuselect1,
                  'gyomuselect2': gyomuselect2,
                  'gyomuselect3': gyomuselect3,
                  'gyomuselect4': gyomuselect4,
                  'abs': abs,
                  'holidaykbn': hol,
                  'riyu' : riyu,
                  'chikoku' : todo0,
                  'hayade'  : todo1,
                  'soutai'  : todo2,
                  'hensoku' : todo3,
                  'midnight': todo4,
                  'holiday' : todo5,
                  'ymd': timestr,
                  'user' : ida,

            })
            print('abserror')
            errflg = True

        if(t1 == '' and t2 == '' and t3 == '' and t4 == ''):
            context.update({
                  'projecterror': 'プロジェクト登録をしてください',
                  'ymd': timestr,
                  'abs': abs,
                  'holidaykbn': hol,
                  'riyu' : riyu,
                  'chikoku' : todo0,
                  'hayade'  : todo1,
                  'soutai'  : todo2,
                  'hensoku' : todo3,
                  'midnight': todo4,
                  'holiday' : todo5,
                  'user' : ida,
            })
            errflg = True
        
        if( (t1 != '' and starttime1 == '')  or (t2 != '' and starttime2 == '') or (t3 != '' and starttime3 == '') or (t4 != '' and starttime4 == '') ):
            context.update({
                  'starterror': '開始時刻が入力されていません',
                  'starttime': start,
                  'endtime': end,
                  'overtime': over,
                  'projectname1': t1,
                  'projectname2': t2,
                  'projectname3': t3,
                  'projectname4': t4,
                  'starttime1': request.POST.get('starttime1',''),
                  'starttime2': request.POST.get('starttime2',''),
                  'starttime3': request.POST.get('starttime3',''),
                  'starttime4': request.POST.get('starttime4',''),
                  'endtime1': request.POST.get('endtime1',''),
                  'endtime2': request.POST.get('endtime2',''),
                  'endtime3': request.POST.get('endtime3',''),
                  'endtime4': request.POST.get('endtime4',''),
                  'resttime1': request.POST.get('resttime1',''),
                  'resttime2': request.POST.get('resttime2',''),
                  'resttime3': request.POST.get('resttime3',''),
                  'resttime4': request.POST.get('resttime4',''),
                  'koutei1': value1,
                  'koutei2': value2,
                  'koutei3': value3,
                  'koutei4': value4,
                  'kouteiselect1': koutei1,
                  'kouteiselect2': koutei2,
                  'kouteiselect3': koutei3,
                  'kouteiselect4': koutei4,
                  'gyomu1': gyomu1,
                  'gyomu2': gyomu2,
                  'gyomu3': gyomu3,
                  'gyomu4': gyomu4,
                  'gyomuselect1': gyomuselect1,
                  'gyomuselect2': gyomuselect2,
                  'gyomuselect3': gyomuselect3,
                  'gyomuselect4': gyomuselect4,
                  'abs': abs,
                  'holidaykbn': hol,
                  'riyu' : riyu,
                  'chikoku' : todo0,
                  'hayade'  : todo1,
                  'soutai'  : todo2,
                  'hensoku' : todo3,
                  'midnight': todo4,
                  'holiday' : todo5,
                  'ymd': timestr,
                  'user' : ida,
            })
            print('starterror')
            errflg = True
        if( (t1 != '' and endtime1 == '')  or (t2 != '' and endtime2 == '') or (t3 != '' and endtime3 == '') or (t4 != '' and endtime4 == '')  ):
            context.update({
                  'enderror': '終了時刻が入力されていません',
                  'starttime': start,
                  'endtime': end,
                  'overtime': over,
                  'projectname1': t1,
                  'projectname2': t2,
                  'projectname3': t3,
                  'projectname4': t4,
                  'starttime1': request.POST.get('starttime1',''),
                  'starttime2': request.POST.get('starttime2',''),
                  'starttime3': request.POST.get('starttime3',''),
                  'starttime4': request.POST.get('starttime4',''),
                  'endtime1': request.POST.get('endtime1',''),
                  'endtime2': request.POST.get('endtime2',''),
                  'endtime3': request.POST.get('endtime3',''),
                  'endtime4': request.POST.get('endtime4',''),
                  'resttime1': request.POST.get('resttime1',''),
                  'resttime2': request.POST.get('resttime2',''),
                  'resttime3': request.POST.get('resttime3',''),
                  'resttime4': request.POST.get('resttime4',''),
                  'koutei1': value1,
                  'koutei2': value2,
                  'koutei3': value3,
                  'koutei4': value4,
                  'kouteiselect1': koutei1,
                  'kouteiselect2': koutei2,
                  'kouteiselect3': koutei3,
                  'kouteiselect4': koutei4,
                  'gyomu1': gyomu1,
                  'gyomu2': gyomu2,
                  'gyomu3': gyomu3,
                  'gyomu4': gyomu4,
                  'gyomuselect1': gyomuselect1,
                  'gyomuselect2': gyomuselect2,
                  'gyomuselect3': gyomuselect3,
                  'gyomuselect4': gyomuselect4,
                  'abs': abs,
                  'holidaykbn': hol,
                  'riyu' : riyu,
                  'chikoku' : todo0,
                  'hayade'  : todo1,
                  'soutai'  : todo2,
                  'hensoku' : todo3,
                  'midnight': todo4,
                  'holiday' : todo5,
                  'ymd': timestr,
                  'user' : ida,
            })
            print('enderror')
            errflg = True
        

        if( (t1 != '' and koutei1 == '')  or (t2 != '' and koutei2 == '') or (t3 != '' and koutei3 == '') or (t4 != '' and koutei4 == '')):
            context.update({
                  'kouteierror': '工程が入力されていません',
                  'starttime': start,
                  'endtime': end,
                  'overtime': over,
                  'projectname1': t1,
                  'projectname2': t2,
                  'projectname3': t3,
                  'projectname4': t4,
                  'starttime1': request.POST.get('starttime1',''),
                  'starttime2': request.POST.get('starttime2',''),
                  'starttime3': request.POST.get('starttime3',''),
                  'starttime4': request.POST.get('starttime4',''),
                  'endtime1': request.POST.get('endtime1',''),
                  'endtime2': request.POST.get('endtime2',''),
                  'endtime3': request.POST.get('endtime3',''),
                  'endtime4': request.POST.get('endtime4',''),
                  'resttime1': request.POST.get('resttime1',''),
                  'resttime2': request.POST.get('resttime2',''),
                  'resttime3': request.POST.get('resttime3',''),
                  'resttime4': request.POST.get('resttime4',''),
                  'koutei1': value1,
                  'koutei2': value2,
                  'koutei3': value3,
                  'koutei4': value4,
                  'kouteiselect1': koutei1,
                  'kouteiselect2': koutei2,
                  'kouteiselect3': koutei3,
                  'kouteiselect4': koutei4,
                  'gyomu1': gyomu1,
                  'gyomu2': gyomu2,
                  'gyomu3': gyomu3,
                  'gyomu4': gyomu4,
                  'gyomuselect1': gyomuselect1,
                  'gyomuselect2': gyomuselect2,
                  'gyomuselect3': gyomuselect3,
                  'gyomuselect4': gyomuselect4,
                  'abs': abs,
                  'holidaykbn': hol,
                  'riyu' : riyu,  
                  'chikoku' : todo0,
                  'hayade'  : todo1,
                  'soutai'  : todo2,
                  'hensoku' : todo3,
                  'midnight': todo4,
                  'holiday' : todo5,
                  'ymd': timestr,
                  'user' : ida,

            })
            errflg = True
        if( (t1 != '' and gyomuselect1 == '')  or (t2 != '' and gyomuselect2 == '') or (t3 != '' and gyomuselect3 == '') or (t4 != '' and gyomuselect4 == '')):
            context.update({
                  'workerror': '業務が入力されていません',
                  'starttime': start,
                  'endtime': end,
                  'overtime': over,
                  'projectname1': t1,
                  'projectname2': t2,
                  'projectname3': t3,
                  'projectname4': t4,
                  'starttime1': request.POST.get('starttime1',''),
                  'starttime2': request.POST.get('starttime2',''),
                  'starttime3': request.POST.get('starttime3',''),
                  'starttime4': request.POST.get('starttime4',''),
                  'endtime1': request.POST.get('endtime1',''),
                  'endtime2': request.POST.get('endtime2',''),
                  'endtime3': request.POST.get('endtime3',''),
                  'endtime4': request.POST.get('endtime4',''),
                  'resttime1': request.POST.get('resttime1',''),
                  'resttime2': request.POST.get('resttime2',''),
                  'resttime3': request.POST.get('resttime3',''),
                  'resttime4': request.POST.get('resttime4',''),
                  'koutei1': value1,
                  'koutei2': value2,
                  'koutei3': value3,
                  'koutei4': value4,
                  'kouteiselect1': koutei1,
                  'kouteiselect2': koutei2,
                  'kouteiselect3': koutei3,
                  'kouteiselect4': koutei4,
                  'gyomu1': gyomu1,
                  'gyomu2': gyomu2,
                  'gyomu3': gyomu3,
                  'gyomu4': gyomu4,
                  'gyomuselect1': gyomuselect1,
                  'gyomuselect2': gyomuselect2,
                  'gyomuselect3': gyomuselect3,
                  'gyomuselect4': gyomuselect4,
                  'abs': abs,
                  'holidaykbn': hol,
                  'riyu' : riyu,
                  'chikoku' : todo0,
                  'hayade'  : todo1,
                  'soutai'  : todo2,
                  'hensoku' : todo3,
                  'midnight': todo4,
                  'holiday' : todo5,
                  'ymd': timestr,
                  'user' : ida,

            })
            print('workerror')
            errflg = True
        if( timestr == ''):
            context.update({
                  'timeerror': '日付が入力されていません',
                  'projectname1': t1,
                  'projectname2': t2,
                  'projectname3': t3,
                  'projectname4': t4,
                  'starttime': start,
                  'endtime': end,
                  'overtime': over,
                  'starttime1': request.POST.get('starttime1',''),
                  'starttime2': request.POST.get('starttime2',''),
                  'starttime3': request.POST.get('starttime3',''),
                  'starttime4': request.POST.get('starttime4',''),
                  'endtime1': request.POST.get('endtime1',''),
                  'endtime2': request.POST.get('endtime2',''),
                  'endtime3': request.POST.get('endtime3',''),
                  'endtime4': request.POST.get('endtime4',''),
                  'koutei1': value1,
                  'koutei2': value2,
                  'koutei3': value3,
                  'koutei4': value4,
                  'kouteiselect1': koutei1,
                  'kouteiselect2': koutei2,
                  'kouteiselect3': koutei3,
                  'kouteiselect4': koutei4,
                  'gyomu1': gyomu1,
                  'gyomu2': gyomu2,
                  'gyomu3': gyomu3,
                  'gyomu4': gyomu4,
                  'gyomuselect1': gyomuselect1,
                  'gyomuselect2': gyomuselect2,
                  'gyomuselect3': gyomuselect3,
                  'gyomuselect4': gyomuselect4,
                  'abs': abs,
                  'holidaykbn': hol,
                  'riyu' : riyu,
                  'chikoku' : todo0,
                  'hayade'  : todo1,
                  'soutai'  : todo2,
                  'hensoku' : todo3,
                  'midnight': todo4,
                  'holiday' : todo5,
                  'ymd': timestr,
                  'user' : ida,

            })
            errflg = True
        if (todo0 == ''):
            todo0db = 0
        else:
            todo0db = 1
        
        if (todo1 == ''):
            todo1db = 0
        else:
            todo1db = 1
            
        if (todo2 == ''):
            todo2db = 0
        else:
            todo2db = 1

        if (todo3 == ''):
            todo3db = 0
        else:
            todo3db = 1
        
        if (todo4 == ''):
            todo4db = 0
        else:
            todo4db = 1
            
        if (todo5 == ''):
            todo5db = 0
        else:
            todo5db = 1

        if(todo0db == 1 or todo1db == 1 or todo2db == 1 or todo3db == 1 or todo4db == 1 or todo5db == 1 ):
            todok = 1
        if errflg:
           return render(request, 'registration/kintai.html', context)
        
        startn = start.split(':')
        endn = end.split(':')
        starth = int(startn[0])
        endh = int(endn[0])
        if(starth >= endh):
            endh = endh + 24
        startm = int(startn[1])
        endm = int(endn[1])
        min = endm - startm
        min = min / 60
        
        worktime = endh - starth + min - float(resttime)
        worktime = round(worktime,2)
        if (worktime < 7.5):
            paidtime = math.ceil(7.5 - worktime)
        
        if (starth <= 8 and starth >= 5 and (endh >= 9 or endh <= 4)):
            morningtime = 9 - starth - startm / 60
        if(starth <= 8 and starth >= 5 and (endh < 9 or endh > 4)):
            morningtime = worktime
        
        if(startm >  endm):
            worktime = worktime - 1
        if (endh >= 22 or endh <= 5 or starth  >= 22 or starth <= 5):
        
            if (starth < 22 and starth > 5):
                if (endh >= 22):
                    midtime = endh - 22 + endm / 60
                if (endh <= 5):
                    midtime = endh + 2 + endm / 60
            else:
                if (starth >= 22 or starth <= 5):
                    if ( endh <= 5 and starth < 22):
                        midtime = endh - starth + min
                    if ( endh <= 5 and starth >= 22):
                        midtime = endh + 24 - starth - min
                    if ( end > 5 and  start < 22):
                        midtime = 5 - starth - min
                    if ( end > 5 and start >= 22):
                        midtime = 24 - starth + 4 - startm / 60
            if (worktime > 7.5):
                    midover = midtime
                    
            if (todo4 == ''):
                context.update({
                  'miderror': '深夜有が選択されていません',
                  'starttime': start,
                  'endtime': end,
                  'overtime': over,
                  'projectname1': t1,
                  'projectname2': t2,
                  'projectname3': t3,
                  'projectname4': t4,
                  'starttime1': request.POST.get('starttime1',''),
                  'starttime2': request.POST.get('starttime2',''),
                  'starttime3': request.POST.get('starttime3',''),
                  'starttime4': request.POST.get('starttime4',''),
                  'endtime1': request.POST.get('endtime1',''),
                  'endtime2': request.POST.get('endtime2',''),
                  'endtime3': request.POST.get('endtime3',''),
                  'endtime4': request.POST.get('endtime4',''),
                  'resttime1': request.POST.get('resttime1',''),
                  'resttime2': request.POST.get('resttime2',''),
                  'resttime3': request.POST.get('resttime3',''),
                  'resttime4': request.POST.get('resttime4',''),
                  'koutei1': value1,
                  'koutei2': value2,
                  'koutei3': value3,
                  'koutei4': value4,
                  'kouteiselect1': koutei1,
                  'kouteiselect2': koutei2,
                  'kouteiselect3': koutei3,
                  'kouteiselect4': koutei4,
                  'gyomu1': gyomu1,
                  'gyomu2': gyomu2,
                  'gyomu3': gyomu3,
                  'gyomu4': gyomu4,
                  'gyomuselect1': gyomuselect1,
                  'gyomuselect2': gyomuselect2,
                  'gyomuselect3': gyomuselect3,
                  'gyomuselect4': gyomuselect4,
                  'abs': abs,
                  'holidaykbn': hol,
                  'riyu' : riyu,
                  'chikoku' : todo0,
                  'hayade'  : todo1,
                  'soutai'  : todo2,
                  'hensoku' : todo3,
                  'midnight': todo4,
                  'holiday' : todo5,
                  'ymd': timestr,
                  'user' : ida,
                })
                return render(request, 'registration/kintai.html', context)


        
        #DB格納(出勤)
        b = kintai_touroku_info(syaincd=ida,syainname = name, 
        ymd=timestr,starttime=start,endtime=end,worktime=worktime,overtime=over,
        resttime=resttime, attkbn=absdb, holidaykbn=holdb, holidayriyu=riyu,
        todoke_tikoku=todo0db, todoke_soutai=todo1db, todoke_midnight=todo2db, todoke_hayade=todo3db, 
        todoke_irregular=todo4db, todoke_holiwork=todo5db, todokekbn=todok,mntime = midtime,mnovertime = midover,
        paidtime = paidtime,
        projectname1 = t1,kouteiname1 = koutei1, workname1 = gyomuselect1, start1 = starttime1, end1 = endtime1, rest1 = resttime1,
        projectname2 = t2,kouteiname2 = koutei2, workname2 = gyomuselect2, start2 = starttime2, end2 = endtime2, rest2 = resttime2,
        projectname3 = t3,kouteiname3 = koutei3, workname3 = gyomuselect3, start3 = starttime3, end3 = endtime3, rest3 = resttime3,
        projectname4 = t4,kouteiname4 = koutei4, workname4 = gyomuselect4, start4 = starttime4, end4 = endtime4, rest4 = resttime4,
        projectcd1 = projectcd1,projectcd2 = projectcd2,projectcd3 = projectcd3,projectcd4 = projectcd4,
        kouteicd1 = kouteicd1,kouteicd2 = kouteicd2,kouteicd3 = kouteicd3,kouteicd4 = kouteicd4,
        workcd1 = workcd1,workcd2 = workcd2,workcd3 = workcd3,workcd4 = workcd4)
    #DB格納(欠勤)
    else:
        start = '00:00'
        end = '00:00'
        worktime= 0.0
        over = 0.0
        b = kintai_touroku_info(syaincd=ida,syainname = name, 
        ymd=timestr, starttime=start,endtime=end,worktime=worktime,overtime=over,attkbn=absdb, holidaykbn=holdb, holidayriyu=riyu,
        start1 = starttime1, end1 = endtime1,
        start2 = starttime2, end2 = endtime2,
        start3 = starttime3, end3 = endtime3,
        start4 = starttime4, end4 = endtime4,
        todokekbn=todok)

    listf = kintai_touroku_info.objects.filter(ymd = timestr)
    
   
    if (len(listf) == 0):
       b.save()
    else:
       b =  kintai_touroku_info.objects.filter(ymd = timestr)
       b.update(starttime=start,endtime=end,worktime=worktime,overtime=over,
       resttime=resttime,attkbn=absdb, holidaykbn=holdb, holidayriyu=riyu,
       todoke_tikoku=todo0db, todoke_soutai=todo1db, todoke_midnight=todo2db, todoke_hayade=todo3db, 
       todoke_irregular=todo4db, todoke_holiwork=todo5db, todokekbn=todok,
       projectname1 = t1,kouteiname1 = koutei1, workname1 = gyomuselect1, start1 = starttime1, end1 = endtime1, rest1 = resttime1,
       projectname2 = t2,kouteiname2 = koutei2, workname2 = gyomuselect2, start2 = starttime2, end2 = endtime2, rest2 = resttime2,
       projectname3 = t3,kouteiname3 = koutei3, workname3 = gyomuselect3, start3 = starttime3, end3 = endtime3, rest3 = resttime3,
       projectname4 = t4,kouteiname4 = koutei4, workname4 = gyomuselect4, start4 = starttime4, end4 = endtime4, rest4 = resttime4,
       projectcd1 = projectcd1,projectcd2 = projectcd2,projectcd3 = projectcd3,projectcd4 = projectcd4,
       kouteicd1 = kouteicd1,kouteicd2 = kouteicd2,kouteicd3 = kouteicd3,kouteicd4 = kouteicd4,
       workcd1 = workcd1,workcd2 = workcd2,workcd3 = workcd3,workcd4 = workcd4)
     
    context = {
                  'message': '勤怠登録しました',
                  'starttime':start, 'endtime': end,'worktime': worktime,'overtime': over,'resttime': resttime,
                  'ymd': timestr,'projectname1': t1,'projectname2': t2,'projectname3': t3,'projectname4': t4,
                  'starttime1': request.POST.get('starttime1',''),'starttime2': request.POST.get('starttime2',''),
                  'starttime3': request.POST.get('starttime3',''),'starttime4': request.POST.get('starttime4',''),
                  'endtime1': request.POST.get('endtime1',''),'endtime2': request.POST.get('endtime2',''),
                  'endtime3': request.POST.get('endtime3',''),'endtime4': request.POST.get('endtime4',''),
                  'resttime1': request.POST.get('resttime1',''), 'resttime2': request.POST.get('resttime2',''),
                  'resttime3': request.POST.get('resttime3',''), 'resttime4': request.POST.get('resttime4',''),
                  'koutei1': value1,'koutei2': value2, 'koutei3': value3,'koutei4': value4,
                  'kouteiselect1': koutei1,'kouteiselect2': koutei2, 'kouteiselect3': koutei3, 'kouteiselect4': koutei4,
                  'gyomu1': gyomu1,'gyomu2': gyomu2,'gyomu3': gyomu3, 'gyomu4': gyomu4,
                  'gyomuselect1': gyomuselect1,'gyomuselect2': gyomuselect2,'gyomuselect3': gyomuselect3,'gyomuselect4': gyomuselect4,
                  'abs': abs, 'holidaykbn': hol, 'riyu' : riyu,
                  'chikoku' : todo0,'hayade'  : todo1,'soutai'  : todo2,'hensoku' : todo3,'midnight': todo4, 'holiday' : todo5,
                  'user' : ida,

            }
    return render(request, 'registration/kintai.html', context)


#勤怠入力画面ロード   
def kintaiload(request):
    template = loader.get_template('registration/kintai.html')
    id = request.session.get('User','')
    nowyear = str(datetime.date.today().year)
    nowmonth = str(format(datetime.date.today().month,'02'))
    nowday = str(format(datetime.date.today().day,'02'))
    nowdate = nowyear + "-" +  nowmonth +  "-" + nowday
    monthyear = request.POST.get('dateselect',nowdate)

    listf = kintai_touroku_info.objects.filter(ymd = monthyear, syaincd = id)
    if (len(listf) == 1):

        attkbn = listf[0].attkbn
        holidaykbn = listf[0].holidaykbn
        holidayriyu = listf[0].holidayriyu
        start = str(listf[0].starttime)
        start = start[:5]
        end = str(listf[0].endtime)
        end = end[:5]
        start1 = str(listf[0].start1)
        start1 = start1[:5]
        end1 = str(listf[0].end1)
        end1 = end1[:5]
        start2 = str(listf[0].start2)
        start2 = start2[:5]
        end2 = str(listf[0].end2)
        end2 = end2[:5]
        start3 = str(listf[0].start3)
        start3 = start3[:5]
        end3 = str(listf[0].end3)
        end3 = end3[:5]
        start4 = str(listf[0].start4)
        start4 = start4[:5]
        end4 = str(listf[0].end4)
        end4 = end4[:5]
        todo0 = listf[0].todoke_tikoku
        todo1 = listf[0].todoke_soutai
        todo2 = listf[0].todoke_midnight
        todo3 = listf[0].todoke_hayade
        todo4 = listf[0].todoke_irregular
        todo5 = listf[0].todoke_holiwork
        koutei1 = project_work.objects.filter(projectname=listf[0].projectname1).distinct('kouteiname')
        koutei2 = project_work.objects.filter(projectname=listf[0].projectname2).distinct('kouteiname')
        koutei3 = project_work.objects.filter(projectname=listf[0].projectname3).distinct('kouteiname')
        koutei4 = project_work.objects.filter(projectname=listf[0].projectname4).distinct('kouteiname')
        gyomu1 = project_work.objects.filter(projectname=listf[0].projectname1,kouteiname=listf[0].kouteiname1)
        gyomu2 = project_work.objects.filter(projectname=listf[0].projectname2,kouteiname=listf[0].kouteiname2)
        gyomu3 = project_work.objects.filter(projectname=listf[0].projectname3,kouteiname=listf[0].kouteiname3)
        gyomu4 = project_work.objects.filter(projectname=listf[0].projectname4,kouteiname=listf[0].kouteiname4)
        
        if (attkbn == 0 ):
            attkbn = '出勤'
        if (attkbn == 1 ):
            attkbn = '欠勤'
        if (holidaykbn == 0 ):
            holidaykbn = '取得なし'
        if (holidaykbn == 1 ):
            holidaykbn = '有給休暇'
        if (holidaykbn == 2 ):
            holidaykbn = '特休・その他休暇'
        if (holidaykbn == 3 ):
            holidaykbn = '代休'
        if (holidaykbn == 4 ):
            holidaykbn = 'その他'
        if (holidaykbn == 5 ):
            holidaykbn = '半休等'
        if (todo0 == 1 ):
            todo0 = '遅刻'
        else:
            todo0 = ''
        if (todo1 == 1 ):
            todo1 = '早出有'
        else:
            todo1 = ''
        if (todo2 == 1 ):
            todo2 = '早退'
        else:
            todo2 = ''
        if (todo3 == 1 ):
            todo3 = '変則勤務'
        else:
            todo3 = ''
        if (todo4 == 1 ):
            todo4 = '深夜有'
        else:
            todo4 = ''
        if (todo5 == 1 ):
            todo5 = '休日出勤'
        else:
            todo5 = ''
        context = {
                      'starttime':start, 'endtime': end,
                      'worktime': listf[0].worktime,'overtime': listf[0].overtime,
                      'resttime': listf[0].resttime,'ymd':      monthyear,
                      'projectname1':listf[0].projectname1, 'projectname2':listf[0].projectname2,
                      'projectname3':listf[0].projectname3, 'projectname4':listf[0].projectname4,
                      'koutei1': koutei1, 'koutei2': koutei2,'koutei3': koutei3,'koutei4': koutei4,
                      'kouteiselect1': listf[0].kouteiname1, 'kouteiselect2': listf[0].kouteiname2,'kouteiselect3': listf[0].kouteiname3, 'kouteiselect4': listf[0].kouteiname4,
                      'gyomu1':   gyomu1,'gyomu2':   gyomu2, 'gyomu3':   gyomu3, 'gyomu4':   gyomu4,
                      'gyomuselect1': listf[0].workname1, 'gyomuselect2': listf[0].workname2,
                      'gyomuselect3': listf[0].workname3, 'gyomuselect4': listf[0].workname4,
                      'starttime1':start1, 'endtime1': end1, 'resttime1':   listf[0].rest1,
                      'starttime2':start2,'endtime2': end2,  'resttime2':   listf[0].rest2,
                      'starttime3':start3,'endtime3': end3,  'resttime3':   listf[0].rest3,
                      'starttime4':start4,'endtime4': end4,  'resttime4':   listf[0].rest4,
                      'holidaykbn': holidaykbn, 'abs': attkbn,  'riyu': holidayriyu,
                      'chikoku': todo0, 'hayade': todo1,'soutai': todo2, 'hensoku': todo3, 'midnight': todo4, 'holiday': todo5,
                      'user' : id,
                }      
        return render(request, 'registration/kintai.html', context)
    context = {
                      'ymd':      monthyear,
                      'user' : id,
                }      
    return render(request, 'registration/kintai.html', context)

class UserCreate(generic.CreateView):
     
     template_name = 'customLogin/user_create.html'
     form_class = CustomUserCreateForm
     def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super().get(request, **kwargs)

     def form_valid(self, form):
        # 仮登録
        user = form.save(commit=False)
        #user.is_active = False
        #user.save()
        print("メール")
        #account_sid = 'VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        #auth_token = 'TAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        #client = Client(account_sid, auth_token)
        #verification = client.verify \
        #             .services('VAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') \
        #             .verifications \
        #             .create(to='j1409032@yahoo.co.jp', channel='sms')
        #print(verification.sid)

        # メール送信
        current_site = get_current_site(self.request)
        domain = current_site.domain
        #breakpoint()
        context = {
            'protocol': 'https' if self.request.is_secure() else 'http',
            'domain': '127.0.0.1:8000',
            'token': dumps(user.pk),
            'user': user
        }
        subject_template = get_template('customLogin/mail/subject.txt')
        message_template = get_template('customLogin/mail/message.txt')
        subject = subject_template.render(context)
        message = message_template.render(context)
        #breakpoint()
        gmail_account = "j1409032@gmail.com"
        gmail_password = "mamoka1212"
        # メールの送信先 --- (*2)
        mail_to = "j1409032@yahoo.co.jp"        
        encoding = 'utf-8'
        msg = MIMEMultipart()
        msg["Subject"] = Header(subject, encoding)
        msg["To"] = mail_to
        msg["From"] = gmail_account
        msg.attach(MIMEText(message, 'plain', encoding))
        
        # Gmailに接続 --- (*6)
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
        context=ssl.create_default_context())
        server.login(gmail_account, gmail_password)
        server.send_message(msg) # メールの送信
        server.quit()

        #user.email_user(subject, message)
        return redirect('user_create_done')
        
        
        
class UserCreateComplete(generic.TemplateView):
    """本登録完了"""
    template_name = 'customLogin/user_create_complete.html'
    timeout_seconds = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60 * 60 * 24)  # デフォルトでは1日以内

    def get(self, request, **kwargs):
        """tokenが正しければ本登録."""
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')

        token = kwargs.get('token')
        try:
            user_pk = loads(token, max_age=self.timeout_seconds)

        # 期限切れ
        except SignatureExpired:
            return HttpResponseBadRequest()

        # tokenが間違っている
        except BadSignature:
            return HttpResponseBadRequest()

        # tokenは問題なし
        try:
            #user = User.objects.get(pk=user_pk)
            user = request.session.get('User','')
        except User.DoenNotExist:
            return HttpResponseBadRequest()

        if not user:
            # 問題なければ本登録とする
            #user.is_active = True
            #user.is_staff = True
            #user.is_superuser = True
            #user.save()

            # QRコード生成
            request.session["img"] = utils.get_image_b64(utils.get_auth_url('j1409032@gmail.com', utils.get_secret(user)))

            return super().get(request, **kwargs)

        return HttpResponseBadRequest()


@login_required()
@transaction.atomic
def display_qrcode(request):
    user_id = 'j1409032@yahoo.co.jp'
    secret = get_secret()
    
#    try:
#        two_auth = TwoAuth.objects.get(fk_user=request.user)
#        two_auth.secret_key = secret
#    except TwoAuth.DoesNotExist:
#        two_auth = TwoAuth(fk_user=request.user, secret_key=secret)
    
    two_auth.save()

    return JsonResponse({
        'img':  get_image_b64(get_auth_url(user_id, secret)),
    })

class CustomLoginView(LoginView):
    """ログイン"""
    form_class = CustomLoginForm
    template_name = 'customLogin/user_login.html'

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super().get(request, **kwargs)

class UserCreateDone(generic.TemplateView):
    print("仮登録")
    template_name = 'customLogin/user_create_done.html'
    
    def get(self, request, **kwargs):
        #breakpoint()
        #if request.user.is_authenticated:
            
       return HttpResponseRedirect('/')
       # return super().get(request, **kwargs)

class OTPAdmin(OTPAdminSite):
    pass


admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)
