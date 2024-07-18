from datetime import date
from django.shortcuts import render, redirect
from apps.career.models import Career
from apps.period.models import Semester
from apps.group.models import Group
from apps.academy.models import Professor
from .models import ReporteTutoria

def reporte_tutoria(request):
    if request.method == 'POST':
        # Procesar el formulario enviado
        fecha_tutoria = request.POST.get('fecha')
        carrera_id = request.POST.get('carrera')
        semestre_id = request.POST.get('semestre')
        grupo_id = request.POST.get('grupo')
        nombre_actividad = request.POST.get('nombre_actividad')
        objetivo_actividad = request.POST.get('objetivo_actividad')
        descripcion_actividad = request.POST.get('descripcion_actividad')
        evidencia1 = request.FILES.get('evidencia1')
        evidencia2 = request.FILES.get('evidencia2')

        reporte = ReporteTutoria(
            fecha_tutoria=fecha_tutoria,
            carrera_id=carrera_id,
            semestre_id=semestre_id,
            grupo_id=grupo_id,
            nombre_actividad=nombre_actividad,
            objetivo_actividad=objetivo_actividad,
            descripcion_actividad=descripcion_actividad,
            evidencia1=evidencia1,
            evidencia2=evidencia2,
            tutor=request.user.professor
        )
        reporte.save()

        
        # Redirigir a una página de éxito o a donde necesites después de guardar
        return redirect('ruta_de_exito')  # Reemplazar 'ruta_de_exito' con la URL a donde deseas redirigir

    else:
        tutor = request.user.professor  
        carrera = professor.career
        semestre = professor.group
        grupo = professor.group

        context = {
            'reporte': { 
                'carreras': Career.objects.all(), 
                'semestres': Semester.objects.all(),  
                'grupos': Group.objects.all(),
            },
            'tutor': tutor,
            'default_carrera': carrera.id,
            'default_semestre': semestre.id,
            'default_grupo': grupo.id,
        }
        return render(request, 'reporte_tutorias/reporte_tutoria.html', context)
