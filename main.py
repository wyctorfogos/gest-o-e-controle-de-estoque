import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# Função para calcular o estoque em função do tempo
def calcular_estoque(Qmax, Qmin, r, T, total_tempo):
    def estoque(t):
        ciclo = t // T  
        tempo_no_ciclo = t % T  
        Q = Qmax - r * tempo_no_ciclo  
        
        if tempo_no_ciclo == T - 1:
            return Qmax
        elif Q < Qmin:
            return Qmin
        return Q

    t = np.arange(0, total_tempo, 1)  
    Q = [estoque(i) for i in t]  
    return t, Q

# Função para gerar o gráfico
def gerar_grafico():
    try:
        Qmax = float(entry_Qmax.get())
        Qmin = float(entry_Qmin.get())
        r = float(entry_r.get())
        T = int(entry_T.get())
        total_tempo = int(entry_total_tempo.get())
            
        t, Q = calcular_estoque(Qmax, Qmin, r, T, total_tempo)

        # Plotar o gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(t, Q, color='blue', marker='o', linestyle='-', label='Nível de Estoque')
        plt.axhline(y=Qmin, color='green', linestyle='--', label='Estoque de Segurança')
        plt.axhline(y=Qmax, color='red', linestyle='--', label='Ponto de Pedido')
            
        plt.xlabel('Tempo (dias)')
        plt.ylabel('Quantidade em Estoque')
        plt.title('Gráfico de Estoque em Função do Tempo - Com Reabastecimento')
        plt.legend(loc='upper right')
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")
            
if __name__=="__main__":
    # Criar a interface gráfica
    root = tk.Tk()
    root.title("Gerador de Gráfico de Estoque")

    # Criar labels e entradas
    tk.Label(root, text="Estoque Máximo (Qmax):").grid(row=0, column=0)
    entry_Qmax = tk.Entry(root)
    entry_Qmax.grid(row=0, column=1)

    tk.Label(root, text="Estoque de Segurança (Qmin):").grid(row=1, column=0)
    entry_Qmin = tk.Entry(root)
    entry_Qmin.grid(row=1, column=1)

    tk.Label(root, text="Taxa de Consumo (r):").grid(row=2, column=0)
    entry_r = tk.Entry(root)
    entry_r.grid(row=2, column=1)

    tk.Label(root, text="Ciclo de Reabastecimento (T):").grid(row=3, column=0)
    entry_T = tk.Entry(root)
    entry_T.grid(row=3, column=1)

    tk.Label(root, text="Período Total (dias):").grid(row=4, column=0)
    entry_total_tempo = tk.Entry(root)
    entry_total_tempo.grid(row=4, column=1)

    # Botão para gerar o gráfico
    btn_gerar = tk.Button(root, text="Gerar Gráfico", command=gerar_grafico)
    btn_gerar.grid(row=5, columnspan=2)

    # Executar a interface gráfica
    root.mainloop()




