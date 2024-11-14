from django.db import models
from edificios.models import Edificio
from login.models import CustomUser
from datetime import timedelta
from sayl.utils import time2timedelta
from cargos.models import CargosCache
from simple_history.models import HistoricalRecords


class PeriodoLectivo(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    actual = models.BooleanField()
    descripcion = models.CharField(max_length=200)
    history = HistoricalRecords()


class Horario(models.Model):
    edificio = models.ForeignKey(Edificio, on_delete=models.PROTECT, blank=True, null=True)
    periodo_lectivo = models.ForeignKey('PeriodoLectivo', on_delete=models.PROTECT, blank=True, null=True)
    legajo = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    cant_modificaciones = models.IntegerField()
    activo = models.BooleanField(default=False)
    cargo = models.OneToOneField(CargosCache, on_delete=models.PROTECT)
    history = HistoricalRecords()


class DetalleHorario(models.Model):
    horario = models.ForeignKey('Horario', on_delete=models.PROTECT)
    
    DIAS = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miercoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sabado'),
        ('Domingo', 'Domingo')
    ]
    desde = models.TimeField()
    hasta = models.TimeField()
    dia = models.CharField(
        max_length=10,
        choices=DIAS
    )
    descripcion = models.CharField(max_length=200)
    history = HistoricalRecords()


class HorariosFijos(models.Model):
    agente = models.ManyToManyField(CustomUser)
    hora_entrada = models.TimeField()
    horas_a_cumplir = models.TimeField()
    hora_salida = models.TimeField()
    history = HistoricalRecords()

    @property
    def hora_salida(self):
        hs_cumplir = timedelta(hours=self.horas_a_cumplir.hour, minutes=self.horas_a_cumplir.minute)
        hora_entrada = time2timedelta(self.hora_entrada)
        hora_salida = hora_entrada + hs_cumplir
        return hora_salida


    


