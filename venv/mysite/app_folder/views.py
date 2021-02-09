from django.shortcuts import render
from .models import SampleDB
from django.http import HttpResponse
from django.template import loader

#class SampleView(View):  
#    def get(self, request, *args, **kwargs):  
#        return render(request, 'app_folder/top_page.html')
#top_page = SampleView.as_view()
# Create your views here.

def info(request):
    infodata = SampleDB.objects.all()
    infodata2 = SampleDB.objects.values()
    my_dict2 = {
        'title':'テスト',
        'val':infodata,
        'val2':infodata2,
    }
    return render(request, 'registration/projecttouroku.html',my_dict2)
