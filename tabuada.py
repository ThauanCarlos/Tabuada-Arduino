import tkinter as tk
import random
import serial

# Configuração da porta serial do Arduino (substitua "COM3" pelo nome da porta correta do seu Arduino)
arduino_port = 'COM3'  # Para Windows: algo como 'COM3', para Linux/Mac: '/dev/ttyUSB0'
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

def gerar_pergunta():
    # Gera dois números aleatórios de 1 a 9
    global num1, num2
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    pergunta_label.config(text=f"Quanto é {num1} x {num2}?")
    entry_resposta.delete(0, tk.END)

def verificar_resposta():
    try:
        resposta_usuario = int(entry_resposta.get())
        resposta_correta = num1 * num2
        
        if resposta_usuario == resposta_correta:
            resultado_label.config(text="Correto!", fg="green")
            enviar_resultado(True)
        else:
            resultado_label.config(text=f"Incorreto! A resposta era {resposta_correta}", fg="red")
            enviar_resultado(False)
        
        # Gerar uma nova pergunta após a verificação
        root.after(3000, gerar_pergunta)  # Gera uma nova pergunta após 3 segundos
        
    except ValueError:
        resultado_label.config(text="Por favor, insira um número válido.", fg="red")

def enviar_resultado(correto):
    try:
        if correto:
            ser.write(b'1')  # Enviar '1' se a resposta for correta
        else:
            ser.write(b'0')  # Enviar '0' se a resposta for incorreta
    except:
        resultado_label.config(text="Erro ao comunicar com o Arduino", fg="red")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Tabuada Arduino")
root.geometry("300x200")

# Elementos da GUI
pergunta_label = tk.Label(root, text="", font=("Arial", 14))
pergunta_label.pack(pady=10)

entry_resposta = tk.Entry(root, font=("Arial", 14))
entry_resposta.pack(pady=5)

botao_verificar = tk.Button(root, text="Verificar", command=verificar_resposta, font=("Arial", 12))
botao_verificar.pack(pady=5)

resultado_label = tk.Label(root, text="", font=("Arial", 12))
resultado_label.pack(pady=10)


gerar_pergunta()


root.mainloop()


ser.close()
