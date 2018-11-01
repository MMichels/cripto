import tkinter.ttk as ttk
from io import TextIOWrapper
from tkinter import *

import avisos
import tela_support
from cfgManager import Config
from cripto import Cripto
from fileman import FileChooser


def start_gui():
    global val, w, root
    root = Tk()
    top = Tela(root)
    tela_support.init(root, top)
    root.mainloop()


w = None


def iniciar_Tela(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Tela(w)
    tela_support.init(w, top, *args, **kwargs)
    return (w, top)


def fechar_Tela():
    global w
    w.destroy()
    w = None


class Tela:
    def __init__(self, top=None):
        self.file = TextIOWrapper
        self.cfgM = Config()
        self.style = ttk.Style()
        top.geometry("745x560+656+150")
        top.title("Editor CFG")
        # telas
        self.abas = ttk.Notebook(top, width=720)
        self.abas_db = Frame(self.abas)
        self.abas.place(relx=0.013, rely=0.15, relheight=0.75
                        , relwidth=0.974)
        self.abas.add(self.abas_db, padding=3)
        self.abas.tab(0, text="Database", compound="left", underline="-1")
        # Labels
        self.lblStatus = Label(top, text='Status')
        self.lblStatus.place(relx=0.013, rely=0.947, height=26, width=722)
        Label(top, text='Arquivo').place(relx=0.013, rely=0.018, height=30, width=58)
        Label(top, text='Chave').place(relx=0.013, rely=0.09, height=30, width=50)
        Label(self.abas_db, text='Endereço').place(relx=0.042, rely=0.372, height=26, width=68)
        Label(self.abas_db, text='Porta').place(relx=0.472, rely=0.372, height=26, width=41)
        Label(self.abas_db, text='Usuário').place(relx=0.042, rely=0.442, height=26, width=56)
        Label(self.abas_db, text='Senha').place(relx=0.042, rely=0.512, height=26, width=46)
        Label(self.abas_db, text='Base').place(relx=0.042, rely=0.581, height=26, width=37)

        # Inputs
        self.txtDir = Entry(top)
        self.txtDir.place(relx=0.094, rely=0.018, height=30, relwidth=0.342)

        self.txtChave = Entry(top)
        self.txtChave.place(relx=0.094, rely=0.09, height=30, relwidth=0.342)

        self.txtDbUrl = Entry(self.abas_db)
        self.txtDbUrl.place(relx=0.153, rely=0.372, height=24, relwidth=0.311)

        self.txtDbPort = Entry(self.abas_db)
        self.txtDbPort.place(relx=0.542, rely=0.372, height=24, relwidth=0.111)

        self.txtDbUser = Entry(self.abas_db)
        self.txtDbUser.place(relx=0.153, rely=0.442, height=24, relwidth=0.311)

        self.txtDbSenha = Entry(self.abas_db)
        self.txtDbSenha.place(relx=0.153, rely=0.512, height=24, relwidth=0.311)

        self.txtDbBase = Entry(self.abas_db)
        self.txtDbBase.place(relx=0.153, rely=0.581, height=24, relwidth=0.311)

        self.btnProcurar = Button(top, text='Procurar', takefocus='1')
        self.btnProcurar.place(relx=0.444, rely=0.018, height=30, width=76)

        self.btnNovo = Button(top, text='Novo', takefocus='1', command=self.clk_novo)
        self.btnNovo.place(relx=0.556, rely=0.018, height=30, width=76)

        self.btnAcao = Button(top, text='Carregar', command=self.clk_acao)
        self.btnAcao.place(relx=0.444, rely=0.09, height=30, width=76)

        self.btnTestar = Button(self.abas_db, text="Testar")
        self.btnTestar.place(relx=0.542, rely=0.512, height=30, width=80)

    def procurar(self):
        fc = FileChooser()
        self.file = fc.get_open_file_dir()

    def clk_acao(self):
        if self.btnAcao['text'] == 'Carregar':
            if self.txtChave.get() is '':
                self.lblStatus['text'] = 'Nao foi adicionada uma chave para o arquivo'
            # TODO: Fazer o codigo de carregamento do arquivo cfg
        elif self.btnAcao['text'] == 'Salvar':
            avisos.aviso('Lembre-se de salvar sua chave!')
            if self.txtDir.get().endswith('proj.cfg'):
                fc = FileChooser()
                self.file = fc.get_save_file_dir()
                self.txtDir.delete(0, END)
                self.txtDir.insert(0, self.file)
                try:
                    chave = open('..\\arquivos\\chave.key', 'x')
                except FileExistsError:
                    chave = open('..\\arquivos\\chave.key', 'w')
                chave.write(self.txtChave.get())
                chave.close()
            elif self.txtDir.get().endswith('.cfg'):
                self.file = open(self.txtDir['text'])
            self.mk_cfg()
            self.cfgM.save(self.txtDir.get())

    def clk_novo(self):
        if self.btnNovo['text'] == 'Novo':
            self.txtChave.delete(0, END)
            self.txtChave.insert(0, Cripto.gerar_chave())
            self.btnAcao['text'] = 'Salvar'
            self.txtDir.delete(0, END)
            self.txtDir.insert(0, FileChooser().get_fullpath('..\\arquivos\\proj.cfg'))

    def mk_cfg(self):
        self.cfgM = Config(self.txtChave.get())
        self.cfgM.set_db_url(self.txtDbUrl.get())
        self.cfgM.set_db_port(self.txtDbPort.get())
        self.cfgM.set_db_user(self.txtDbUser.get())
        self.cfgM.set_db_passwd(self.txtDbSenha.get())
        self.cfgM.set_db_name(self.txtDbBase.get())


if __name__ == '__main__':
    start_gui()
