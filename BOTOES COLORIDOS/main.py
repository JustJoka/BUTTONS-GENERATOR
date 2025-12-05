import customtkinter as ctk
import random

def gerar_botoes():
    for widget in container.winfo_children():
        widget.destroy()


    try:
        quantidade = int(entrada.get())
    except ValueError:
        return
    
    container.update_idletasks()
    altura_container = container.winfo_height()
    largura_container = container.winfo_width()
    
    for i in range(quantidade):
        
        tamanho=40

        x = random.randint(0, max(0, largura_container - tamanho))
        y = random.randint(0, max(0, altura_container - tamanho))

        cor = random.choice(["red", "green", "blue", "black", "orange", "purple"])
        botao = ctk.CTkButton(container, hover_color="black", text=f"{i+1}", fg_color=cor, width=tamanho, height=tamanho)

        botao.place(x=x, y=y)


janela = ctk.CTk()
janela.geometry("600x500")
janela.title("Gerador de botoes")

entrada = ctk.CTkEntry(janela, placeholder_text="Digite a quantidade")
entrada.pack(pady=5)

botao_principal = ctk.CTkButton(janela, command=gerar_botoes, bg_color="pink", text="Gerar botões")
botao_principal.pack(pady=5, padx=5)


container = ctk.CTkFrame(janela)
container.pack(pady=5, fill="both", expand=True)

janela.mainloop()