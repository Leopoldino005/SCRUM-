



















































































































  self.lb_nome.place(relx=0.008, rely=0.19

  self.nome_entry = Entry(self.aba1)
  self.nome_entry.place(relx=0.008, rely=0.27, relwidth=0.46, relheight=0.08)
                   
  # Criação da Label e Entrada do Telefone
  self.lb_telefone = Label(self.aba1, text="Telefone", bg="#363636", fg "#808080", font = ("Trebouchet", 10))
  self.lb_telefone.place(relx=0.008, rely=0.35)

  self.telefone_entry = Entry(self.aba1)
  self.telefone_entry.place(relx=0.008, rely=0.43, relwidth=0.20, relheight=0.08)

  # Criação da Label e Entrada do Cidade
  self.lb_cidade = Label(self.aba1, text="Cidade", bg="#363636", fg= "#808080", font = ("Trebouchet", 10))
  self.lb_cidade.place(relx=0.25, rely=0.35)
                   
  self.cidade_entry = Entry(self.aba1)
  self.cidade_entry.place(relx=0.25, rely=0.43, relwidth=0.22, relheight=0.08)

  # Menu Dropdown
  self.Tipvar = StringVar()
  self.TipV = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)")
  self.Tipvar.set("Estado civil")

  self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
  self.popupMnu.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.15)
  self.estado_civil = self.Tipvar.get()
 def lista_frame2(self):
  self.listaCli = ttk.Treeview(self.frame_2, height = 3, column = ("col1", "col2", "col3", "col4"))
  self.listaCli.place(relx = 0.01, rely = 0.05, relwidth = 0.98, relheigth = 0.9)
  self.listaCli.heading("#0", text = " ")
                 
    
