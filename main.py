import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from horario import Horario
import bisect  # Para búsqueda binaria

# Instancia de Horario
horario = Horario()

# Función Merge Sort para ordenar los empleados por nombre
def merge_sort(empleados):
    if len(empleados) > 1:
        mid = len(empleados) // 2
        left_half = empleados[:mid]
        right_half = empleados[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i].nombre < right_half[j].nombre:
                empleados[k] = left_half[i]
                i += 1
            else:
                empleados[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            empleados[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            empleados[k] = right_half[j]
            j += 1
            k += 1

# Función para verificar si es jefe o empleado
def verificar_empleado():
    nombre_empleado = entry_nombre.get()
    try:
        id_empleado = int(entry_id.get())
    except ValueError:
        messagebox.showerror("Error", "El ID debe ser un número.")
        return

    # Usamos la búsqueda binaria para encontrar el empleado
    empleado = buscar_empleado_binario(nombre_empleado, id_empleado)

    if not empleado:
        messagebox.showerror("Error", "Nombre o ID incorrecto.")
        return

    # Si es jefe, mostrar opciones para consultar horarios de otros empleados
    if empleado.es_jefe:
        ventana_jefe(empleado)
    else:
        ventana_empleado(empleado)

# Función de búsqueda binaria
def buscar_empleado_binario(nombre, id_empleado):
    # Suponemos que los empleados están ordenados por nombre
    empleados_ordenados = horario.empleados[:]
    merge_sort(empleados_ordenados)  # Usamos Merge Sort para ordenar

    # Búsqueda binaria por nombre
    index = bisect.bisect_left([emp.nombre for emp in empleados_ordenados], nombre)
    if index != len(empleados_ordenados) and empleados_ordenados[index].nombre == nombre and empleados_ordenados[index].id == id_empleado:
        return empleados_ordenados[index]
    return None

# Ventana para el jefe
def ventana_jefe(empleado):
    ventana_principal.withdraw()
    ventana_jefe = tk.Toplevel()
    ventana_jefe.title("Portal del Jefe")
    ventana_jefe.geometry("400x300")

    # Mostrar mensaje de bienvenida
    tk.Label(ventana_jefe, text=f"Bienvenida {empleado.nombre}", font=("Helvetica", 14)).pack(pady=10)
    tk.Label(ventana_jefe, text="Elija un empleado para consutar su horario", font=("Helvetica", 14, )).pack(pady=10)

    # Lista de empleados excluyendo a la jefa, ordenada por nombre usando Merge Sort
    empleados_disponibles = horario.empleados[:]
    merge_sort(empleados_disponibles)  # Usamos Merge Sort para ordenar

    # Combobox para elegir un empleado
    combo_empleado = ttk.Combobox(ventana_jefe, values=[emp.nombre for emp in empleados_disponibles if not emp.es_jefe], font=("Helvetica", 12))
    combo_empleado.pack(pady=10)

    # Campo de entrada para el día
    tk.Label(ventana_jefe, text="Ingresa el día de la semana:").pack(pady=5)
    entry_dia = ttk.Entry(ventana_jefe)
    entry_dia.pack(pady=5)

    # Botones para consultar el horario
    btn_consultar_turno = tk.Button(ventana_jefe, text="Consultar Turno de Hoy", command=lambda: consultar_turno_jefe(combo_empleado, empleado, entry_dia))
    btn_consultar_turno.pack(pady=5)

    btn_consultar_semana = tk.Button(ventana_jefe, text="Consultar Horario Semanal", command=lambda: consultar_semana_jefe(combo_empleado, empleado, entry_dia))
    btn_consultar_semana.pack(pady=5)

# Función para consultar el turno de hoy del jefe (sin cambios)
def consultar_turno_jefe(combo_empleado, jefe, entry_dia):
    nombre_empleado = combo_empleado.get()
    empleado = next((emp for emp in horario.empleados if emp.nombre == nombre_empleado), None)
    
    if empleado:
        dia_semana = entry_dia.get()
        if dia_semana not in horario.dias_semana:
            messagebox.showerror("Error", "El día ingresado no es válido.")
            return

        turno = horario.turnos_predefinidos.get(dia_semana, {}).get(empleado, None)
        if turno:
            hora_inicio, hora_fin = turno
            messagebox.showinfo("Turno encontrado", f"Turno de {empleado.nombre} en {dia_semana}: {hora_inicio.strftime('%H:%M')} - {hora_fin.strftime('%H:%M')}")
        else:
            messagebox.showerror("Error", f"{empleado.nombre} no tiene turno asignado en {dia_semana}.")
    else:
        messagebox.showerror("Error", "Empleado no encontrado.")

# Función para consultar el horario semanal del jefe (sin cambios)
def consultar_semana_jefe(combo_empleado, jefe, entry_dia):
    nombre_empleado = combo_empleado.get()
    empleado = next((emp for emp in horario.empleados if emp.nombre == nombre_empleado), None)
    
    if empleado:
        tabla = f"Horario Semanal de {empleado.nombre}\n"
        for dia in horario.dias_semana:
            turno = horario.turnos_predefinidos.get(dia, {}).get(empleado, None)
            if turno:
                hora_inicio, hora_fin = turno
                tabla += f"{dia}: {hora_inicio.strftime('%H:%M')} - {hora_fin.strftime('%H:%M')}\n"
            else:
                tabla += f"{dia}: No asignado\n"
        messagebox.showinfo("Horario Semanal", tabla)

# Función para la ventana del empleado (sin cambios)
def ventana_empleado(empleado):
    ventana_principal.withdraw()
    ventana_empleado = tk.Toplevel()
    ventana_empleado.title(f"Horario de {empleado.nombre}")
    ventana_empleado.geometry("400x300")

    tk.Label(ventana_empleado, text=f"Bienvenid@ {empleado.nombre}", font=("Helvetica", 14)).pack(pady=10)

    tk.Label(ventana_empleado, text="Ingresa el día de la semana:").pack(pady=5)
    entry_dia = ttk.Entry(ventana_empleado)
    entry_dia.pack(pady=5)

    btn_consultar_turno = tk.Button(ventana_empleado, text="Consultar Turno de Hoy", command=lambda: consultar_turno_empleado(empleado, entry_dia))
    btn_consultar_turno.pack(pady=5)

    btn_consultar_semana = tk.Button(ventana_empleado, text="Consultar Horario Semanal", command=lambda: consultar_semana_empleado(empleado, entry_dia))
    btn_consultar_semana.pack(pady=5)

# Función para consultar el turno de hoy del empleado (sin cambios)
def consultar_turno_empleado(empleado, entry_dia):
    dia_semana = entry_dia.get()
    if dia_semana not in horario.dias_semana:
        messagebox.showerror("Error", "El día ingresado no es válido.")
        return

    turno = horario.turnos_predefinidos.get(dia_semana, {}).get(empleado, None)
    if turno:
        hora_inicio, hora_fin = turno
        messagebox.showinfo("Turno encontrado", f"Tu turno el {dia_semana}: {hora_inicio.strftime('%H:%M')} - {hora_fin.strftime('%H:%M')}")
    else:
        messagebox.showerror("Error", f"No tienes turno asignado el {dia_semana}.")

# Función para consultar el horario semanal del empleado (sin cambios)
def consultar_semana_empleado(empleado, entry_dia):
    tabla = f"Horario Semanal de {empleado.nombre}\n"
    for dia in horario.dias_semana:
        turno = horario.turnos_predefinidos.get(dia, {}).get(empleado, None)
        if turno:
            hora_inicio, hora_fin = turno
            tabla += f"{dia}: {hora_inicio.strftime('%H:%M')} - {hora_fin.strftime('%H:%M')}\n"
        else:
            tabla += f"{dia}: No asignado\n"
    messagebox.showinfo("Horario Semanal", tabla)

# Ventana Principal de Entrada
ventana_principal = tk.Tk()
ventana_principal.title("Ingreso")
ventana_principal.geometry("400x250")

# Etiqueta con el mensaje de bienvenida
tk.Label(ventana_principal, text="Horarios Farmacia Arapiles", font=("Helvetica", 14, "bold")).pack(pady=10)

# Campos de entrada
tk.Label(ventana_principal, text="Nombre:").pack(pady=5)
entry_nombre = ttk.Entry(ventana_principal)
entry_nombre.pack(pady=5)

tk.Label(ventana_principal, text="ID:").pack(pady=5)
entry_id = ttk.Entry(ventana_principal)
entry_id.pack(pady=5)

btn_ingresar = tk.Button(ventana_principal, text="Ingresar", command=verificar_empleado)
btn_ingresar.pack(pady=10)

ventana_principal.mainloop()
