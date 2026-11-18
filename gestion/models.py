from django.db import models


class TipoMaquinaria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Tipo de Maquinaria")
    descripcion = models.TextField(blank=True, verbose_name="Descripción de categoría")

    class Meta:
        verbose_name = "Tipo de Maquinaria"
        verbose_name_plural = "Tipos de Maquinaria"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Maquinaria(models.Model):
    nombre = models.CharField(max_length=120, verbose_name="Nombre / Modelo")
    patente_serie = models.CharField(max_length=50, unique=True, verbose_name="Patente o N° Serie")
    anio_fabricacion = models.PositiveIntegerField(verbose_name="Año de Fabricación")
    horas_uso = models.DecimalField(max_digits=8, decimal_places=1, default=0.0, verbose_name="Horas de Uso")
    operativa = models.BooleanField(default=True, verbose_name="¿Operativa?")
    observaciones = models.TextField(blank=True, verbose_name="Observaciones Técnicas")
    tipo = models.ForeignKey(
        TipoMaquinaria,
        on_delete=models.CASCADE,
        related_name='maquinarias',
        verbose_name="Tipo de Maquinaria"
    )

    class Meta:
        verbose_name = "Maquinaria"
        verbose_name_plural = "Maquinarias"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.patente_serie})"