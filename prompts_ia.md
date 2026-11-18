# Bitácora de Prompts IA (Formato RTCF) - Hito 3

## Prompt 1: Modelamiento Relacional y Optimización ORM en Oracle
- **Rol:** Actúa como un desarrollador Senior especialista en Python y Django con enfoque en rendimiento de bases de datos relacionales Oracle mediante el driver `oracledb`.
- **Tarea:** Diseña dos modelos relacionales (1:N) en `models.py` para un sistema de control de maquinaria agrícola (`TipoMaquinaria` y `Maquinaria`) y su vista de listado `ListView` optimizada con `select_related()`.
- **Contexto:** El proyecto se evalúa en una asignatura de Programación Back End usando Django y Oracle Database local (`oracledb` en modo Thin). La entidad padre solo se gestiona desde Django Admin y la entidad hija requiere al menos 4 atributos variados y evitar consultas N+1 en el catálogo público.
- **Formato:** Entrega el código fuente limpio en bloques Python separados para `models.py` y `views.py`, incluyendo comentarios breves explicando el `on_delete` y la consulta `JOIN` generada por `select_related`.

## Prompt 2: Protección de Rutas CBV (MRO) y Formularios Bootstrap
- **Rol:** Actúa como arquitecto de seguridad web en Django.
- **Tarea:** Implementa un `ModelForm` estilizado con Bootstrap 5 y las vistas basadas en clases `CreateView`, `UpdateView` y `DeleteView` protegidas mediante `LoginRequiredMixin` y alertas `SuccessMessageMixin`.
- **Contexto:** Solo los usuarios autenticados pueden crear, editar o eliminar registros de maquinaria, redirigiendo a `/accounts/login/` si un usuario anónimo intenta acceder por URL directa.
- **Formato:** Entrega el código Python de `forms.py` y las vistas de mutación en `views.py`, respetando el orden correcto de herencia (MRO) de Python.