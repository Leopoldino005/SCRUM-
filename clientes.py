from modulos import *
from valida import Validadores
from reports import Relatorios
from funcionalidades import Funcs

root = tix.Tk()

class App(Funcs, Relatorios, Validadores):
    def __init__(Self):
        self.root = root
        self.images_base64()
        self.validaEntradas()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.monta_tabelas()
        self.select_lista()
        self.Menus()
        root.mainLoop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background = "#1C1C1C")
        self.root.geometry("700x500")
        self.state("zoomed")
        self.root.resizable(True, True)
        self.root.minsize(width = 700, height = 500)
        self.root.iconbitmap("icocli.ico")























































































































   self.listaCli.heading("#1", text= "Código")
   self.listaCli.heading("#2", text= "Nome")
   self.listaCli.heading("#3", text= "Telefone")
   self.listaCli.heading("#4", text= "Cidade")
    
   self.listaCli.column('#0', stretch=YES, minwidth=0,   width=0, anchor="center")
   self.listaCli.column('#1', stretch=YES, minwidth=40,  width=50, anchor="center")
   self.listaCli.column('#2', stretch=YES, minwidth=250, width=800, anchor="nw")
   self.listaCli.column('#3', stretch=YES, minwidth=100, width=190, anchor="nw")
   self.listaCli.column('#4', stretch=YES, minwidth=120, width=250, anchor="nw")
   
   self.barra_de_rolagem= scrollbar(self.frame_2, orient= "vertical")
   self.listaCli.configure(yscroll= self.barra_de_rolagem.set)
   self.barra_de_rolagem.place(relx=0.98, rely=0.052, relheight= 0.8962)
   
   self.listaCli.bind("<Double-1>", self.onDoubleClick)
 def Menus(self):
   menubar= Menu(self.root)
   self.root.config(menu=menubar)
   filemenu= Menu(menubar, tearoff=0)
   filemenu2= Menu(menubar, tearoff=0)
  
   def quit():
      self.root.destroy()
   
   menubar.add_cascade(label= "Opções", menu= filemenu)
   menubar.add_cascade(label="Relatórios", menu= filemenu2)
   
   filemenu.add_command(label="Limpa Cliente", command=self.limpa_tela)
   filemenu.add_command(label="Sair", command=quit)
    

