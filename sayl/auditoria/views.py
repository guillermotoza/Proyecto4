from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app_tipojustificacion.views import TipoJustificacion
from app_justificacion.views import Justificacion
from app_horarios.models import *
from asistencias.models import Asistencia
from django.core import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from sayl.utils import get_next_or_prev
import logging
from django.db.models import Count

logger = logging.getLogger(__name__)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def get_historial_diff(historial, id_history):
    for i in range(len(historial)):
        if historial[i].pk == id_history:
            audit_regsolo = historial[i]
            delta = audit_regsolo.diff_against(historial[i + 1])
            data = [{'change': change.field, 'old': change.old, 'new': change.new} for change in delta.changes]
            return data
    return [{'change': False}]

def estadistica_estados_marcajes(request): 
    labels = [] 
    data = [] 
    fecha_rango = request.GET.get('fechona') 
    user_pk = request.GET.get('user_pk') 
    
    if fecha_rango: 
        f_desde, f_hasta = fecha_rango.split(' - ') 
        f_desde = f"{f_desde[-4:]}-{f_desde[3:5]}-{f_desde[0:2]}" 
        f_hasta = f"{f_hasta[-4:]}-{f_hasta[3:5]}-{f_hasta[0:2]}" 
    else: 
        f_desde, f_hasta = None, None 
        
    print("----------->>>>>>> ", user_pk, ">>", fecha_rango) 
    
    if user_pk == 'all': 
        if fecha_rango: 
            queryset = Asistencia.objects.filter(fecha_marcaje__range=(f_desde, f_hasta)).values('condicion').order_by('condicion').annotate(count=Count('condicion')) 
            print(f_desde, " - ", f_hasta) 
        else: 
            queryset = Asistencia.objects.values('condicion').order_by('condicion').annotate(count=Count('condicion')) 
    else: 
        if fecha_rango: 
            queryset = Asistencia.objects.filter(legajo__pk=user_pk, fecha_marcaje__range=(f_desde, f_hasta)).values('condicion').order_by('condicion').annotate(count=Count('condicion')) 
        else: 
            queryset = Asistencia.objects.filter(legajo__pk=user_pk).values('condicion').order_by('condicion').annotate(count=Count('condicion')) 
    
    for entry in queryset: 
        labels.append(entry['condicion']) 
        data.append(entry['count']) 
    
    return JsonResponse(data={ 
        'labels': labels, 
        'data': data 
    })

def audit_tjust(request):
    tj_all = TipoJustificacion.history.all()
    context = {'audit_regs': tj_all}
    return render(request, 'auditoria/audit_tjust.html', context)

def audit_tjust_detail(request, pk):
    tjs_historial = TipoJustificacion.history.filter(id=pk)   
    context = {'audit_regs': tjs_historial, 'detail': True}
    return render(request, 'auditoria/audit_tjust.html', context)

def audit_tjust_detail_json(request, pk, id_history):
    tjs_historial = TipoJustificacion.history.filter(id=pk)
    data = get_historial_diff(tjs_historial, id_history)
    return JSONResponse(data)

def audit_just(request):
    audit_justs = Justificacion.history.all()
    context = {'audit_justs': audit_justs}
    return render(request, 'auditoria/audit_just.html', context)

def audit_just_detail(request, pk):
    js_historial = Justificacion.history.filter(id=pk)    
    context = {'audit_justs': js_historial, 'detail': True}
    return render(request, 'auditoria/audit_just.html', context)

def audit_just_detail_json(request, pk, id_history):
    js_historial = Justificacion.history.filter(id=pk)
    data = get_historial_diff(js_historial, id_history)
    return JSONResponse(data)

def audit_asist(request):
    audit_asists = Asistencia.history.all()
    context = {'audit_asists': audit_asists}
    return render(request, 'auditoria/audit_asist.html', context)

def audit_asist_detail(request, pk):
    js_historial = Asistencia.history.filter(id=pk)    
    context = {'audit_asists': js_historial, 'detail': True}
    return render(request, 'auditoria/audit_asist.html', context)

def audit_asist_detail_json(request, pk, id_history):
    js_historial = Asistencia.history.filter(id=pk)
    data = get_historial_diff(js_historial, id_history)
    return JSONResponse(data)

def audit_horario(request):
    audit_horarios = Horario.history.all()
    context = {'audit_horarios': audit_horarios}
    return render(request, 'auditoria/audit_horario.html', context)

def audit_horario_detail(request, pk):
    js_historial = Horario.history.filter(id=pk)    
    print(js_historial)
    context = {'audit_horarios':js_historial, 'detail':True}
    # return render(request, 'auditoria/audit_tjust.html', context)
    return render(request, 'auditoria/audit_horario.html', context)

def audit_horario_detail_json(request, pk, id_history):
    print(pk, id_history)
    js_historial = Horario.history.filter(id=pk)
    historial = Horario.history.filter(id=pk)
    print(historial)
    if len(js_historial) > 1:
        for i in range(len(historial)):
            print(id_history, " - ", historial[i].pk)
            if historial[i].pk == id_history:            
                audit_regsolo = historial[i]    
                delta = audit_regsolo.diff_against(js_historial[i+1])
                print(delta)
                data = []            
                for change in delta.changes:
                    dic = {'change': change.field, 'old':change.old, 'new':change.new}
                    data.append(dic)
                    print("Entro en el for")
                    print(data)
                break
            else:
                data = []
    else:
        data=[{'change':False}]
    print("DATA: ", data)
    return JSONResponse(data)  
    
def audit_horario_fijo(request):
    audit_horario_fijos = HorariosFijos.history.all()
    context = {'audit_horario_fijos': audit_horario_fijos}
    return render(request, 'auditoria/audit_horario_fijo.html', context)

def audit_horario_fijo_detail(request, pk):
    js_historial = HorariosFijos.history.filter(id=pk)    
    print(js_historial)
    context = {'audit_horario_fijos':js_historial, 'detail':True}
    # return render(request, 'auditoria/audit_tjust.html', context)
    return render(request, 'auditoria/audit_horario_fijo.html', context)

def audit_horario_fijo_detail_json(request, pk, id_history):
    print(pk, id_history)
    js_historial = HorariosFijos.history.filter(id=pk)
    historial = HorariosFijos.history.filter(id=pk)
    print(historial)
    if len(js_historial) > 1:
        for i in range(len(historial)):
            print(id_history, " - ", historial[i].pk)
            if historial[i].pk == id_history:            
                audit_regsolo = historial[i]    
                delta = audit_regsolo.diff_against(js_historial[i+1])
                print(delta)
                data = []            
                for change in delta.changes:
                    dic = {'change': change.field, 'old':change.old, 'new':change.new}
                    data.append(dic)
                    print("Entro en el for")
                    print(data)
                break
            else:
                data = []
    else:
        data=[{'change':False}]
    print("DATA: ", data)
    return JSONResponse(data) 



