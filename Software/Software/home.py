from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader

def saludo (request): #primera vista 
    #views_sal=open("C:/Users/FABRICIO/Desktop/Django/Software2/Software2/views/home.html")
    #tmp=Template(views_sal.read())
    #views_sal.close()
    views_sal=loader.get_template('home.html')
    #contexto=Context()
    documento=views_sal.render()
    return HttpResponse(documento)

    
def login(request): #segundA vista 
    views_log=loader.get_template('login.html')
    doc=views_log.render()
    return HttpResponse(doc)
    
def odontologo(request): #tercera vista 
    views_doc=loader.get_template('odontologo.html')
    docum=views_doc.render()
    return HttpResponse(docum)    

def citas(request): #cuarta vista 
    views_cit=loader.get_template('citas.html')
    documen=views_cit.render()
    return HttpResponse(documen)  

def fichas(request): #quinta vista 
    views_fic=loader.get_template('fichas.html')
    documento=views_fic.render()
    return HttpResponse(documento)  

def registar(request): #sexta vista 
    views_reg=loader.get_template('registrar.html')
    d=views_reg.render()
    return HttpResponse(d)  
    
def nosotros(request): #septima vista 
    views_nos=loader.get_template('nosotros.html')
    dou=views_nos.render()
    return HttpResponse(dou) 

def servicios(request): #octaba vista 
    views_ser=loader.get_template('servicios.html')
    ser=views_ser.render()
    return HttpResponse(ser) 