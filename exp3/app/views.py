from django.shortcuts import render
from app.models import Owner,AccessRecord,Cat
#from  django.http import HttpResponse
# Create your views here.
def index(request):
    ownerList= AccessRecord.objects.order_by('arDate')
    dateOwner = {
        'acc_rec':ownerList
    }
    dicto ={
        'usuario':'Benjamin!'
    }
    # return HttpResponse('<h1>Hola mundo!</h1>')
    return render(request,'app/index.html',context=dateOwner)
    

def base(request):
    #return HttpResponse('<h1>Hola mundo en base!</h1>')
    return render(request,'app/base.html')