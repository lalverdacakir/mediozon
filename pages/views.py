from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'anasayfa.html')
def bize_ulasin(request):
    return render(request,'bize-ulasin.html')
def hakkimizda(request):
    return render(request,'hakkimizda.html')
def ozon_hakkinda(request):
    return render(request,'ozon-hakkinda.html')
def nedir(request):
    return render(request,'nedir.html')
def etki(request):
    return render(request,'etki.html')
def tarih(request):
    return render(request,'tarih.html')
def dunya(request):
    return render(request,'dunya.html')
def ozonterapi(request):
    return render(request,'ozonterapi.html')
def hastaliklar(request):
    return render(request,'hastaliklar.html')
def tedaviYontemleri(request):
    return render(request,'tedavi-yontemleri.html')
def etkiMekanizmasi(request):
    return render(request,'etki-mekanizmasi.html')
def kimlereUygulanmaz(request):
    return render(request,'kimlere-uygulanmaz.html')
def tedaviResim(request):
    return render(request,'tedavi-resim.html')
    
def sauna(request):
    return render(request,'sauna.html')

def urunler(request):
    return render(request,'urunler.html')
def iyi(request):
    return render(request,'iyi.html')
def kotu(request):
    return render(request,'kotu.html')

def uygulama(request):
    return render(request,'uygulama.html')

def dahiliye(request):
    return render(request,'dahiliye.html')
def cerrahi(request):
    return render(request,'cerrahi.html')
def ortepedi(request):
    return render(request,'ortepedi.html')
def kadin_dogum(request):
    return render(request,'kadin-dogum.html')
def enfeksiyon(request):
    return render(request,'enfeksiyon.html')
def cilt(request):
    return render(request,'cilt.html')
def solunum(request):
    return render(request,'solunum.html')
def seker(request):
    return render(request,'seker.html')
def kanser(request):
    return render(request,'kanser.html')
def hepatit(request):
    return render(request,'hepatit.html')