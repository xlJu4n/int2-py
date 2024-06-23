import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

class Curso:
    def __init__(self, nombre, profesor, asignaturas, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.asignaturas = asignaturas
        self.horario = horario
        self.estudiantes = []

class Profesor:
    def __init__(self, nombre, horarios):
        self.nombre = nombre
        self.horarios = horarios

class Estudiante:
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

def inscribir_estudiante():
    curso_index = cursos_listbox.curselection()
    if curso_index:
        curso_seleccionado = cursos[curso_index[0]]
        if len(curso_seleccionado.estudiantes) < 20:
            nombre = entry_nombre_estudiante.get()
            apellido = entry_apellido_estudiante.get()
            cedula = entry_cedula_estudiante.get()
            estudiante = Estudiante(nombre, apellido, cedula)
            curso_seleccionado.estudiantes.append(estudiante)
            messagebox.showinfo("Estudiante inscrito", f"{nombre} {apellido} se ha inscrito en el curso {curso_seleccionado.nombre}")
            entry_nombre_estudiante.delete(0, tk.END)
            entry_apellido_estudiante.delete(0, tk.END)
            entry_cedula_estudiante.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "El curso ya tiene 20 estudiantes inscritos, no se pueden agregar más.")
    else:
        messagebox.showwarning("Error", "Por favor, seleccione un curso para inscribir al estudiante.")

def mostrar_horarios():
    cursos_disponibles = [curso.nombre + " - " + curso.horario.dia + " " + curso.horario.hora_inicio + "-" + curso.horario.hora_fin for curso in cursos]
    if cursos_disponibles:
        horarios_text = "\n".join(cursos_disponibles)
        messagebox.showinfo("Horarios de cursos disponibles", horarios_text)
    else:
        messagebox.showinfo("Horarios de cursos disponibles", "No hay cursos disponibles en este momento.")

def mostrar_profesores():
    profesores_text = ""
    for profesor in profesores:
        profesores_text += f"{profesor.nombre} - Horarios: {', '.join([horario.dia + ' ' + horario.hora_inicio + '-' + horario.hora_fin for horario in profesor.horarios])}\n"
    if profesores_text:
        messagebox.showinfo("Profesores disponibles", profesores_text)
    else:
        messagebox.showinfo("Profesores disponibles", "No hay profesores disponibles en este momento.")

def mostrar_estudiantes_inscritos():
    curso_index = cursos_listbox.curselection()
    if curso_index:
        curso_seleccionado = cursos[curso_index[0]]
        estudiantes_inscritos = ", ".join([estudiante.nombre + " " + estudiante.apellido for estudiante in curso_seleccionado.estudiantes])
        if estudiantes_inscritos:
            messagebox.showinfo("Estudiantes inscritos", f"Estudiantes inscritos en el curso {curso_seleccionado.nombre}:\n{estudiantes_inscritos}")
        else:
            messagebox.showinfo("Estudiantes inscritos", f"No hay estudiantes inscritos en el curso {curso_seleccionado.nombre}")
    else:
        messagebox.showwarning("Error", "Por favor, seleccione un curso para ver los estudiantes inscritos.")

def listar_cursos():
      for curso in cursos:
        cursos_listbox.insert(tk.END, f"{curso.nombre} - {curso.profesor}")

cursos = [
    Curso("Programacion", "Federico Velez", ["Programacion basica", "Interfaces Graficas"], Horario("Lunes", "07:00", "09:00")),
    Curso("Idiomas", "Dayana Contreras", ["Ingles", "Frances"], Horario("Jueves", "06:00", "08:00")),
    Curso("Fisica", "Luisa Gimenez", ["Electromagnetismo", "Mecanica"], Horario("Martes", "10:00", "12:00"))
]

profesores = [
    Profesor("Federico Velez", [Horario("Lunes", "07:00", "09:00"), Horario("Miércoles", "14:00", "16:00")]),
    Profesor("Dayana Contreras", [Horario("Jueves", "06:00", "08:00"), Horario("Viernes", "12:00", "14:00")]),
    Profesor("Luisa Gimenez", [Horario("Martes", "10:00", "12:00"), Horario("Jueves", "10:00", "12:00")])
]

root = tk.Tk()
root.title("Gestión de Cursos")


bg_color = "#CCD1D1"
fg_color = "#17202A"
highlight_color = "#ffcc00"
button_color = "#1B4F72"
button_text_color = "#ffffff"

root.configure(bg=bg_color)

frame = tk.Frame(root, bg=bg_color)
frame.pack(padx=20, pady=20)


image_path = r"C:\Users\jjcme\OneDrive\Escritorio\pooxd\Curso tkinter\Gestion de Curso\CURSO\IMGS\CURSO.png"
img = PhotoImage(file=image_path)

image_label = tk.Label(frame, image=img, bg=bg_color)
image_label.grid(row=0, column=3, rowspan=7, padx=10, pady=10)

label_nombre_estudiante = tk.Label(frame, text="Nombre estudiante:", bg=bg_color, fg=fg_color)
label_nombre_estudiante.grid(row=0, column=0, padx=5, pady=5)

entry_nombre_estudiante = tk.Entry(frame)
entry_nombre_estudiante.grid(row=0, column=1, padx=5, pady=5)

label_apellido_estudiante = tk.Label(frame, text="Apellido estudiante:", bg=bg_color, fg=fg_color)
label_apellido_estudiante.grid(row=1, column=0, padx=5, pady=5)

entry_apellido_estudiante = tk.Entry(frame)
entry_apellido_estudiante.grid(row=1, column=1, padx=5, pady=5)

label_cedula_estudiante = tk.Label(frame, text="Documento estudiante:", bg=bg_color, fg=fg_color)
label_cedula_estudiante.grid(row=2, column=0, padx=5, pady=5)

entry_cedula_estudiante = tk.Entry(frame)
entry_cedula_estudiante.grid(row=2, column=1, padx=5, pady=5)

button_inscribir_estudiante = tk.Button(frame, text="Inscribir estudiante", command=inscribir_estudiante, bg=button_color, fg=button_text_color)
button_inscribir_estudiante.grid(row=3, column=0, columnspan=2, pady=10)

button_mostrar_estudiantes = tk.Button(frame, text="Mostrar estudiantes inscritos", command=mostrar_estudiantes_inscritos, bg=button_color, fg=button_text_color)
button_mostrar_estudiantes.grid(row=4, column=0, columnspan=2, pady=10)

button_horarios = tk.Button(frame, text="Mostrar horarios de cursos", command=mostrar_horarios, bg=button_color, fg=button_text_color)
button_horarios.grid(row=5, column=0, columnspan=2, pady=10)

button_profesores = tk.Button(frame, text="Mostrar profesores", command=mostrar_profesores, bg=button_color, fg=button_text_color)
button_profesores.grid(row=6, column=0, columnspan=2, pady=10)

label_cursos_disponibles = tk.Label(frame, text="Cursos disponibles:", bg=bg_color, fg=fg_color)
label_cursos_disponibles.grid(row=0, column=2, padx=5, pady=5)

cursos_listbox = tk.Listbox(frame, height=15, width=50, bg="white", fg=fg_color, selectbackground=highlight_color)
cursos_listbox.grid(row=1, column=2, rowspan=6, padx=5, pady=5)

button_listar_cursos = tk.Button(frame, text="Listar cursos", command=listar_cursos, bg=button_color, fg=button_text_color)
button_listar_cursos.grid(row=7, column=2, columnspan=2, pady=10)

root.mainloop()