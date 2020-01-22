#GAD

from tkinter import *
from random import randint

listabolas=[]
bola = 0

def iniciar():
	botao_sortear = Button(janela, width= 7, text='Sortear', command=sortear)
	botao_sortear.place(x=320, y=220)
	
def sortear():

	def sorteiodebola():
		ball=(randint(1, 80))
		return ball
		

	bola=sorteiodebola()
	
	if bola not in listabolas:
		listabolas.append(bola)
		print(bola)

		labelbola1["text"] = bola  #Ultima bola
		
		labelbola = Label(janela, wraplength=750, text= sorted(listabolas)) #todas bolas chamadas
		labelbola.place(x=40, y=320)
				
		lbcontador["text"]=len(listabolas) #contador de bola
		
		lbpenultimo["text"]= listabolas[-2]#pega o penultimo elemento da lista
	else:
		sortear()

janela = Tk()
photo_bingo = PhotoImage(file='bingo.png')
label_phobingo = Label(janela, image = photo_bingo).pack()

#Botão iniciar
botao_iniciar = Button(janela, width= 7, text='INICIAR', command=iniciar)
botao_iniciar.place(x=420, y=220)

#Bola pricipal
labelbola1 = Label(janela, text= '??', font= 'impact 60 bold')
labelbola1.place(x=350, y=100)

#Contador de bolas
lbcontador = Label(janela, text= '0', font= 'impact 20 bold')
lbcontador.place(x= 100, y= 150)
qtdbolas= Label(janela, text="Contador de Bolas")
qtdbolas.place(x=90, y=190)

#Penultimo número
lbpenultimo = Label(janela, text="?", font= 'impact 30 bold')
lbpenultimo.place(x=600, y=100)
titulo_penultimo= Label(janela, text='Penúltimo')
titulo_penultimo.place(x=590, y=140)

#Titulo para bolas chamadas
bolaschamadas = Label(janela, text='Bolas Chamadas')
bolaschamadas.place(x=30, y=370)

#Janela Principal
janela.title('BINGO')
janela.geometry('800x400+100+100')
janela.mainloop()

#(x) Verificar numeros de um digito 
#(x) Mostrar penultimo numero lista
#(x) Ordenar lista
#( ) Adicionar musica
#(x) Adicionar um contador de numeros
#(x) Diminuir os clicks
#( ) Limpeza de tela e destruição de botões
#( ) Quebra de pagina para Label
#( ) Criar Executavel

