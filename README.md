# Horarios Farmacia Arapiles

Este proyecto permite gestionar los horarios de los empleados de la farmacia Arapiles, con opciones diferenciadas para empleados y jefe. Los usuarios pueden consultar sus propios horarios y, en el caso del jefe, consultar los horarios de los demás empleados.

## Archivos del Proyecto

El proyecto está dividido en tres archivos principales:

1. **empleado.py**: 
   - Define la clase `Empleado`, que representa a cada empleado con las propiedades como nombre, ID y si es jefe.
   - Métodos:
     - `__init__()`: Inicializa un empleado con su nombre, ID y un valor opcional `es_jefe`.
     - Propiedades `nombre`, `id`, `es_jefe` para acceder a los atributos del empleado.

2. **horario.py**: 
   - Define la clase `Horario`, que gestiona los turnos de los empleados.
   - Métodos:
     - `__init__()`: Inicializa los empleados y los días de la semana.
     - `asignar_turno()`: Asigna un turno específico a un empleado para un día determinado.
     - `consultar_turno()`: Devuelve el turno asignado para un empleado y un día específico.
     - `consultar_turno_semanal()`: Devuelve el horario completo de un empleado para toda la semana.

3. **main.py**: 
   - Contiene la aplicación principal con la interfaz gráfica de usuario usando `tkinter`.
   - Funcionalidad:
     - Los empleados pueden ingresar su nombre y ID para acceder a su información.
     - Los jefes pueden consultar los horarios de otros empleados.
     - Usa el algoritmo de **Merge Sort** para ordenar a los empleados por nombre y **Búsqueda Binaria** para encontrarlos rápidamente.

## Instrucciones

1. **Ejecuta el archivo `main.py`**.
   - Al abrir la aplicación, verás una ventana de inicio con campos para ingresar el nombre y el ID de un empleado.

2. **Ingreso como empleado**:
   - En la ventana de inicio, introduce tu nombre y ID.
   - Si eres un empleado, verás las opciones para consultar tu turno de hoy o el horario semanal.

3. **Ingreso como jefe**:
   - Si eres jefe, después de ingresar tu nombre y ID, tendrás la opción de consultar los turnos de otros empleados para un día específico o el horario semanal de todo el personal.

