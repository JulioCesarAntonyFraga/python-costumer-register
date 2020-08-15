import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
import os
import sys
py = sys.executable
####################TELA INICIAL##########################

mainWindow = Tk()
mainWindow.a = StringVar()
mainWindow.b = StringVar()
mainWindow.maxsize(1366, 768)
mainWindow.minsize(1366, 768)
mainWindow.state("zoomed")
mainWindow.iconbitmap(r'icone_mel.ico')
mainWindow.canvas = Canvas(width=1366, height=768, bg='blue')
mainWindow.canvas.pack()
mainWindow.photo = PhotoImage(file='bg_init.png')
mainWindow.canvas.create_image(0, 0, image=mainWindow.photo, anchor=NW)
mainWindow.title('Iniciar')


###############################FUNÇÃO PARA INICIAR O PROGRAMA#############################
def entrar_no_programa():

    mainWindow.destroy()

    painelWindow = Tk()
    painelWindow.iconbitmap(r'icone_mel.ico')
    painelWindow.configure(bg='light blue')
    painelWindow.maxsize(1366, 768)
    painelWindow.minsize(1366, 768)
    painelWindow.state('zoomed')
    painelWindow.title("Mel's")
    painelWindow.canvas = Canvas(width=1366, height=768, bg='blue')
    painelWindow.canvas.pack()
    painelWindow.photo = PhotoImage(file='bg_mel.png')
    painelWindow.canvas.create_image(0, 0, image=painelWindow.photo, anchor=NW)
    painelWindow.title("Mel's")
    painelWindow.a = StringVar()
    painelWindow.b = StringVar()

    ###########################FUNÇÕES CHAMANDO AS JANELAS DE ADD E REMOVER...#########################
    def a_s():
        # creating window
        cadastroWindow = Toplevel()
        cadastroWindow.iconbitmap(r'icone_mel.ico')
        cadastroWindow.maxsize(500, 500)
        cadastroWindow.minsize(500, 500)
        cadastroWindow.title('Cadastro')
        cadastroWindow.photo = PhotoImage(file='bg_addHorario.png')
        cadastroWindow.myLabel = Label(cadastroWindow, image = cadastroWindow.photo)
        cadastroWindow.myLabel.place(x=0,y=0)

        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()

        ######################FUNÇÃO SEGURANÇÃO ID##################
        def segura():
            try:
                a = random.randrange(1000, 9999)
                cadastroWindow.conn = sqlite3.connect('library_administration.db')
                cadastroWindow.myCursor = cadastroWindow.conn.cursor()
                cadastroWindow.myCursor.execute(
                    "INSERT INTO clientes('Id', 'Nome', 'Telefone', 'Instagram', 'Idade') values (?,?,?,?,?)",
                    [a, b.get(), c.get(), d.get(), e.get()])
                cadastroWindow.conn.commit()
                messagebox.showinfo('Info', 'Sucesso ao agendar um cliente')
                cadastroWindow.destroy()
            except:
                segura()

        #################FUNÇÃO PARA VERIFICAR AS INFORMAÇÕES##############
        def b_q():
            try:
                options = []
                cadastroWindow.conn = sqlite3.connect('library_administration.db')
                cadastroWindow.myCursor = cadastroWindow.conn.cursor()
                cadastroWindow.myCursor.execute("SELECT Id FROM clientes")
                pc = cadastroWindow.myCursor.fetchall()
                options = pc
                a = random.randrange(1000, 9999)
                print(a)
            except Error as erro:
                print(erro)
            if len(b.get()) == 0:
                messagebox.showerror("Erro", "Preencha pelo menos o nome")
            else:
                try:
                    cadastroWindow.conn = sqlite3.connect('library_administration.db')
                    cadastroWindow.myCursor = cadastroWindow.conn.cursor()
                    cadastroWindow.myCursor.execute(
                        "INSERT INTO clientes('Id', 'Nome', 'Telefone', 'Instagram', 'Idade') values (?,?,?,?,?)",
                        [a, b.get(), c.get(), d.get(), e.get()])
                    cadastroWindow.conn.commit()
                    messagebox.showinfo('Info', 'Sucesso ao agendar um cliente')
                    cadastroWindow.destroy()
                except Error as erro:
                    print(erro)
                    segura()

        def sair():
            cadastroWindow.destroy()

        ##########################LABELS BOTOES E ENTRY DA JANELA ADICIONAR CLIENTE###############################
        label = Label(cadastroWindow, bd=2, width=15, relief='ridge', text='Nome:').place(x=70, y=130)
        S_name = Entry(cadastroWindow, textvariable=b, width=30).place(x=200, y=132)
        label5 = Label(cadastroWindow, bd=2, relief='ridge', width=15, text='Telefone:').place(x=70, y=180)
        S_ID = Entry(cadastroWindow, textvariable=c, width=30).place(x=200, y=182)
        label6 = Label(cadastroWindow, bd=2, relief='ridge', width=15, text='Instagram:').place(x=70, y=230)
        S_Class = Entry(cadastroWindow, textvariable=d, width=30).place(x=200, y=232)
        label7 = Label(cadastroWindow, bd=2, relief='ridge', width=15, text='Aniversário:').place(x=70, y=280)
        S_phone_number = Entry(cadastroWindow, textvariable=e, width=30).place(x=200, y=282)
        S_butt = Button(cadastroWindow, bd=3, text="Cadastrar", width=25, command=b_q).place(x=200, y=340)
        Sair_butt = Button(cadastroWindow, bd=3, text="Sair", width=14, command=sair).place(x=72, y=340)

    def e_c():
        editarClienteWindow = Toplevel()
        editarClienteWindow.iconbitmap(r'icone_mel.ico')
        editarClienteWindow.maxsize(1300, 500)
        editarClienteWindow.minsize(1300, 500)
        editarClienteWindow.state('zoomed')
        editarClienteWindow.title('Editar cliente')
        editarClienteWindow.photo = PhotoImage(file='bg_editClientes.png')
        editarClienteWindow.myLabel = Label(editarClienteWindow, image=editarClienteWindow.photo)
        editarClienteWindow.myLabel.place(x=0, y=0)

        f = StringVar()
        g = StringVar()

        #####################################FUNÇÃO PARA OS VALORES APARECEREM NA LISTBOX#############################
        def insert(data):
            listTree.delete(*listTree.get_children())
            for row in data:
                listTree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4]))

        ##################FUNÇÃO PARA SELECIONAR O TEXTO NA LISTBOX #########################
        def select(a):
            curItem = listTree.focus()
            selItem = listTree.item(curItem)

        ##################FUNÇÃO PARA SAIR ###################################
        def sair():
            editarClienteWindow.destroy()

        ##############FUNÇÃO PARA SEPARAR OS TOPICOS DA LIST############################
        def handle(event):
            if listTree.identify_region(event.x, event.y) == "separator":
                return "break"

        ##################LABELS TITULOS E CONFIGURAÇOES DA LIST#############################
        listTree = ttk.Treeview(editarClienteWindow, height=7, columns=('Nome', 'Telefone', 'Instagram', 'Idade'))
        vsb = ttk.Scrollbar(editarClienteWindow, orient="vertical", command=listTree.yview)
        listTree.configure(yscrollcommand=vsb.set)
        listTree.heading("#0", text='ID', anchor='w')
        listTree.column("#0", width=130, anchor='w')
        listTree.heading("Nome", text='Nome')
        listTree.column("Nome", width=170, anchor='center')
        listTree.heading("Telefone", text='Telefone')
        listTree.column("Telefone", width=200, anchor='center')
        listTree.heading("Instagram", text='Instagram')
        listTree.column("Instagram", width=200, anchor='center')
        listTree.heading("Idade", text='Aniversário')
        listTree.column("Idade", width=100, anchor='center')
        listTree.bind("<Button-1>", handle)
        listTree.bind("<ButtonRelease-1>", select)
        listTree.place(x=460, y=200)
        vsb.place(x=1263, y=200, height=168)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

        ####################FUNÇÃO PARA BUSCAR CLIENTES##################################
        def buscar_todos():
            try:
                i = ''
                editarClienteWindow.conn = sqlite3.connect('library_administration.db')
                editarClienteWindow.mycursor = editarClienteWindow.conn.cursor()
                editarClienteWindow.mycursor.execute("Select * from clientes")
                pc = editarClienteWindow.mycursor.fetchall()

                if pc:
                    try:
                        insert(pc)
                    except EXCEPTION:
                        messagebox.showinfo("Alerta", "Nenhum cliente encontrado")
            except EXCEPTION:
                messagebox.showinfo("Alerta", "Não foi possível buscar todos os clientes")

        ##############FUNÇÃO PARA FAZER A BUSCA#################################
        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Erro', 'Selecione o tipo de busca')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Erro', 'Digite o ' + g.get())
            elif g.get() == 'ID':
                try:
                    editarClienteWindow.conn = sqlite3.connect('library_administration.db')
                    editarClienteWindow.mycursor = editarClienteWindow.conn.cursor()
                    editarClienteWindow.mycursor.execute("Select * from clientes where Id like ?", ['%' + f.get() + '%'])
                    pc = editarClienteWindow.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Alerta", "Id não encontrado")
                except Error:
                    messagebox.showerror("Alerta", "Algum erro ocorreu")
            elif g.get() == 'Nome':
                try:
                    editarClienteWindow.conn = sqlite3.connect('library_administration.db')
                    editarClienteWindow.mycursor = editarClienteWindow.conn.cursor()
                    editarClienteWindow.mycursor.execute("Select * from clientes where Nome like ?", ['%' + f.get() + '%'])
                    pc = editarClienteWindow.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Alerta", "Nome não encontrado")
                except Error:
                    messagebox.showerror("Alerta", "Algum erro ocorreu")
            elif g.get() == 'Telefone':
                try:
                    editarClienteWindow.conn = sqlite3.connect('library_administration.db')
                    editarClienteWindow.mycursor = editarClienteWindow.conn.cursor()
                    editarClienteWindow.mycursor.execute("Select * from clientes where Telefone like ?", ['%' + f.get() + '%'])
                    pc = editarClienteWindow.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Alerta", "Telefone não encontrado")
                except Error:
                    messagebox.showerror("Erro", "Algum erro ocorreu")

        ##################LABELS E BOTOES E ENTRY DA JANELA BUSCAR CLIENTES########################
        b = Button(editarClienteWindow, bd=3, relief='raised', text="Buscar", width=15, command=ge).place(x=460, y=82)
        b = Button(editarClienteWindow, bd=3, relief='raised', text="Buscar Todos", width=15, command=buscar_todos).place(x=460, y=134)

        c = ttk.Combobox(editarClienteWindow, textvariable=g, values=["ID", "Nome", "Telefone"], width=40,
                         state="readonly").place(x=620, y=82)
        en = Entry(editarClienteWindow, textvariable=f, width=43).place(x=620, y=137)

        #################FUNÇÃO PARA VERIFICAR AS INFORMAÇÕES E MANDAR PRO BANCO DE DADOS##################
        def asi():
            try:
                editarClienteWindow.conn = sqlite3.connect('library_administration.db')
                editarClienteWindow.myCursor = editarClienteWindow.conn.cursor()
                editarClienteWindow.myCursor.execute(
                    "REPLACE into clientes('Id','Nome','Telefone','Instagram', 'Idade') values (?,?,?,?,?)",
                    [a.get(), b.get(), c.get(), d.get(), e.get()])
                messagebox.showinfo('Alerta', 'Sucesso ao editar cliente')
                editarClienteWindow.conn.commit()
                editarClienteWindow.myCursor.close()
                editarClienteWindow.conn.close()
            except Error as erro:
                print(erro)
                messagebox.showerror("Alerta", "Não foi possível editar ou foi digitado incorretamente")

        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()

        ##########################LABELS BOTOES E ENTRY DA JANELA ADICIONAR CLIENTE###############################
        lbl = Label(editarClienteWindow, bd=2, width=15, relief='ridge', text='ID do cliente:').place(x=30, y=82)
        S_name = Entry(editarClienteWindow, textvariable=a, width=30).place(x=150, y=84)
        label = Label(editarClienteWindow, bd=2, width=15, relief='ridge', text='Novo Nome:').place(x=30, y=130)
        S_name = Entry(editarClienteWindow, textvariable=b, width=30).place(x=150, y=132)
        label5 = Label(editarClienteWindow, bd=2, relief='ridge', width=15, text='Novo Telefone:').place(x=30, y=180)
        S_ID = Entry(editarClienteWindow, textvariable=c, width=30).place(x=150, y=182)
        label6 = Label(editarClienteWindow, bd=2, relief='ridge', width=15, text='Novo Instagram:').place(x=30, y=230)
        S_Class = Entry(editarClienteWindow, textvariable=d, width=30).place(x=150, y=232)
        label7 = Label(editarClienteWindow, bd=2, relief='ridge', width=15, text='Nova Idade').place(x=30, y=280)
        S_phone_number = Entry(editarClienteWindow, textvariable=e, width=30).place(x=150, y=282)
        S_butt = Button(editarClienteWindow, bd=3, text="Confirmar", width=25, command=asi).place(x=150, y=340)
        Sair_butt = Button(editarClienteWindow, bd=3, text="Sair", width=14, command=sair).place(x=30, y=340)

    def a_b():
        # creating window
        addHorarioWindow = Toplevel()
        addHorarioWindow.iconbitmap(r'icone_mel.ico')
        addHorarioWindow.maxsize(500, 500)
        addHorarioWindow.minsize(500, 500)
        addHorarioWindow.title('Adicionar Horário')
        addHorarioWindow.photo = PhotoImage(file='bg_addHorario.png')
        addHorarioWindow.myLabel = Label(addHorarioWindow, image=addHorarioWindow.photo)
        addHorarioWindow.myLabel.place(x=0, y=0)

        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()
        f = StringVar()

        ######################FUNÇÃO SEGURANÇÃO ID##################
        def segura():
            try:
                a = random.randrange(1000, 9999)
                addHorarioWindow.conn = sqlite3.connect('library_administration.db')
                addHorarioWindow.myCursor = addHorarioWindow.conn.cursor()
                addHorarioWindow.myCursor.execute(
                    "INSERT INTO horarios('Id', 'Horario', 'Data', 'Tipo', 'Cliente', 'Valor') values (?,?,?,?,?,?)",
                    [a, b.get() + 'h', c.get(), d.get(), e.get(), 'R$' + f.get()])
                addHorarioWindow.conn.commit()
                messagebox.showinfo('Info', 'Sucesso ao agendar um horário')
                addHorarioWindow.destroy()
            except:
                segura()

        #################FUNÇÃO PARA VERIFICAR AS INFORMAÇÕES##############
        def b_q():
            try:
                options = []
                addHorarioWindow.conn = sqlite3.connect('library_administration.db')
                addHorarioWindow.myCursor = addHorarioWindow.conn.cursor()
                addHorarioWindow.myCursor.execute("SELECT Id FROM horarios")
                pc = addHorarioWindow.myCursor.fetchall()
                options = pc
                a = random.randrange(1000, 9999)
                print(a)
            except Error as erro:
                print(erro)
            if len(b.get()) == 0 or len(b.get()) == 0:
                messagebox.showerror("Erro", "Preencha pelo menos o horario e a data")
            else:
                try:
                    addHorarioWindow.conn = sqlite3.connect('library_administration.db')
                    addHorarioWindow.myCursor = addHorarioWindow.conn.cursor()
                    addHorarioWindow.myCursor.execute(
                        "INSERT INTO horarios('Id', 'Horario', 'Data', 'Tipo', 'Cliente', 'Valor') values (?,?,?,?,?,?)",
                        [a, b.get() + 'h', c.get(), d.get(), e.get(), 'R$' + f.get()])
                    addHorarioWindow.conn.commit()
                    messagebox.showinfo('Info', 'Sucesso ao agendar um horário')
                    addHorarioWindow.destroy()
                except Error as erro:
                    print(erro)
                    segura()

        ################LABEL AO LADO DAS CAIXA DE TEXTO DA JANELA ADD HORARIOS######################
        Label(addHorarioWindow, width=15,text='Cliente:', font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=115)
        options = []

        addHorarioWindow.conn = sqlite3.connect('library_administration.db')
        addHorarioWindow.mycursor = addHorarioWindow.conn.cursor()
        addHorarioWindow.mycursor.execute("SELECT Nome FROM clientes")
        pc = addHorarioWindow.mycursor.fetchall()

        str(pc)

        options = pc


        ggggg = ttk.Combobox(addHorarioWindow, textvariable=e, values=[*options], width=27, state="readonly").place(x=230,
                                                                                                        y=115)

        Label(addHorarioWindow, text='Horário:', width=15,font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=160)
        Entry(addHorarioWindow, textvariable=b, width=30).place(x=230, y=160)
        Label(addHorarioWindow, text='Data:',width=15 ,font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=205)
        Entry(addHorarioWindow, textvariable=c, width=30).place(x=230, y=205)
        Label(addHorarioWindow, text='Tipo:', width=15,font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=252)
        Entry(addHorarioWindow, textvariable=d, width=30).place(x=230, y=252)
        Button(addHorarioWindow, bd=4, text="Agendar", width=45, command=b_q).place(x=100, y=350)
        Label(addHorarioWindow, text='Valor:',width=15, font=('Comic Scan Ms', 10, 'bold')).place(x=100, y=300)
        Entry(addHorarioWindow, textvariable=f, width=30).place(x=230, y=300)

    def e_h():
        #############################INICIO DA JANELA BUSCAR HORARIO###########################
        editarHorarioWindow = Toplevel()
        editarHorarioWindow.iconbitmap(r'icone_mel.ico')
        editarHorarioWindow.maxsize(1300, 500)
        editarHorarioWindow.minsize(1300, 500)
        editarHorarioWindow.state('zoomed')
        editarHorarioWindow.title('Editar Horário')
        editarHorarioWindow.photo = PhotoImage(file='bg_editClientes.png')
        editarHorarioWindow.myLabel = Label(editarHorarioWindow, image=editarHorarioWindow.photo)
        editarHorarioWindow.myLabel.place(x=0, y=0)

        f = StringVar()
        g = StringVar()

        #####################################FUNÇÃO PARA OS VALORES APARECEREM NA LISTBOX#############################
        def insert(data):
            listTree.delete(*listTree.get_children())
            for row in data:
                listTree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))

        ##################FUNÇÃO PARA SELECIONAR O TEXTO NA LISTBOX #########################
        def select(a):
            curItem = listTree.focus()
            selItem = listTree.item(curItem)

        ##################FUNÇÃO PARA SAIR ###################################
        def sair():
            editarHorarioWindow.destroy()

        ##############FUNÇÃO PARA SEPARAR OS TOPICOS DA LIST############################
        def handle(event):
            if listTree.identify_region(event.x, event.y) == "separator":
                return "break"

        ##################LABELS TITULOS E CONFIGURAÇOES DA LIST#############################
        listTree = ttk.Treeview(editarHorarioWindow, height=7, columns=('Horário', 'Data', 'Tipo', 'Cliente', 'Valor'))
        vsb = ttk.Scrollbar(editarHorarioWindow, orient="vertical", command=listTree.yview)
        listTree.configure(yscrollcommand=vsb.set)
        listTree.heading("#0", text='ID', anchor='w')
        listTree.heading("Horário", text='Horário')
        listTree.column("Horário", width=150, anchor='center')
        listTree.column("#0", width=130, anchor='w')
        listTree.heading("Data", text='Data')
        listTree.column("Data", width=150, anchor='center')
        listTree.heading("Tipo", text='Tipo')
        listTree.column("Tipo", width=130, anchor='center')
        listTree.heading("Cliente", text='Cliente')
        listTree.column("Cliente", width=140, anchor='center')
        listTree.heading("Valor", text='Valor')
        listTree.column("Valor", width=100, anchor='center')
        listTree.bind("<Button-1>", handle)
        listTree.bind("<ButtonRelease-1>", select)
        listTree.place(x=460, y=240)
        vsb.place(x=1263, y=240, height=168)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

        ####################FUNÇÃO PARA BUSCAR CLIENTES##################################
        def buscar_todos():
            i = ''
            editarHorarioWindow.conn = sqlite3.connect('library_administration.db')
            editarHorarioWindow.mycursor = editarHorarioWindow.conn.cursor()
            editarHorarioWindow.mycursor.execute("Select * from horarios where Id like ?", ['%' + i + '%'])
            pc = editarHorarioWindow.mycursor.fetchall()
            if pc:
                insert(pc)
            else:
                messagebox.showinfo("Alerta", "Não foi possível buscar todos os horários")

        ##############FUNÇÃO PARA FAZER A BUSCA#################################
        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Erro', 'Selecione o tipo de busca')
            elif g.get() == 'Tipo':
                try:
                    editarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                    editarHorarioWindow.mycursor = editarHorarioWindow.conn.cursor()
                    editarHorarioWindow.mycursor.execute("Select * from horarios where Tipo like ?", ['%' + f.get() + '%'])
                    pc = editarHorarioWindow.mycursor.fetchall()
                    editarHorarioWindow.conn.close()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Alerta", "Tipo não encontrado")
                except Error:
                    messagebox.showerror("Alerta", "Algum erro ocorreu")
            elif g.get() == 'Data':
                try:
                    editarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                    editarHorarioWindow.mycursor = editarHorarioWindow.conn.cursor()
                    editarHorarioWindow.mycursor.execute("Select * from horarios where Data like ?", ['%' + f.get() + '%'])
                    pc = editarHorarioWindow.mycursor.fetchall()
                    editarHorarioWindow.conn.close()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Alerta", "Data não encontrada")
                except Error:
                    messagebox.showerror("Erro", "Algum erro ocorreu")

            elif g.get() == 'Cliente':
                try:
                    editarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                    editarHorarioWindow.mycursor = editarHorarioWindow.conn.cursor()
                    editarHorarioWindow.mycursor.execute("Select * from horarios where Cliente like ?", ['%' + f.get() + '%'])
                    pc = editarHorarioWindow.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Alerta", "Cliente não encontrada")
                except Error:
                    messagebox.showerror("Erro", "Algum erro ocorreu")

        ##################LABELS E BOTOES E ENTRY DA JANELA BUSCAR CLIENTES########################
        b = Button(editarHorarioWindow, bd=3, relief='raised', text="Buscar", width=15, command=ge).place(x=460, y=82)
        b = Button(editarHorarioWindow, bd=3, relief='raised', text="Buscar Todos", width=15, command=buscar_todos).place(
            x=460, y=134)
        c = ttk.Combobox(editarHorarioWindow, textvariable=g, values=["Data", "Tipo","Cliente"], width=40, state="readonly").place(x=620,y=82)

        en = Entry(editarHorarioWindow, textvariable=f, width=43).place(x=620, y=137)

        #################FUNÇÃO PARA VERIFICAR AS INFORMAÇÕES E MANDAR PRO BANCO DE DADOS##################
        def asi():
            if len(b.get()) < 1:
                messagebox.showinfo("Alerta", "Por favor digite o horário que deseja editar")
            else:
                try:
                    editarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                    editarHorarioWindow.myCursor = editarHorarioWindow.conn.cursor()
                    editarHorarioWindow.myCursor.execute(
                        "REPLACE into horarios('Id','Horario','Data','Tipo','Cliente', 'Valor') values (?,?,?,?,?,?)",
                        [a.get(), b.get() + 'h', c.get(), d.get(), e.get(), 'R$' + f.get()])
                    messagebox.showinfo('Alerta', 'Horário editado com sucesso')
                    editarHorarioWindow.conn.commit()
                    editarHorarioWindow.myCursor.close()
                    editarHorarioWindow.conn.close()
                except Error as erro:
                    print(erro)
                    messagebox.showerror("Alerta", "Não foi possível editar ou foi digitado incorretamente")

        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()
        e = StringVar()


        ##########################LABELS BOTOES E ENTRY DA JANELA ADICIONAR CLIENTE###############################
        lbl = Label(editarHorarioWindow, bd=2, width=15, relief='ridge', text='Id Do Horário:').place(x=30, y=82)
        S_name = Entry(editarHorarioWindow, textvariable=a, width=30).place(x=150, y=82)
        lbl = Label(editarHorarioWindow, bd=2, width=15, relief='ridge', text='Novo Horário:').place(x=30, y=130)
        S_name = Entry(editarHorarioWindow, textvariable=b, width=30).place(x=150, y=130)
        label = Label(editarHorarioWindow, bd=2, width=15, relief='ridge', text='Nova Data:').place(x=30, y=180)
        S_name = Entry(editarHorarioWindow, textvariable=c, width=30).place(x=150, y=180)
        label5 = Label(editarHorarioWindow, bd=2, relief='ridge', width=15, text='Novo Tipo:').place(x=30, y=230)
        S_ID = Entry(editarHorarioWindow, textvariable=d, width=30).place(x=150, y=230)
        label6 = Label(editarHorarioWindow, bd=2, relief='ridge', width=15, text='Novo Cliente:').place(x=30, y=280)

        options = []
        editarHorarioWindow.conn = sqlite3.connect('library_administration.db')
        editarHorarioWindow.mycursor = editarHorarioWindow.conn.cursor()
        editarHorarioWindow.mycursor.execute("SELECT Nome FROM clientes")
        pc = editarHorarioWindow.mycursor.fetchall()
        options = pc
        ggggg = ttk.Combobox(editarHorarioWindow, textvariable=e, values=[*options], width=27, state="readonly").place(x=150,
                                                                                                        y=280)

        label7 = Label(editarHorarioWindow, bd=2, relief='ridge', width=15, text='Novo Valor').place(x=30, y=330)
        S_phone_number = Entry(editarHorarioWindow, textvariable=f, width=30).place(x=150, y=330)
        S_butt = Button(editarHorarioWindow, bd=3, text="Confirmar", width=25, command=asi).place(x=150, y=380)
        Sair_butt = Button(editarHorarioWindow, bd=3, text="Sair", width=14, command=sair).place(x=30, y=380)

    def a_h():
        #############################INICIO DA JANELA BUSCAR CLIENTES###########################
        buscarHorarioWindow = Toplevel()
        f = StringVar()
        g = StringVar()
        buscarHorarioWindow.title("Histórico")
        buscarHorarioWindow.maxsize(1000, 500)
        buscarHorarioWindow.minsize(1000, 500)
        buscarHorarioWindow.iconbitmap(r'icone_mel.ico')
        buscarHorarioWindow.photo = PhotoImage(file='bg_pHor.png')
        buscarHorarioWindow.myLabel = Label(buscarHorarioWindow, image=buscarHorarioWindow.photo)
        buscarHorarioWindow.myLabel.place(x=0, y=0)

        #####################################FUNÇÃO PARA OS VALORES APARECEREM NA LISTBOX#############################
        def insert(data):
            buscarHorarioWindow.listTree.delete(*buscarHorarioWindow.listTree.get_children())
            for row in data:
                buscarHorarioWindow.listTree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))

        ##########################FUNÇÃO PARA BUSCAR TODOS CLIENTES######################################
        def buscar_todos():
            try:
                i = ''
                buscarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                buscarHorarioWindow.mycursor = buscarHorarioWindow.conn.cursor()
                buscarHorarioWindow.mycursor.execute("Select * from historico where Id like ?", ['%' + i + '%'])
                pc = buscarHorarioWindow.mycursor.fetchall()
                print(pc)
                if pc:
                    try:
                        insert(pc)
                    except EXCEPTION:
                        messagebox.showinfo("Alerta", "Nenhum histórico encontrado")
            except EXCEPTION:
                messagebox.showinfo("Alerta", "Não foi possível buscar todos os clientes")

        ##################FUNÇÃO PARA SELECIONAR O TEXTO NA LISTBOX #########################
        def select(a):
            curItem = buscarHorarioWindow.listTree.focus()
            selItem = buscarHorarioWindow.listTree.item(curItem)
            pic = str(selItem['text'])

        ##############FUNÇÃO PARA FAZER A BUSCA#################################
        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Erro', 'Selecione o tipo de busca')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Erro', 'Digite o ' + g.get())
            elif g.get() == 'ID':
                try:
                    buscarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                    buscarHorarioWindow.mycursor = buscarHorarioWindow.conn.cursor()
                    buscarHorarioWindow.mycursor.execute("Select * from historico where Id like ?", ['%' + f.get() + '%'])
                    pc = buscarHorarioWindow.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Alerta", "Id não encontrado")
                except Error:
                    messagebox.showerror("Alerta", "Algum erro ocorreu")
            elif g.get() == 'Cliente':
                try:
                    buscarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                    buscarHorarioWindow.mycursor = buscarHorarioWindow.conn.cursor()
                    buscarHorarioWindow.mycursor.execute("Select * from historico where Cliente like ?", ['%' + f.get() + '%'])
                    pc = buscarHorarioWindow.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Alerta", "Nome não encontrado")
                except Error:
                    messagebox.showerror("Alerta", "Algum erro ocorreu")
            elif g.get() == 'Tipo':
                try:
                    buscarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                    buscarHorarioWindow.mycursor = buscarHorarioWindow.conn.cursor()
                    buscarHorarioWindow.mycursor.execute("Select * from historico where Tipo like ?",
                                                    ['%' + f.get() + '%'])
                    pc = buscarHorarioWindow.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Alerta", "Telefone não encontrado")
                except Error:
                    messagebox.showerror("Erro", "Algum erro ocorreu")

        def aaa():
            if len(a.get()) == 0:
                messagebox.showerror("Erro", "Por favor digite o cliente que deseja excluir")
            else:
                c = messagebox.askyesno('Alerta', 'Você tem certeza que deseja deletar esse horário ?')
                if c:
                    try:
                        buscarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                        buscarHorarioWindow.mycursor = buscarHorarioWindow.conn.cursor()
                        pc = buscarHorarioWindow.mycursor.execute("DELETE FROM historico WHERE Id = ?", [a.get()])
                        buscarHorarioWindow.conn.commit()
                        if pc:
                            messagebox.showinfo("Alerta", "Sucesso ao deletar")
                            buscarHorarioWindow.destroy()
                        else:
                            messagebox.showerror("Erro",
                                                 "Este cliente não existe ou foi digitado incorretamente")
                    except Error:
                        messagebox.showerror("Erro", "Algo de errado ocorreu")
                    except Error as erro:
                        print(erro)
                        messagebox.showerror("Erro", "Algum erro ocorreu")

        ##################LABELS E BOTOES E ENTRY DA JANELA BUSCAR CLIENTES########################
        b1 = Button(buscarHorarioWindow, bd=3, relief='raised', text="Deletar", width=14, font=("Arial", 10, 'bold'),
                    command=aaa).place(x=860, y=160)
        b2 = Button(buscarHorarioWindow, bd=3, relief='raised', font=("Arial", 10, 'bold'), text="Buscar", width=28,
                    command=ge).place(x=190, y=164)
        c = ttk.Combobox(buscarHorarioWindow, textvariable=g, values=["ID", "Cliente", "Tipo"], width=35,
                         state="readonly").place(x=190, y=90)
        en = Entry(buscarHorarioWindow, textvariable=f, width=38).place(x=190, y=140)

        ##############FUNÇÃO PARA SEPARAR OS TOPICOS DA LIST############################
        def handle(event):
            if buscarHorarioWindow.listTree.identify_region(event.x, event.y) == "separator":
                return "break"

        ##################LABELS TITULOS E CONFIGURAÇOES DA LIST#############################
        buscarHorarioWindow.listTree = ttk.Treeview(buscarHorarioWindow, height=13,columns=('Horários Marcados', 'Datas Marcadas', 'Tipo', 'Clientes', 'Valor'))
        buscarHorarioWindow.vsb = ttk.Scrollbar(buscarHorarioWindow, orient="vertical", command=buscarHorarioWindow.listTree.yview)
        buscarHorarioWindow.listTree.configure(yscrollcommand=buscarHorarioWindow.vsb.set)
        buscarHorarioWindow.listTree.heading("#0", text='ID', anchor='w')
        buscarHorarioWindow.listTree.column("#0", width=100, anchor='w')
        buscarHorarioWindow.listTree.heading("Horários Marcados", text='Horários Marcados')
        buscarHorarioWindow.listTree.column("Horários Marcados", width=150, anchor='center')
        buscarHorarioWindow.listTree.heading("Datas Marcadas", text='Datas Marcadas')
        buscarHorarioWindow.listTree.column("Datas Marcadas", width=200, anchor='center')
        buscarHorarioWindow.listTree.heading("Tipo", text='Tipo')
        buscarHorarioWindow.listTree.column("Tipo", width=190, anchor='center')
        buscarHorarioWindow.listTree.heading("Clientes", text='Clientes')
        buscarHorarioWindow.listTree.column("Clientes", width=200, anchor='center')
        buscarHorarioWindow.listTree.heading("Valor", text='Valor')
        buscarHorarioWindow.listTree.column("Valor", width=120, anchor='center')
        buscarHorarioWindow.listTree.bind("<Button-1>", handle)
        buscarHorarioWindow.listTree.bind("<ButtonRelease-1>", select)
        buscarHorarioWindow.listTree.place(x=10, y=200)
        buscarHorarioWindow.vsb.place(x=973, y=200, height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

        a = StringVar()

        lb = Label(buscarHorarioWindow, bd=6, text="Deletar histórico(ID):", font=("Arial", 10, 'bold'), relief='ridge',
                   width=23)
        lb.place(x=650, y=132)
        e = Entry(buscarHorarioWindow, textvariable=a, width=20).place(x=857, y=135)

        bt = Button(buscarHorarioWindow, bd=3, relief='raised', text="Mostrar Todos", width=35, font=("Arial", 10, 'bold'),
                    command=buscar_todos).place(x=10, y=50)

    def sair():
        painelWindow.destroy()

    def sea():
        ##################INICIO JANELA BUSCAR HORARIO#################
        buscarHorarioWindow = Toplevel()
        f = StringVar()
        g = StringVar()
        p = StringVar()
        buscarHorarioWindow.title("Buscar Horário")
        buscarHorarioWindow.maxsize(1000, 500)
        buscarHorarioWindow.minsize(1000, 500)
        buscarHorarioWindow.iconbitmap(r'icone_mel.ico')
        buscarHorarioWindow.photo = PhotoImage(file='bg_pHor.png')
        buscarHorarioWindow.myLabel = Label(buscarHorarioWindow, image=buscarHorarioWindow.photo)
        buscarHorarioWindow.myLabel.place(x=0, y=0)


        def insert(data):
            buscarHorarioWindow.listTree.delete(*buscarHorarioWindow.listTree.get_children())
            for row in data:
                buscarHorarioWindow.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))

        ##########################FUNÇÃO PARA BUSCAR TODOS CLIENTES######################################
        def buscar_todos():
            try:
                i = ''
                buscarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                buscarHorarioWindow.mycursor = buscarHorarioWindow.conn.cursor()
                buscarHorarioWindow.mycursor.execute("Select * from horarios where Horario like ?", ['%' + i + '%'])
                pc = buscarHorarioWindow.mycursor.fetchall()
                if pc:
                    try:
                        insert(pc)
                    except EXCEPTION:
                        messagebox.showinfo("Alerta", "Não existe horários agendados")
            except EXCEPTION:
                messagebox.showinfo("Alerta", "Não foi possível buscar todos os horários")

        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Erro', 'Primeiro selecione o tipo de busca')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Erro', 'Digite o Nome a Data ou o Tipo')
            elif g.get() == 'Data':
                try:
                    buscarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                    buscarHorarioWindow.mycursor = buscarHorarioWindow.conn.cursor()
                    buscarHorarioWindow.mycursor.execute("Select * from horarios where Data LIKE ?", ['%' + f.get() + '%'])
                    buscarHorarioWindow.pc = buscarHorarioWindow.mycursor.fetchall()
                    if buscarHorarioWindow.pc:
                        insert(buscarHorarioWindow.pc)
                    else:
                        messagebox.showinfo("Alerta", "Não foi possivel encontrar")
                except Error:
                    messagebox.showerror("Erro", "Algum erro ocorreu")
            elif g.get() == 'Tipo':
                try:
                    buscarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                    buscarHorarioWindow.mycursor = buscarHorarioWindow.conn.cursor()
                    buscarHorarioWindow.mycursor.execute("Select * from horarios where Tipo LIKE ?", ['%' + f.get() + '%'])
                    buscarHorarioWindow.pc = buscarHorarioWindow.mycursor.fetchall()
                    if buscarHorarioWindow.pc:
                        insert(buscarHorarioWindow.pc)
                    else:
                        messagebox.showinfo("Alerta", "Não foi possivel encontrar")
                except Error:
                    messagebox.showerror("Erro", "Não foi possivel encontrar")
            elif g.get() == 'Cliente':
                try:
                    buscarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                    buscarHorarioWindow.mycursor = buscarHorarioWindow.conn.cursor()
                    buscarHorarioWindow.mycursor.execute("Select * from horarios where Cliente LIKE ?", ['%' + f.get() + '%'])
                    buscarHorarioWindow.pc = buscarHorarioWindow.mycursor.fetchall()
                    if buscarHorarioWindow.pc:
                        insert(buscarHorarioWindow.pc)
                    else:
                        messagebox.showinfo("Alerta", "Não foi possivel encontrar")
                except Error:
                    messagebox.showerror("Erro", "Não foi possivel encontrar")

        def aaa():
            if len(a.get()) == 0:
                messagebox.showerror("Erro", "Por favor digite o horário que deseja excluir")
            else:
                c = messagebox.askyesno('Alerta', 'Você tem certeza que deseja deletar esse horário ?')
                if c == 1:
                    messagebox.showinfo("Alerta", "Sucesso ao deletar horário")
                    result = messagebox.askyesno(title='Alerta', message='Deseja salvar esse horário no seu histórico ?')
                    if result == 1:

                        buscarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                        buscarHorarioWindow.myCursor = buscarHorarioWindow.conn.cursor()

                        buscarHorarioWindow.myCursor.execute("SELECT * FROM horarios WHERE Id = " + a.get())

                        pc = buscarHorarioWindow.myCursor.fetchall()
                        print(pc[0][5])

                        buscarHorarioWindow.myCursor.execute("INSERT INTO historico('Id','Horario','Data','Tipo','Cliente', 'Valor') values (?,?,?,?,?,?)",[a.get(), pc[0][1], pc[0][2], pc[0][3], pc[0][4], pc[0][5]])

                        buscarHorarioWindow.myCursor.execute("DELETE FROM horarios WHERE Id = " + a.get())

                        messagebox.showinfo('Alerta', 'Horário salvado no histórico com sucesso')
                        buscarHorarioWindow.conn.commit()
                        buscarHorarioWindow.myCursor.close()
                    else:
                        buscarHorarioWindow.conn = sqlite3.connect('library_administration.db')
                        buscarHorarioWindow.myCursor = buscarHorarioWindow.conn.cursor()
                        buscarHorarioWindow.myCursor.execute("DELETE FROM horarios WHERE Id = " + a.get())
                        buscarHorarioWindow.conn.commit()
                        buscarHorarioWindow.myCursor.close()

        b1 = Button(buscarHorarioWindow, bd=2, relief='raised', text="Buscar", width=20, font=("Arial", 10, 'bold'),
                    command=ge).place(x=452, y=135)
        c = ttk.Combobox(buscarHorarioWindow, textvariable=g, values=["Data", "Tipo", "Cliente"], width=40,
                         state="readonly").place(x=185, y=88)
        en = Entry(buscarHorarioWindow, textvariable=f, width=43).place(x=185, y=138)

        def handle(event):
            if buscarHorarioWindow.listTree.identify_region(event.x, event.y) == "separator":
                return "break"

        buscarHorarioWindow.listTree = ttk.Treeview(buscarHorarioWindow, height=13, columns=('Horario', 'Data', 'Tipo', 'Cliente', 'Valor'))
        buscarHorarioWindow.vsb = ttk.Scrollbar(buscarHorarioWindow, orient="vertical", command=buscarHorarioWindow.listTree.yview)
        buscarHorarioWindow.listTree.configure(yscrollcommand=buscarHorarioWindow.vsb.set)
        buscarHorarioWindow.listTree.heading("#0", text='Id', anchor='center')
        buscarHorarioWindow.listTree.column("#0", width=150, anchor='center')
        buscarHorarioWindow.listTree.heading("Horario", text='Horario')
        buscarHorarioWindow.listTree.column("Horario", width=150, anchor='center')
        buscarHorarioWindow.listTree.heading("Data", text='Data')
        buscarHorarioWindow.listTree.column("Data", width=157, anchor='center')
        buscarHorarioWindow.listTree.heading("Tipo", text='Tipo')
        buscarHorarioWindow.listTree.column("Tipo", width=160, anchor='center')
        buscarHorarioWindow.listTree.heading("Cliente", text='Cliente')
        buscarHorarioWindow.listTree.column("Cliente", width=160, anchor='center')
        buscarHorarioWindow.listTree.heading("Valor", text='Valor')
        buscarHorarioWindow.listTree.column("Valor", width=150, anchor='center')
        buscarHorarioWindow.listTree.bind('<Button-1>', handle)
        buscarHorarioWindow.listTree.place(x=10, y=190)
        buscarHorarioWindow.vsb.place(x=940, y=190, height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

        a = StringVar()

        lb = Label(buscarHorarioWindow, bd=3, text="Deletar o horário (ID):", font=("Arial", 10, 'bold'), relief='ridge',
                   width=22)
        lb.place(x=640, y=135)
        e = Entry(buscarHorarioWindow, textvariable=a, width=20).place(x=830, y=135)
        b3 = Button(buscarHorarioWindow, bd=2, relief='raised', text="Deletar", width=15, font=("Arial", 10, 'bold'),
                    command=aaa).place(x=828, y=160)

        bt = Button(buscarHorarioWindow, bd=2, relief='raised', text="Mostrar Todos", width=35, font=("Arial", 10, 'bold'),
                    command=buscar_todos).place(x=10, y=50)

    def sest():
        #############################INICIO DA JANELA BUSCAR CLIENTES###########################
        clientesWindow = Toplevel()
        f = StringVar()
        g = StringVar()
        clientesWindow.title("Clientes")
        clientesWindow.maxsize(1000, 500)
        clientesWindow.minsize(1000, 500)
        clientesWindow.iconbitmap(r'icone_mel.ico')
        clientesWindow.photo = PhotoImage(file='bg_procurarCliente.png')
        clientesWindow.myLabel = Label(clientesWindow, image=clientesWindow.photo)
        clientesWindow.myLabel.place(x=0, y=0)

        #####################################FUNÇÃO PARA OS VALORES APARECEREM NA LISTBOX#############################
        def insert(data):
            clientesWindow.listTree.delete(*clientesWindow.listTree.get_children())
            for row in data:
                clientesWindow.listTree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4]))

        ##########################FUNÇÃO PARA BUSCAR TODOS CLIENTES######################################
        def buscar_todos():
            try:
                i = ''
                clientesWindow.conn = sqlite3.connect('library_administration.db')
                clientesWindow.mycursor = clientesWindow.conn.cursor()
                clientesWindow.mycursor.execute("Select * from clientes where Id like ?", ['%' + i + '%'])
                pc = clientesWindow.mycursor.fetchall()
                if pc:
                    try:
                        insert(pc)
                    except EXCEPTION:
                        messagebox.showinfo("Alerta", "Nenhum cliente encontrado")
            except EXCEPTION:
                messagebox.showinfo("Alerta", "Não foi possível buscar todos os clientes")

        ##################FUNÇÃO PARA SELECIONAR O TEXTO NA LISTBOX #########################
        def select(a):
            curItem = clientesWindow.listTree.focus()
            selItem = clientesWindow.listTree.item(curItem)
            pic = str(selItem['text'])


        ##############FUNÇÃO PARA FAZER A BUSCA#################################
        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Erro', 'Selecione o tipo de busca')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Erro', 'Digite o ' + g.get())
            elif g.get() == 'ID':
                try:
                    clientesWindow.conn = sqlite3.connect('library_administration.db')
                    clientesWindow.mycursor = clientesWindow.conn.cursor()
                    clientesWindow.mycursor.execute("Select * from clientes where Id like ?", ['%' + f.get() + '%'])
                    pc = clientesWindow.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Alerta", "Id não encontrado")
                except Error:
                    messagebox.showerror("Alerta", "Algum erro ocorreu")
            elif g.get() == 'Nome':
                try:
                    clientesWindow.conn = sqlite3.connect('library_administration.db')
                    clientesWindow.mycursor = clientesWindow.conn.cursor()
                    clientesWindow.mycursor.execute("Select * from clientes where Nome like ?", ['%' + f.get() + '%'])
                    pc = clientesWindow.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Alerta", "Nome não encontrado")
                except Error:
                    messagebox.showerror("Alerta", "Algum erro ocorreu")
            elif g.get() == 'Telefone':
                try:
                    clientesWindow.conn = sqlite3.connect('library_administration.db')
                    clientesWindow.mycursor = clientesWindow.conn.cursor()
                    clientesWindow.mycursor.execute("Select * from clientes where Telefone like ?", ['%' + f.get() + '%'])
                    pc = clientesWindow.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Alerta", "Telefone não encontrado")
                except Error:
                    messagebox.showerror("Erro", "Algum erro ocorreu")

        def aaa():
            if len(a.get()) == 0:
                messagebox.showerror("Erro", "Por favor digite o cliente que deseja excluir")
            else:
                c = messagebox.askyesno('Alerta', 'Você tem certeza que deseja deletar esse cliente?')
                if c:
                    try:
                        clientesWindow.conn = sqlite3.connect('library_administration.db')
                        clientesWindow.mycursor = clientesWindow.conn.cursor()
                        pc = clientesWindow.mycursor.execute("DELETE FROM clientes WHERE Id = ?", [a.get()])
                        clientesWindow.conn.commit()
                        if pc:
                            messagebox.showinfo("Alerta", "Sucesso ao deletar")
                            clientesWindow.destroy()
                        else:
                            messagebox.showerror("Erro",
                                                 "Este cliente não existe ou foi digitado incorretamente")
                    except Error:
                        messagebox.showerror("Erro", "Algo de errado ocorreu")
                    except Error as erro:
                        print(erro)
                        messagebox.showerror("Erro", "Algum erro ocorreu")

        ##################LABELS E BOTOES E ENTRY DA JANELA BUSCAR CLIENTES########################
        b1 = Button(clientesWindow, bd=3, relief='raised', text="Deletar", width=14, font=("Arial", 10, 'bold'),
                    command=aaa).place(x=860, y=160)
        b2 = Button(clientesWindow, bd=3, relief='raised', font=("Arial", 10, 'bold'), text="Buscar", width=15,
                    command=ge).place(x=460, y=125)
        c = ttk.Combobox(clientesWindow, textvariable=g, values=["ID", "Nome", "Telefone"], width=40,
                         state="readonly").place(x=180, y=130)
        en = Entry(clientesWindow, textvariable=f, width=43).place(x=180, y=170)

        ##############FUNÇÃO PARA SEPARAR OS TOPICOS DA LIST############################
        def handle(event):
            if clientesWindow.listTree.identify_region(event.x, event.y) == "separator":
                return "break"

        ##################LABELS TITULOS E CONFIGURAÇOES DA LIST#############################
        clientesWindow.listTree = ttk.Treeview(clientesWindow, height=13, columns=('Nome', 'Telefone', 'Instagram', 'Idade'))
        clientesWindow.vsb = ttk.Scrollbar(clientesWindow, orient="vertical", command=clientesWindow.listTree.yview)
        clientesWindow.listTree.configure(yscrollcommand=clientesWindow.vsb.set)
        clientesWindow.listTree.heading("#0", text='ID', anchor='w')
        clientesWindow.listTree.column("#0", width=150, anchor='w')
        clientesWindow.listTree.heading("Nome", text='Nome')
        clientesWindow.listTree.column("Nome", width=200, anchor='center')
        clientesWindow.listTree.heading("Telefone", text='Telefone')
        clientesWindow.listTree.column("Telefone", width=200, anchor='center')
        clientesWindow.listTree.heading("Instagram", text='Instagram')
        clientesWindow.listTree.column("Instagram", width=200, anchor='center')
        clientesWindow.listTree.heading("Idade", text='Aniversário')
        clientesWindow.listTree.column("Idade", width=200, anchor='center')
        clientesWindow.listTree.bind("<Button-1>", handle)
        clientesWindow.listTree.bind("<ButtonRelease-1>", select)
        clientesWindow.listTree.place(x=10, y=200)
        clientesWindow.vsb.place(x=963, y=200, height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

        a = StringVar()

        lb = Label(clientesWindow, bd=6, text="Deletar cliente(ID):", font=("Arial", 10, 'bold'), relief='ridge',
                   width=22)
        lb.place(x=650, y=130)
        e = Entry(clientesWindow, textvariable=a, width=20).place(x=860, y=135)

        bt = Button(clientesWindow, bd=3, relief='raised', text="Mostrar Todos", width=35, font=("Arial", 10, 'bold'),
                    command=buscar_todos).place(x=10, y=80)


    #########################LABELS DA JANELA PAINEL MENU############################
    painelWindow.button = Button(painelWindow, bd=4, relief='ridge', text='Clientes', width=20, font=('Algerian', 20),
                         command=sest).place(x=1000, y=25)
    painelWindow.brt = Button(painelWindow, bd=4, relief='ridge', text="Adicionar cliente", width=20, font=('Algerian', 20),
                      command=a_s).place(x=1000, y=95)
    painelWindow.brt = Button(painelWindow, bd=4, relief='ridge', text="Editar Cliente", width=20, font=('Algerian', 20),
                      command=e_c).place(x=1000, y=165)

    painelWindow.button = Button(painelWindow, bd=4, relief='ridge', text='Horários marcados', width=20, font=('Algerian', 20),
                         command=sea).place(x=1000, y=280)
    painelWindow.brt = Button(painelWindow, bd=4, relief='ridge', text="Agendar horário", width=20, font=('Algerian', 20),
                      command=a_b).place(x=1000, y=350)
    painelWindow.brt = Button(painelWindow, bd=4, relief='ridge', text="Editar Horário", width=20, font=('Algerian', 20),
                      command=e_h).place(x=1000, y=420)

    painelWindow.brt = Button(painelWindow, bd=4, relief='ridge', text="Histórico", width=20, font=('Algerian', 20),
                      command=a_h).place(x=1000, y=520)

    painelWindow.brt = Button(painelWindow, bd=4, relief='ridge', text="Sair", width=20, font=('Algerian', 20),
                      command=sair).place(x=1000, y=625)

    painelWindow.mainloop()



##################################BOTAO PARA INICIAR O PROGRAMA##############################
mainWindow.botao = Button(mainWindow, bg = '#FFFFFF', bd=15, relief='flat', text="Iniciar", font=('Algerian', 20), width=20, height=2, command=entrar_no_programa).place(x=460, y=292)
mainWindow.mainloop()