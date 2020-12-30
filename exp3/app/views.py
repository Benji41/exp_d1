from django.shortcuts import render
#from  django.http import HttpResponse
# Create your views here.
def index(request):
    dicto ={
        'usuario':'Benjamin!'
    }
    # return HttpResponse('<h1>Hola mundo!</h1>')
    return render(request,'app/index.html',context=dicto)
    

def base(request):
    #return HttpResponse('<h1>Hola mundo en base!</h1>')
    return render(request,'app/base.html')