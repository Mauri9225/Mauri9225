import tkinter as tk
from tkinter import messagebox

# Crear ventana
ventana = tk.Tk()
ventana.title("Registro Usuario")
ventana.geometry("400x350")
ventana.configure(bg="lightgray")

# Crear frame
formulario = tk.Frame(ventana, bg="white", padx=20, pady=20)
formulario.pack(pady=20)

# Campos de entrada
tk.Label(formulario, text="Nombre Completo:", bg="white").grid(row=0, column=0, sticky="e", pady=5)
entrada_nombre = tk.Entry(formulario, width=30)
entrada_nombre.grid(row=0, column=1, pady=5)

tk.Label(formulario, text="Correo:", bg="white").grid(row=1, column=0, sticky="e", pady=5)
entrada_correo = tk.Entry(formulario, width=30)
entrada_correo.grid(row=1, column=1, pady=5)

tk.Label(formulario, text="Cédula:", bg="white").grid(row=2, column=0, sticky="e", pady=5)
entrada_cedula = tk.Entry(formulario, width=30)
entrada_cedula.grid(row=2, column=1, pady=5)

tk.Label(formulario, text="Saldo inicial:", bg="white").grid(row=3, column=0, sticky="e", pady=5)
entrada_saldo = tk.Entry(formulario, width=30)
entrada_saldo.grid(row=3, column=1, pady=5)


# Función para validar y mostrar mensaje
def enviar_formulario():
    nombre = entrada_nombre.get().strip()
    correo = entrada_correo.get().strip()
    cedula = entrada_cedula.get().strip()
    saldo = entrada_saldo.get().strip()

    # Validaciones de datos
    if not nombre or not correo or not cedula or not saldo:# validacion que todos los campos esten llenos
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return
    if "@" not in correo or "." not in correo: #valida que el correo contenga los caracteres @ y .
        messagebox.showerror("Error", "Correo electrónico no válido.")
        return
    if not cedula.isdigit(): #valida que la cedula sea numerica sin guiones
        messagebox.showerror("Error", "La cédula debe ser numérica (sin guiones).")
        return
    if len(cedula) > 10: #valida que no exeda los 10 digitos
        messagebox.showerror("Error", "La cédula no puede tener más de 10 dígitos.")
        return
    try:
        saldo_float = float(saldo)
        if saldo_float < 0: # valida que no sean numeros negativos
            messagebox.showerror("Error", "El saldo inicial debe ser un número positivo.")
            return
    except ValueError:
        messagebox.showerror("Error", "El saldo inicial debe ser un número válido.")
        return

    # Si todo es válido
    messagebox.showinfo("Éxito", f"¡Formulario enviado con éxito!\nBienvenido/a {nombre}.\nTu saldo inicial es ${saldo_float:,.2f}")


# Botón de envío
boton_enviar = tk.Button(formulario, text="Enviar", command=enviar_formulario, bg="blue", fg="white", width=20)
boton_enviar.grid(row=4, column=0, columnspan=2, pady=15)

# Ejecutar
ventana.mainloop()
