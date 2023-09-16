

# funciones basicas calculadora

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."
    
    # Interfaz grafica calculadora
import tkinter as tk    
def click_button(valor):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + valor)

def clear_entry():
    entry.delete(0, tk.END)

def calcular():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Entrada
entry = tk.Entry(ventana, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Botones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for boton in botones:
    tk.Button(ventana, text=boton, padx=20, pady=20, font=('Arial', 20),
              command=lambda valor=boton: click_button(valor)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botón de borrar
tk.Button(ventana, text='C', padx=20, pady=20, font=('Arial', 20),
          command=clear_entry).grid(row=row_val, column=col_val)

# Botón de calcular
tk.Button(ventana, text='=', padx=20, pady=20, font=('Arial', 20),
          command=calcular).grid(row=row_val, column=col_val+1)



# TEMA CLARO O OSCURO PARA LA CALCULADORA
# Variables globales para el tema
 
TEMA_CLARO = 'light'
TEMA_OSCURO = 'dark'
TEMA_ACTUAL = TEMA_CLARO

def cambiar_tema():
    global TEMA_ACTUAL
    TEMA_ACTUAL = TEMA_OSCURO if TEMA_ACTUAL == TEMA_CLARO else TEMA_CLARO

    ventana.tk_setPalette(background=COLORES[TEMA_ACTUAL]['background'], foreground=COLORES[TEMA_ACTUAL]['foreground'])

    for boton in botones:
        boton.configure(background=COLORES[TEMA_ACTUAL]['button_background'], foreground=COLORES[TEMA_ACTUAL]['button_foreground'])

# Definir colores para los temas
COLORES = {
    'light': {
        'background': '#FFFFFF',
        'foreground': '#000000',
        'button_background': '#E0E0E0',
        'button_foreground': '#000000'
    },
    'dark': {
        'background': '#333333',
        'foreground': '#FFFFFF',
        'button_background': '#444444',
        'button_foreground': '#FFFFFF'
    }
}

ventana = tk.Tk()
ventana.title("Calculadora")

# Configurar el tema predeterminado (claro)
ventana.tk_setPalette(background=COLORES[TEMA_CLARO]['background'], foreground=COLORES[TEMA_CLARO]['foreground'])

# Botones (solo como ejemplo)
botones = []
for i in range(3):
    for j in range(3):
        boton = tk.Button(ventana, text=f'Botón {i+1}-{j+1}', padx=20, pady=20)
        boton.grid(row=i, column=j)
        botones.append(boton)

# Crear un botón para cambiar el tema
tk.Button(ventana, text='Cambiar Tema', command=cambiar_tema).grid(row=3, column=0, columnspan=3)


ventana.mainloop()                                                                                                         