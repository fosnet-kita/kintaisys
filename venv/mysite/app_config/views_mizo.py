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
from .forms import CustomUserCreateForm
from django.views import generic
import datetime
import calendar
import locale
# Create your views here.



def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render( None, request))
    
def project(request):
    template = loader.get_template('registration/projecttouroku.html')
    list =  project_work.objects.all().distinct('projectname')
    cont = {
        'pro': list,
    }
    return render(request, 'registration/projecttouroku.html', context=cont)
    
def kintai(request):
    template = loader.get_template('registration/kintai.html')
    
    return HttpResponse(template.render( None, request))
    
def login(request):
    template = loader.get_template('registration/login.html')

    
    return HttpResponse(template.render( None, request))
    
def password(request):
    template = loader.get_template('registration/password_change.html')
   
    return HttpResponse(template.render( None, request))
    
def passwordchange(request):
    template = loader.get_template('registration/password_change.html')
    
    id = request.POST['UserId']
    passw =request.POST['Password']
    passn =request.POST['APassword']
    passk =request.POST['KPassword']
    list =  syain_info.objects.all()
    print("新しい" + passn)
    print("確認"  +passk)
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
    for i in range(len(list)):
      syaincd1=list[i].syaincd
      password1=list[i].password
      print(list[i].syaincd)
      print(list[i].password)
      if (id == syaincd1 and passw == password1):
         if(passn == passk):
           p =  syain_info.objects.filter(syaincd = syaincd1)
           print(p)
           p.update(password = passn)
           return render(request, 'registration/login.html')
    context.update({
              'matcherror': 'ユーザーid,パスワードが違います',
        })
    return render(request, 'registration/password_change.html', context)
    
def koutuhilist(request):
    template = loader.get_template('registration/koutuhi_itiran.html')
    data = trans_info.objects.all()
    print(data)
    my_dict2 = {
        'data':  data
    }
    return render(request, 'registration/koutuhi_itiran.html', my_dict2)
    
def koutuhi(request):
    template = loader.get_template('registration/koutuhi.html')
    list =  torihikisaki_list.objects.all()
    if request.method == 'POST':
      tablesumi = request.POST['tablesumi']
      kbn = request.POST['tourokukbn']
      date = datetime.date.today()
      
      
      
      homon = request.POST['homon']
      trans = request.POST['transport']
      start = request.POST['startdate']
      end = request.POST['enddate']
      kamoku = request.POST['kamoku']
      syudan = request.POST['syudan']
      k_seikyu = request.POST.getlist('seikyu')
      print(k_seikyu)
      seisan = request.POST['seisan']
      startstr = start[:4] + '-' + start[4:6] + '-' + start[6:]
      endstr = end[:4] + '-' + end[4:6] + '-' + end[6:]
      if( homon == '' or trans == '' or  start == '' or  end == '' or kamoku == '' or syudan == ''):
          context = {
                  'error': '入力されていない項目があります',
            }
          return render(request, 'registration/koutuhi.html', context)      
      
      
      else:
          print(kbn)
          print(date)
          print(homon)
          print(trans)
          print(seisan)
          b = trans_info(tourokukbn = kbn,tourokudate = date,tourokuno = '11', startdate = startstr, enddate = endstr,kamoku = kamoku, syudan = syudan,transport = trans, k_seikyu = '0', seisan_kbn = seisan)
          b.save()
          context = {
                  'kbn': kbn ,
                  'date': date,
                  'homon': homon,
                  'trans': trans,
            }
          return render(request, 'registration/koutuhi.html', context)
    cus = {
            'cus': list,
      }
    return render(request, 'registration/koutuhi.html', cus)
    
def appearrance(request):
    template = loader.get_template('registration/syukketsusentaku.html')
    return HttpResponse(template.render( None, request))
    
def output(request):
    template = loader.get_template('registration/output_ichiran.html')
    
    return HttpResponse(template.render( None, request))

def output2(request):
    
    datelist = []
    weeklist = []
    monthyear =request.POST['monthselect']
    year = monthyear[:4]
    month = monthyear[5:7]
    monthz = monthyear[5:6]

    if (monthz  == '0'):
       month = monthyear[6:7]
    print(year)
    print(month)
    month_range = calendar.monthrange(int(year), int(month))
    list =  kintai_touroku_info.objects.all()
    mmm = ''
    listmmm = []

    
    
    listf = kintai_touroku_info.objects.filter(ymd__month = month).order_by('ymd')
    listf2 = []
    print(list)
    print(listf)
    
    # 月数分ループ
    for i in range(1,month_range[1] + 1):
       listmmm.append(i)
    
    # 月数分ループ
    for i in range(1,month_range[1] + 1):
        # DB格納日数分ループ
        for j in range(len(listf)):
            mmmm = str(listf[j].ymd)
            mmm = str(mmmm[8:10])
            

            # 出力日付 = DB格納日付 ?
            if not i in int(mmm):
                listmmm.append(listf[j])# DBの日付格納
            else:
                listmmm.append(i)  # 出力日付格納
               
               
               
               
               
                print(listf[j].todoke_tikoku)
                   
                if (listf[j].holidayriyu  == '0'):
                   listf[j].holidayriyu = str(listf[j].holidayriyu)
                   listf[j].holidayriyu = ""
                   
                   
                if (listf[j].todoke_tikoku  == 0):
                   listf[j].todoke_tikoku = str(listf[j].todoke_tikoku)
                   listf[j].todoke_tikoku = ""
                   
                if (listf[j].todoke_soutai  == 0):
                   listf[j].todoke_soutai = str(listf[j].todoke_soutai)
                   listf[j].todoke_soutai = ""
                   
                if (listf[j].todoke_midnight  == 0):
                   listf[j].todoke_midnight = str(listf[j].todoke_midnight)
                   listf[j].todoke_midnight = ""
                   
                if (listf[j].todoke_hayade  == 0):
                   listf[j].todoke_hayade = str(listf[j].todoke_hayade)
                   listf[j].todoke_hayade = ""
                   
                if (listf[j].todoke_irregular  == 0):
                   listf[j].todoke_irregular = str(listf[j].todoke_irregular)
                   listf[j].todoke_irregular = ""
                   
                if (listf[j].todoke_holiwork  == 0):
                   listf[j].todoke_holiwork = str(listf[j].todoke_holiwork)
                   listf[j].todoke_holiwork = ""
                   
                if (listf[j].todoke_tikoku  == 1):
                   listf[j].todoke_tikoku = str(listf[j].todoke_tikoku)
                   listf[j].todoke_tikoku = "遅刻"
                   
                if (listf[j].todoke_soutai  == 1):
                   listf[j].todoke_soutai = str(listf[j].todoke_soutai)
                   listf[j].todoke_soutai = "早退"
                   
                if (listf[j].todoke_midnight  == 1):
                   listf[j].todoke_midnight = str(listf[j].todoke_midnight)
                   listf[j].todoke_midnight = "深夜"
                   
                if (listf[j].todoke_hayade  == 1):
                   listf[j].todoke_hayade = str(listf[j].todoke_hayade)
                   listf[j].todoke_hayade = "早出"
                   
                if (listf[j].todoke_irregular  == 1):
                   listf[j].todoke_irregular = str(listf[j].todoke_irregular)
                   listf[j].todoke_irregular = "変則出勤"
                   
                if (listf[j].todoke_holiwork  == 1):
                   listf[j].todoke_holiwork = str(listf[j].todoke_holiwork)
                   listf[j].todoke_holiwork = "休日出勤"
                   
    l = []
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    ww = float(0.0);
    sumwork = float(0.0);
    overwork = float(0.0);
    resttime = float(0.0);
    days = 0;
    
    for k in listf:
        sumwork = sumwork + float(k.worktime)
        overwork = overwork + float(k.overtime)
        resttime = resttime + float(k.resttime)
        
        weekday = k.ymd.weekday()
        weekday_name = calendar.day_name[weekday]
        
        days = days + 1

    list_of_ids = []
    for i in range(1,month_range[1] + 1):    
         print(str(days) + 'aaa') 
    
    print(i - days)
    days2 = i - days
    for s in range(1,month_range[1] + 1):
      if s < 10:
        list_of_ids.append('0' + str(s))
      else:
        list_of_ids.append(str(s))
    nolist = []
    for t in range(len(list_of_ids)):

        if not list_of_ids[t] in listmmm:
           nolist.append(list_of_ids[t])
           
           
    print(nolist)
    for u in range(len(nolist)):
         if nolist[u].startswith('0'):
           nolist[u] = nolist[u].replace('0','')
         nolist[u] = int(nolist[u])
         
    nodisp = int(i) - days
    
    print(sumwork)

    
    weekday_jp = ['月','火','水','木','金','土','日']

    print(range(1,month_range[1] + 1))
    print('aaa')
    
    context = {
         'monthselect' : monthyear,
         'listaaaa': listf,
         'listbbbb': nolist,
         'sumwork': sumwork,
         'overwork': overwork,
         'resttime': resttime,
        #'endtime': list.endtime,
        #'worktime': list.worktime,
        #'resttime': list.resttime,
        #'overtime': list.overtime,
    }
    return render(request, 'registration/output_ichiran.html', context)
def kintailogin(request):
    template = loader.get_template('registration/kintai.html')
    id = request.POST['User']
    passw =request.POST['Pass']
    list =  syain_info.objects.all()
    request.session['User'] = request.POST['User']
    print(passw)
    print(id)
    for i in range(len(list)):
      syaincd=list[i].syaincd
      password=list[i].password
      print(list[i].syaincd)
      print(list[i].password)
      if (id == syaincd and passw == password):
         context = {
                   'syaincd':id,
              }
         return render(request, 'registration/kintai.html', context)
    #if (pass==pass)
    #print(request.POST['touroku22'])
    context = {
              'error': 'ユーザーIDまたはパスワードが違います',
        }
    return render(request, 'registration/login.html', context)
    
    
def kintaiabs(request):
    template = loader.get_template('registration/kintai.html')
    request.session['Absentkbn'] = request.POST['Absentkbn']
    request.session['Holidaykbn'] = request.POST['Holidaykbn']
    kbn = request.POST['Holidaykbn']
    abs = request.POST['Absentkbn']
    request.session['Riyu'] = request.POST['Riyu']
    riyu = request.POST['Riyu']
    print("riyu" + riyu)
    print(request.POST.getlist('Todokede'))
    request.session['Todokede0'] = request.POST['Todokede0']
    request.session['Todokede1'] = request.POST['Todokede1']
    request.session['Todokede2'] = request.POST['Todokede2']
    request.session['Todokede3'] = request.POST['Todokede3']
    request.session['Todokede4'] = request.POST['Todokede4']
    request.session['Todokede5'] = request.POST['Todokede5']
    if(abs == '1'  and kbn == ''):
       context1 = {
                'error': '休暇区分を選択してください',
          }
       return render(request, 'registration/syukketsusentaku.html', context1)
    if(abs == '1'  and riyu == ''):
       context2 = {
                'error': '休暇理由を選択してください',
          }
       return render(request, 'registration/syukketsusentaku.html', context2)
    
    
    
    return HttpResponse(template.render( None, request))
      
def kintaiproject(request):
    template = loader.get_template('registration/kintai.html')

    value = project_work.objects.all().distinct('workname')
    value1 = project_work.objects.filter(projectname=request.POST['touroku1']).distinct('kouteiname')
    value2 = project_work.objects.filter(projectname=request.POST['touroku2']).distinct('kouteiname')
    value3 = project_work.objects.filter(projectname=request.POST['touroku3']).distinct('kouteiname')
    t222 = request.session.get('touroku1','')
    k1 = request.session.get('kouteiname1','')
    #koutei = request.POST.get('kouteiname1', '')
    print("t1 aa "   + k1)
    
    
    
    touroku1 = request.POST['touroku1']
    touroku2 = request.POST['touroku2']
    touroku3 = request.POST['touroku3']
    print(touroku1)
    print(touroku2)
    print(touroku3)
    request.session['touroku1'] = request.POST['touroku1']
    request.session['touroku2'] = request.POST['touroku2']
    request.session['touroku3'] = request.POST['touroku3']
    #kou1 = value.get(projectname = touroku )
    #kou2 = project_work.kouteiname
    #print(touroku)
    if request.method == 'POST':
      #touroku = request.POST['touroku22']
      context = {
                'projectname1': touroku1,
                'projectname2': touroku2,
                'projectname3': touroku3,
                'koutei1': value1,
                'koutei2': value2,
                'koutei3': value3,
                #'gyomu1': value,
                #'gyomu2': value,
          }
      return render(request, 'registration/kintai.html', context)
    return HttpResponse(template.render( None, request))
    
def kintaiwork(request):
    template = loader.get_template('registration/kintai.html')
    t1 = request.session.get('touroku1','')
    #t1 = request.POST['touroku1']
    #t2 = request.session.get('touroku2','')
    t222 = request.session.get('touroku13','')
    k1 = request.session.get('kouteiname1','')
    koutei = request.POST.get('kouteiname1', '')
    print("t1"+  request.POST['kouteiname1']  + " aa " + t1)
    #value = ('kouteiname','workname')
    value1 = project_work.objects.filter(projectname=t1).distinct('kouteiname')
    value22 = project_work.objects.filter(projectname=t1,kouteiname=koutei)
    #value = project_work.objects.all()
    #value1 = project_work.objects.filter(projectname=t1).distinct('kouteiname')
    #value2 = project_work.objects.filter(projectname=t2).distinct('kouteiname')
    context = {
                'projectname1': t1,
    #            'projectname2': t2,
                'koutei1': value1,
    #            'koutei2': value2,
                'gyomu1': value22,
                #'gyomu2': value,
         }
    #return render(request, 'registration/kintai.html', context)
    
#勤怠登録押下、工程選択時    
def kintaitouroku(request):
    template = loader.get_template('registration/kintai.html')
    btt = request.POST.get('btnExecH','')
    print(request)
    print(btt)
    start1 = request.POST['starttime1']
    end1 = request.POST['endtime1']
    start = request.POST.get('starttime', '')
    print(start)
  
    
    
    
    if(btt != '勤怠登録'):
        t1 = request.session.get('touroku1','')
        #t1 = request.POST['touroku1']
        t2 = request.session.get('touroku2','')
        t222 = request.session.get('touroku13','')
        k1 = request.session.get('kouteiname1','')
        koutei = request.POST.get('kouteiname1', '')
        #print("t1"+  request.POST['kouteiname1']  + " aa " + t1)
        value1 = project_work.objects.filter(projectname=t1).distinct('kouteiname')
        value2 = project_work.objects.filter(projectname=t2).distinct('kouteiname')
        value22 = project_work.objects.filter(projectname=t1,kouteiname=koutei)
        print(request.POST.get('starttime',''))
        context = {
                    'starttime1': start1,
                    'endtime1': end1,
                    'projectname1': t1,
                    'projectname2': t2,
                    'koutei1': value1,
                    'kouteiselect': request.POST['kouteiname1'],
                    'koutei2': value2,
                    'gyomu1': value22,
                    #'gyomu2': value,
             }
        return render(request, 'registration/kintai.html', context)
        #return redirect('kintaitouroku')
        #return render_to_response('registration/kintai.html')
    ida = request.session.get('User','')
    absn = request.session.get('Absentkbn','')
    
    hol = request.session.get('Holidaykbn','')
    print(btt)
    todo0 = int(request.session.get('Todokede0',''))
    todo1 = int(request.session.get('Todokede1',''))
    todo2 = int(request.session.get('Todokede2',''))
    todo3 = int(request.session.get('Todokede3',''))
    todo4 = int(request.session.get('Todokede4',''))
    todo5 = int(request.session.get('Todokede5',''))
    t1 = request.session.get('touroku1','')
    t2 = request.session.get('touroku2','')
    k1 = request.session.get('kouteiname1','')
    value1 = project_work.objects.filter(projectname=t1).distinct('kouteiname')
    name = syain_info.objects.get(syaincd=ida)
    
       
    if(hol == ''):
       hol = 0
    print(absn)
    print(k1)
    print(k1)
    print(name.syainname)
    print("aa   " + ida)
    #project = request.POST['projectname1']
    project = request.POST.get('projectname1', '')
    print(project)
    
    #date = request.POST['date']
    #year = request.POST['year']
    #month = request.POST['month']
    #week = request.POST['week']
    #timestr = year + '-' + month + '-' + date;
    timestr = request.POST['dateselect']
    todok = 0
    
    
    end = request.POST.get('endtime', '')
    over = request.POST.get('overtime', '')
    koutei = request.POST.get('kouteiname1', '')
    if(absn == ''):
        context = {
                  'error': '出欠選択をしてください',
                  'projectname1': t1,
                  'projectname2': t2,
                  'koutei1': value1,
        }
        return render(request, 'registration/kintai.html', context)
    
    if(absn == 0):
        
        if(project == 'None'):
            context = {
                  'error': 'プロジェクト登録をしてください',
                  #'projectname1': t1,
                  #'projectname2': t2,
                  #'koutei1': value1,
            }
            return render(request, 'registration/kintai.html', context)
        if( start == ''):
            context = {
                  'error': '開始時刻が入力されていません',
                  'projectname1': t1,
                  'projectname2': t2,
                  'koutei1': value1,
            }
            return render(request, 'registration/kintai.html', context)
        if( end == ''  ):
            context = {
                  'error': '終了時刻が入力されていません',
                  'projectname1': t1,
                  'projectname2': t2,
                  'koutei1': value1,
            }
            return render(request, 'registration/kintai.html', context)
            
        if( koutei == '' ):
            context = {
                  'error': '工程が入力されていません',
                  'projectname1': t1,
                  'projectname2': t2,
                  'koutei1': value1,
            }
            return render(request, 'registration/kintai.html', context)
        if( work == ''):
            context = {
                  'error': '業務が入力されていません',
                  'projectname1': t1,
                  'projectname2': t2,
                  'koutei1': value1,
            }
            return render(request, 'registration/kintai.html', context)
        koutei222222 = request.POST['kouteiname1']
        work = request.POST.get('workname1', '')
        rest = request.POST.get('resttime1', '')
        worktime = 0.0
        print("aaaaa   " + koutei222222)
        print("bb   " + start)
        print("cc   " + end)
        startn = start.split(':')
        endn = end.split(':')
        starth = int(startn[0])
        endh = int(endn[0])
        print(starth)
        print(endh)
        startm = int(startn[1])
        endm = int(endn[1])
        min = startm - endm
        min = abs(min) / 60
        worktime = endh - starth + min - float(rest)
        worktime = round(worktime,2)
        if(startm >  endm):
           worktime = worktime - 1
        
        print(worktime)
        
        if(todo0 == 1 or todo1 == 1 or todo2 == 1 or todo3 == 1 or todo4 == 1 or todo5 == 1 ):
           todok = 1
        b = kintai_touroku_info(syaincd=ida,syainname = name.syainname, ymd=timestr,starttime=start,endtime=end,worktime=worktime,overtime=over,resttime=rest, attkbn=absn, holidaykbn=hol, todoke_tikoku=todo0, todoke_soutai=todo1, todoke_midnight=todo2, todoke_hayade=todo3, todoke_irregular=todo4, todoke_holiwork=todo5, todokekbn=todok)
    else:
        holriyu = request.session.get('Riyu','')
        print(holriyu)
        b = kintai_touroku_info(syaincd=ida,syainname = name.syainname, ymd=timestr, attkbn=absn, holidaykbn=hol,holidayriyu=holriyu, todoke_tikoku=todo0, todoke_soutai=todo1, todoke_midnight=todo2, todoke_hayade=todo3, todoke_irregular=todo4, todoke_holiwork=todo5, todokekbn=todok)
    b.save()
     
    context = {
                  'message': '勤怠登録しました',
            }
    return render(request, 'registration/kintai.html', context)
    
