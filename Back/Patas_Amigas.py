# Bibliotecas:
import mysql.connector
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QDialog, QTableWidgetItem, QTableWidget, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QTableWidgetItem
import sys
from Classes import Data_base


# Conectando com o novo Banco de Dados:
def connect():
    conn = mysql.connector.connect(
        user='root',
        password='',  
        host='localhost',
        database='banco tcc'  
    )
    return conn


# Função de gravar dados na tb_adm2 e redirecionar para o login
def gravar_e_ir_para_login():
    try:
        nome = CadastroAdm.txt_nomeadm.text()  # Captura o nome da caixa de texto
        cpf = CadastroAdm.txt_cpf.text().replace(".", "").replace("-", "")
        email = CadastroAdm.txt_email.text()
        senha = CadastroAdm.txt_senha.text()
        rsenha = CadastroAdm.txt_rsenha.text()
        setor = CadastroAdm.txt_setor.text()
        if senha != rsenha:
            mensagem = QMessageBox()
            mensagem.setText("Senhas não conferem")
            mensagem.setWindowTitle("CADASTRO DE CONTAS")
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
            return

        conn = connect()
        cursor = conn.cursor()

        # Verifica se o cadastro já existe na tabela tb_adm2
        SQL = "SELECT * FROM tb_adm2 WHERE cpf = %s OR email = %s"
        cursor.execute(SQL, (cpf, email))

        if cursor.fetchall():
            mensagem = QMessageBox()
            mensagem.setText("Cadastro já existente")
            mensagem.setWindowTitle("CADASTRO DE CONTAS")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
        else:
            # Inserindo os dados na tabela tb_adm2
            SQL = "INSERT INTO tb_adm2 (nome, cpf, email, senha, setor) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(SQL, (nome, cpf, email, senha, setor))
            conn.commit()

            mensagem = QMessageBox()
            mensagem.setText("Dados enviados com sucesso!")
            mensagem.setWindowTitle("CADASTRO DE CONTAS")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()

            # Limpa os campos do formulário
            CadastroAdm.txt_nomeadm.clear()
            CadastroAdm.txt_cpf.clear()
            CadastroAdm.txt_email.clear()
            CadastroAdm.txt_senha.clear()
            CadastroAdm.txt_rsenha.clear()

            # Redireciona para a tela de login
          
            LoginAdm.show()

        cursor.close()
        conn.close()
    except Exception as e:
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Critical)
        message_box.setText(f"Erro ao gravar: {str(e)}")
        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message_box.exec_()

# Função de login para o admin
def login_adm():
    try:
        email = LoginAdm.txt_email.text()
        senha = LoginAdm.txt_senha.text()

        conn = connect()
        cursor = conn.cursor()

        # Busca o nome do administrador na tabela tb_adm2 com base no email e senha
        SQL = "SELECT nome FROM tb_adm2 WHERE email = %s AND senha = %s"
        cursor.execute(SQL, (email, senha))
        result = cursor.fetchone()

        if result:
            nome_adm = result[0]
            mensagem = QMessageBox()
            mensagem.setText("Login realizado com sucesso!")
            mensagem.setWindowTitle("LOGIN")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()

            # Chama a função para abrir a próxima tela e passar o nome do administrador
            abrir_Tela_Inicial(nome_adm)

            # Fecha a tela de login
            LoginAdm.close()
            Escolha.close()
            CadastroAdm.close()

        else:
            mensagem = QMessageBox()
            mensagem.setText("Email ou senha incorretos!")
            mensagem.setWindowTitle("LOGIN")
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()

        cursor.close()
        conn.close()

    except Exception as e:
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Critical)
        message_box.setText(f"Erro ao fazer login: {str(e)}")
        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message_box.exec_()

# Funções de passar a tela:
    #Funções que fecham a tela de Escolha:

def Escolha_para_cadastro():
    Escolha.close()
    CadastroAdm.show()

def Escolha_para_login():
    LoginAdm.show()

    #Funções que fecham o Cadastro de ADM:

def Cadastro_para_login():
    CadastroAdm.close()
    LoginAdm.show()    

def Cadastro_para_telainicial():
    CadastroAdm.close()
    Escolha.show()
    #Funçôes que fecham o Login de ADM:

def login_para_escolha():
    LoginAdm.close()
    Escolha.show()

    #Funções que fecham a Tela Inicial:

def telainical_para_reclamacoes():
    Tela_Inicial.close()
    ReclamacaoControle.show()
    carregar_dados_tabela_Reclamacoes()
def telainicial_para_Usuarios():
    Tela_Inicial.close()
    UserControle.show()

def Tela_Inicial_Para_Ctrl_Adm():
    Crtl_Adm.show()
    Tela_Inicial.close()

    
    #Funções que fecham o Controle de Reclamações:
def Reclamacoes_para_telainicial():
    ReclamacaoControle.close()
    Tela_Inicial.show()

def Reclamacao_Para_User():
    UserControle.show()
    ReclamacaoControle.close()

def Reclamacao_Para_ADM():
    ReclamacaoControle.close()
    Crtl_Adm.show()

def Reclamacao_Para_RecSalva():
    ReclamacaoControle.close()
    Rec_Salvas.show()
    Carregar_RecSalvas()

    #Funções que fecham as reclamações salvas:
def SalvaRec_Para_Reclamacao():
    Rec_Salvas.close()
    ReclamacaoControle.show()
def SalvarRec_Para_Adm():
    Rec_Salvas.close()
    Crtl_Adm.show()
def SalvarRec_Para_Usuario():
    Rec_Salvas.close()
    UserControle.show()
    carregar_dados_tabela_User()
    #Funções que fecham o Controle de Usuários:

def User_Para_Adms():
    Crtl_Adm.show()
    UserControle.close()
    carregar_dados_tabela_Adm2()

def User_Para_Telainicial():
    UserControle.close()
    Tela_Inicial.show()

def User_Para_Reclamacoes():
    UserControle.close()
    ReclamacaoControle.show()
    #Funções que fecham o controle de ADM:

def Adm_Para_Telainicial():
    Crtl_Adm.close()
    Tela_Inicial.show()

def Adm_Para_Controle():
    Crtl_Adm.close()
    Escolha_Adm.show()

#Funções para que fecham Adm1:

def Adm1_Para_adm2():
    Adm1.close()
    Adm2.show()
    Carrega_dados_tbadm_Nvl2()
def adm1_Para_adm3():
    Adm1.close()
    Adm3.show()
def Adm1_Para_ControleAdm():
    Adm1.close()
    Crtl_Adm.show()
#Funções para que fecham Adm2:

def Adm2_Para_adm1():
    Adm2.close()
    Adm1.show()
def Adm2_Para_Adm3():
    Adm2.close()
    Adm3.show()
    Carrega_dados_tbadm_Nvl3()
def Adm2_Para_ControleAdm():
    Adm2.close()
    Crtl_Adm.show()
#Funções para que fecham Adm3:
def Adm3_Para_adm1():
    Adm3.close()
    Adm1.show()
def Adm3_Para_adm2():
    Adm3.close()
    Adm2.show()
def Adm3_Para_ControleAdm():
    Adm3.close()
    Crtl_Adm.show()
#Funções que fecham a escolha do ADM
def Escolha_Para_Adm1():
    Escolha_Adm.close()
    Adm1.show()
    Carrega_dados_tbadm_Nvl1()
def Escolha_Para_Adm2():
    Escolha_Adm.close()
    Adm2.show()
def Escolha_Para_Adm3():
    Escolha_Adm.close()
    Adm3.show()
#------------- Fim das Funções de passar de Tela --------------------------

def abrir_Tela_Inicial(nome_adm):
    try:
        if hasattr(Tela_Inicial, 'lbl_bem_vindo'):
            Tela_Inicial.lbl_bem_vindo.setText(f"Seja Bem-vindo, Sr(a) {nome_adm}!")
        else:
            print("lbl_bem_vindo não encontrado na Tela_Inicial")
        
        Tela_Inicial.show()
        print("Tela inicial aberta com sucesso!")
        
    except Exception as e:
        print(f"Erro ao fazer o login {str(e)}")
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Critical)
        message_box.setText(f"Erro ao fazer o login {str(e)}")
        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message_box.exec_()

#------------- Inicio das funções referentes as funcionalidades do projeto ------------------------
    #Funções referente a reclamações
        #Função para inserir dados na Tabela de Controle de Reclamações AVISO: TEM QUE ESTAR EM UM EVENTO CLICKED!!!
def carregar_dados_tabela_Reclamacoes():
    # Busca os dados da tabela 'tb_reclamacoes' usando a classe Data_base
    results = db.fetch_reclamacoes()
    
    if results:
        # Configura a quantidade de linhas e colunas da tabela
        ReclamacaoControle.TB_Reclamacao.setRowCount(len(results))
        ReclamacaoControle.TB_Reclamacao.setColumnCount(len(results[0]))

        # Preenche a tabela com os dados do banco
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                ReclamacaoControle.TB_Reclamacao.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
    else:
        print("Nenhum dado encontrado ou erro na conexão.")


        #Função de Deletar reclamação vinculada a um evento clicked

def deletar_reclamacao():
    try:    
        # Pega a linha selecionada
        linha_selecionada = ReclamacaoControle.TB_Reclamacao.currentRow()
        
            # Verifica se alguma linha está selecionada
            # Assume que o ID está na primeira coluna (coluna 0)
        id_reclamacao = ReclamacaoControle.TB_Reclamacao.item(linha_selecionada, 0).text()
        if id_reclamacao == False:
            mensagem = QMessageBox()
            mensagem.setText("reclamação não encontrada")
            mensagem.setWindowTitle("Reclamação Indetectável")
            mensagem.setIcon(QMessageBox.warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
        else:
            # Chama o método delete_reclamacao passando o ID da linha selecionada
            db.delete_reclamacao(id_reclamacao)


                # Atualiza a tabela ou faça outra ação necessária
            carregar_dados_tabela_Reclamacoes()

            mensagem = QMessageBox()
            mensagem.setText("reclamação fechada com sucesso!")
            mensagem.setWindowTitle("Fechar Reclamação")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
    except:
        mensagem = QMessageBox()
        mensagem.setText("Erro ao fechar reclamação")
        mensagem.setWindowTitle("ERRO")
        mensagem.setIcon(QMessageBox.critical)
        mensagem.setStandardButtons(QMessageBox.Ok)
        mensagem.exec()


def Salvar_Reclamacao():
    try:
        linha_selecionada = ReclamacaoControle.TB_Reclamacao.currentRow()
        
        # Verifica se alguma linha está selecionada
        # Assume que o ID está na primeira coluna (coluna 0)
        id_reclamacao = ReclamacaoControle.TB_Reclamacao.item(linha_selecionada, 0).text()
        if not id_reclamacao:
            mensagem = QMessageBox()
            mensagem.setText("Nenhuma linha selecionada")
            mensagem.setWindowTitle("ERRO")
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
        else:
            try:
                db.Guardar_Rec(id_reclamacao)
                results = db.fetch_slvRec()
                for row_idx, row_data in enumerate(results):
                    for col_idx, col_data in enumerate(row_data):
                        ReclamacaoControle.TB_Reclamacao.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
                mensagem = QMessageBox()
                mensagem.setText("Reclamação salva com sucesso!")
                mensagem.setWindowTitle("Processo concluido")
                mensagem.setIcon(QMessageBox.Information)
                mensagem.setStandardButtons(QMessageBox.Ok)
                mensagem.exec()

            except Exception as e:
                mensagem = QMessageBox()
                mensagem.setText(f"Ocorreu um erro: {str(e)}")
                mensagem.setWindowTitle("ERRO")
                mensagem.setIcon(QMessageBox.Warning)
                mensagem.setStandardButtons(QMessageBox.Ok)
                mensagem.exec()

    except Exception as e:
        mensagem = QMessageBox()
        mensagem.setText(f"Ocorreu um erro: {str(e)}")
        mensagem.setWindowTitle("ERRO")
        mensagem.setIcon(QMessageBox.Warning)
        mensagem.setStandardButtons(QMessageBox.Ok)
        mensagem.exec()


def Carregar_RecSalvas():
    try:
        results = db.fetch_slvRec()
        if results:
             # Configura a quantidade de linhas e colunas da tabela
            Rec_Salvas.Tb_RecSalva.setRowCount(len(results))
            Rec_Salvas.Tb_RecSalva.setColumnCount(len(results[0]))    
            for row_idx, row_data in enumerate(results):
                for col_idx, col_data in enumerate(row_data):
                    Rec_Salvas.Tb_RecSalva.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    except Exception as e:
        mensagem = QMessageBox()
        mensagem.setText("Erro ao atualizar tabela:  ")
        mensagem.setWindowTitle("ERRO")
        mensagem.setIcon(QMessageBox.Critical)
        mensagem.setStandardButtons(QMessageBox.Ok)
        mensagem.exec()
       

def deletar_RecSalva():
    try:    
        # Pega a linha selecionada
        linha_selecionada = Rec_Salvas.Tb_RecSalva.currentRow()
        
            # Verifica se alguma linha está selecionada
            # Assume que o ID está na primeira coluna (coluna 0)
        id_reclamacao = Rec_Salvas.Tb_RecSalva.item(linha_selecionada, 0).text()
        if id_reclamacao == False:
            mensagem = QMessageBox()
            mensagem.setText("reclamação não encontrada")
            mensagem.setWindowTitle("Reclamação Indetectável")
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
        else:
            # Chama o método delete_reclamacao passando o ID da linha selecionada
            db.delete_RecSalva(id_reclamacao)


                # Atualiza a tabela ou faça outra ação necessária
            Carregar_RecSalvas()

            mensagem = QMessageBox()
            mensagem.setText("reclamação fechada com sucesso!")
            mensagem.setWindowTitle("Fechar Reclamação")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
    except:
        pass
    #----------- Funções de Usuário -----------------------
        #Função para exibir dados na tablea de controle de usuario. AVISO: TEM QUE ESTAR EM UM EVENTO CLICKED!!!
def carregar_dados_tabela_User():
    # Busca os dados da tabela 'tb_reclamacoes' usando a classe Data_base
    results = db.fetch_user()
    
    if results:
        # Configura a quantidade de linhas e colunas da tabela
        UserControle.Tb_CrtlUser.setRowCount(len(results))
        UserControle.Tb_CrtlUser.setColumnCount(len(results[0]))

        # Preenche a tabela com os dados do banco
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                UserControle.Tb_CrtlUser.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
    else:
        print("Nenhum dado encontrado ou erro na conexão.")

        #Função de banir Usuario

def banir_user():
    try:  
        conn = connect()
        cursor = conn.cursor()

        # Pega a linha selecionada
        linha_selecionada = UserControle.Tb_CrtlUser.currentRow()
        
        # Verifica se alguma linha está selecionada
        if linha_selecionada == -1:  # Nenhuma linha selecionada
            mensagem = QMessageBox()
            mensagem.setText("Nenhum usuário selecionado!")
            mensagem.setWindowTitle("User não selecionado")
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
            return  # Sai da função caso não tenha usuário selecionado

        # Assume que o ID está na primeira coluna (coluna 0)
        id_user = UserControle.Tb_CrtlUser.item(linha_selecionada, 0).text()
        
        cursor.execute("SELECT avisos FROM tb_user WHERE Id = %s", (id_user,))
        aviso_data = cursor.fetchone()

        if aviso_data and aviso_data[0] < 3:
            mensagem = QMessageBox()
            mensagem.setText("Usuário possui um número baixo de avisos, deseja realmente continuar?")
            mensagem.setWindowTitle("Reclamações baixas")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            resposta = mensagem.exec()

            if resposta == QMessageBox.Ok:
                db.delete_user(id_user)
                carregar_dados_tabela_User()
                mensagem.setText("Usuário banido com sucesso!")
                mensagem.setWindowTitle("Processo bem sucedido")
                mensagem.setIcon(QMessageBox.Information)
                mensagem.setStandardButtons(QMessageBox.Ok)
                mensagem.exec()
            else:
                mensagem.setText("Processo cancelado.")
                mensagem.setWindowTitle("Usuário permanece ativo")
                mensagem.setIcon(QMessageBox.Information)
                mensagem.setStandardButtons(QMessageBox.Ok)
                mensagem.exec()
        else:
            db.delete_user(id_user)
            carregar_dados_tabela_User()
            mensagem = QMessageBox()
            mensagem.setText("Usuário banido com sucesso!")
            mensagem.setWindowTitle("Processo bem sucedido")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()

    except Exception as e:
        mensagem = QMessageBox()
        mensagem.setText(f"Erro ao banir usuário: {str(e)}")
        mensagem.setWindowTitle("ERRO")
        mensagem.setIcon(QMessageBox.Critical)
        mensagem.setStandardButtons(QMessageBox.Ok)
        mensagem.exec()
        print(e)


def Por_sob_aviso():
    try:
        try:  
            # Pega a linha selecionada
            linha_selecionada = UserControle.Tb_CrtlUser.currentRow()
            
                # Verifica se alguma linha está selecionada
                # Assume que o ID está na primeira coluna (coluna 0)
            id_user =UserControle.Tb_CrtlUser.item(linha_selecionada, 0).text()
            if id_user == False:
                mensagem = QMessageBox()
                mensagem.setText("Nenhum usuário selecionado!")
                mensagem.setWindowTitle("User não selecionado")
                mensagem.setIcon(QMessageBox.Warning)
                mensagem.setStandardButtons(QMessageBox.Ok)
                mensagem.exec()
            else:
                    # Chama o método delete_reclamacao passando o ID da linha selecionada
                db.Registrar_aviso(id_user)
                carregar_dados_tabela_User()
                mensagem = QMessageBox()
                mensagem.setText("Usuário foi advertido com sucesso!")
                mensagem.setWindowTitle("Processo bem sucedido")
                mensagem.setIcon(QMessageBox.Information)
                mensagem.setStandardButtons(QMessageBox.Ok)
                mensagem.exec()
        except Exception as e:
            db.Registrar_aviso(id_user)
            carregar_dados_tabela_User()
            mensagem = QMessageBox()
            mensagem.setText("Ocorreu um erro no processo: ", e)
            mensagem.setWindowTitle("ERRO")
            mensagem.setIcon(QMessageBox.Critical)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
            
    except:
            db.Registrar_aviso(id_user)
            carregar_dados_tabela_User()
            mensagem = QMessageBox()
            mensagem.setText("ERRO FATAL: ", e)
            mensagem.setWindowTitle("ERRO")
            mensagem.setIcon(QMessageBox.Critical)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()



#-----------------------Função de ADM -------------------------
        #Função para mostrar dados na Tabela Adm. AVISO: PRECISA ESTAR EM UM EVENTO CLICKED!!!

def carregar_dados_tabela_Adm2():
    # Busca os dados da tabela 'tb_adm2' usando a classe Data_base
    results = db.fetch_adm()
    
    if results:
        # Configura a quantidade de linhas e colunas da tabela
        Crtl_Adm.Tb_CrtlAdm.setRowCount(len(results))
        Crtl_Adm.Tb_CrtlAdm.setColumnCount(len(results[0]))

        # Preenche a tabela com os dados do banco
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                Crtl_Adm.Tb_CrtlAdm.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
    else:
        print("Nenhum dado encontrado ou erro na conexão.")

        #Função de Recusar Adm

def Reprovar_Adm():
    try:
        # Pega a linha selecionada
        linha_selecionada = Crtl_Adm.Tb_CrtlAdm.currentRow()
        
            # Verifica se alguma linha está selecionada
            # Assume que o ID está na primeira coluna (coluna 0)
        id_Adm = Crtl_Adm.Tb_CrtlAdm.item(linha_selecionada, 0).text()
        if id_Adm == False:
            mensagem = QMessageBox()
            mensagem.setText("Nenhum Adm Selecionado!")
            mensagem.setWindowTitle("Selecione algum Adm na tabela")
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
            # Chama o método delete_reclamacao passando o ID da linha selecionada
        else:
            mensagem = QMessageBox()
            mensagem.setText("Novo Adm Recusado com sucesso!")
            mensagem.setWindowTitle("Adm recusado")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
            db.delete_adm(id_Adm)

                # Atualiza a tabela ou faça outra ação necessária
            carregar_dados_tabela_Adm2()
    except:
            mensagem = QMessageBox()
            mensagem.setText("Erro ao reprovar Adm")
            mensagem.setWindowTitle("ERRO")
            mensagem.setIcon(QMessageBox.Critical)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()

        #Função de Aprovar Adm
        
def aprovar_adm():
    try:
        # Pega a linha selecionada pelo usuário
        linha_selecionada = Crtl_Adm.Tb_CrtlAdm.currentRow()

        # Assume o id como a primeira coluna (coluna 0)
        id_Adm = Crtl_Adm.Tb_CrtlAdm.item(linha_selecionada, 0).text()

        if not id_Adm:
            # Se id_Adm for None ou uma string vazia, exibe a mensagem de erro
            mensagem = QMessageBox()
            mensagem.setText("Nenhum Adm selecionado!")
            mensagem.setWindowTitle("Selecione um Adm na Tabela")
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
        else:
            # Mensagem de sucesso ao cadastrar o novo adm
            mensagem = QMessageBox()
            mensagem.setText("Novo adm cadastrado, acesse o Controle de Adm para alterar seu nivel de permissão!")
            mensagem.setWindowTitle("Novo Adm cadastrado com sucesso")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()

            # Aprova o novo administrador
            db.Aprovar_novo_Adm(id_Adm)
            # Depois de aprovado, exclui da tabela temporária
            db.delete_adm(id_Adm)

            # Carrega novamente os dados da tabela
            carregar_dados_tabela_Adm2()  
    except Exception as e:
        mensagem = QMessageBox()
        mensagem.setText(f"Erro ao aprovar novo Adm: {e}")  # Corrige a formatação do erro
        mensagem.setWindowTitle("ERRO")
        mensagem.setIcon(QMessageBox.Critical)
        mensagem.setStandardButtons(QMessageBox.Ok)
        mensagem.exec()

def Carrega_dados_tbadm_Nvl1():
# Busca os dados da tabela 'tb_adm' usando a classe Data_base
    results = db.fetch_Adm_nivel1()
    
    if results:
        # Configura a quantidade de linhas e colunas da tabela
        Adm1.Tb_adm1.setRowCount(len(results))
        Adm1.Tb_adm1.setColumnCount(len(results[0]))

        # Preenche a tabela com os dados do banco
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                Adm1.Tb_adm1.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
    else:
        print("Nenhum dado encontrado ou erro na conexão.")

def banir_adm1():
    try:
        # Pega a linha selecionada
        linha_selecionada = Adm1.Tb_adm1.currentRow()
        
            # Verifica se alguma linha está selecionada
            # Assume que o ID está na primeira coluna (coluna 0)
        id_Adm = Adm1.Tb_adm1.item(linha_selecionada, 0).text()
        if id_Adm == False:
            mensagem = QMessageBox()
            mensagem.setText("Nenhum Adm Selecionado!")
            mensagem.setWindowTitle("Selecione algum Adm na tabela")
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
            # Chama o método delete_reclamacao passando o ID da linha selecionada
        else:
            mensagem = QMessageBox()
            mensagem.setText("Adm Banido!")
            mensagem.setWindowTitle("Adm recusado")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
            db.banir_Adm1(id_Adm)

                # Atualiza a tabela ou faça outra ação necessária
            Carrega_dados_tbadm_Nvl1()
    except:
            mensagem = QMessageBox()
            mensagem.setText("Erro ao Banir")
            mensagem.setWindowTitle("ERRO")
            mensagem.setIcon(QMessageBox.Critical)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()

def promover_adm1():
    try:
        # Pega a linha selecionada pelo usuário
        linha_selecionada = Adm1.Tb_adm1.currentRow()

        # Assume o id como a primeira coluna (coluna 0)
        id_Adm = Adm1.Tb_adm1.item(linha_selecionada, 0).text()

        if not id_Adm:
            # Se id_Adm for None ou uma string vazia, exibe a mensagem de erro
            mensagem = QMessageBox()
            mensagem.setText("Nenhum Adm selecionado!")
            mensagem.setWindowTitle("Selecione um Adm na Tabela")
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
        else:
            # Mensagem de sucesso ao cadastrar o novo adm
            mensagem = QMessageBox()
            mensagem.setText("O Adm foi cadastrado novamente como Nível 2, acesse o painel do nivel para visualizar alteração")
            mensagem.setWindowTitle("Adm Promovido!")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()

            # Promover
            db.promover_Adm1(id_Adm)
            # Depois de aprovado, exclui da tabela temporária
            # Carrega novamente os dados da tabela
            Carrega_dados_tbadm_Nvl1()  
    except:
            mensagem = QMessageBox()
            mensagem.setText("Erro ao aprovar")
            mensagem.setWindowTitle("ERRO")
            mensagem.setIcon(QMessageBox.Critical)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()

def Carrega_dados_tbadm_Nvl2():
# Busca os dados da tabela 'tb_adm' usando a classe Data_base
    results = db.fetch_Adm_nivel2()
    
    if results:
        # Configura a quantidade de linhas e colunas da tabela
        Adm2.Tb_adm2.setRowCount(len(results))
        Adm2.Tb_adm2.setColumnCount(len(results[0]))

        # Preenche a tabela com os dados do banco
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                Adm2.Tb_adm2.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
    else:
        print("Nenhum dado encontrado ou erro na conexão.")

def promover_adm2():
    try:
        # Pega a linha selecionada pelo usuário no formulário Adm2
        linha_selecionada = Adm2.Tb_adm2.currentRow()
        
        # Assume o id como a primeira coluna (coluna 0)
        id_Adm = Adm2.Tb_adm2.item(linha_selecionada, 0).text()

        if not id_Adm:
            # Se id_Adm for None ou uma string vazia, exibe a mensagem de erro
            mensagem = QMessageBox()
            mensagem.setText("Nenhum Adm selecionado!")
            mensagem.setWindowTitle("Selecione um Adm na Tabela")
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
        else:
            # Mensagem de sucesso ao promover o adm para nível 3
            mensagem = QMessageBox()
            mensagem.setText("O Adm foi promovido ao nível 3, acesse o painel do nível para visualizar a alteração.")
            mensagem.setWindowTitle("Adm Promovido!")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()

            # Promover o adm para nível 3
            db.promover_Adm3(id_Adm)
            # Carrega novamente os dados da tabela
            Carrega_dados_tbadm_Nvl2()
    except:
        mensagem = QMessageBox()
        mensagem.setText("Erro ao promover")
        mensagem.setWindowTitle("ERRO")
        mensagem.setIcon(QMessageBox.Critical)
        mensagem.setStandardButtons(QMessageBox.Ok)
        mensagem.exec()

def rebaixar_nivel_para_1():
    try:
        # Pega a linha selecionada pelo usuário no formulário Adm3
        linha_selecionada = Adm2.Tb_adm2.currentRow()
        
        # Assume o id como a primeira coluna (coluna 0)
        id_Adm = Adm2.Tb_adm2.item(linha_selecionada, 0).text()

        if not id_Adm:
            # Se id_Adm for None ou uma string vazia, exibe a mensagem de erro
            mensagem = QMessageBox()
            mensagem.setText("Nenhum Adm selecionado!")
            mensagem.setWindowTitle("Selecione um Adm na Tabela")
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
        else:
            # Mensagem de sucesso ao rebaixar o adm para nível 1
            mensagem = QMessageBox()
            mensagem.setText("O Adm foi rebaixado ao nível 1, acesse o painel do nível para visualizar a alteração.")
            mensagem.setWindowTitle("Adm Rebaixado!")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()

            # Rebaixar o adm para nível 1
            db.rebaixar_Adm2_para_1(id_Adm)
            # Carrega novamente os dados da tabela
            Carrega_dados_tbadm_Nvl2()
    except:
        mensagem = QMessageBox()
        mensagem.setText("Erro ao rebaixar")
        mensagem.setWindowTitle("ERRO")
        mensagem.setIcon(QMessageBox.Critical)
        mensagem.setStandardButtons(QMessageBox.Ok)
        mensagem.exec()


def Carrega_dados_tbadm_Nvl3():
# Busca os dados da tabela 'tb_adm' usando a classe Data_base
    results = db.fetch_Adm_nivel3()
    
    if results:
        # Configura a quantidade de linhas e colunas da tabela
        Adm3.Tb_adm3.setRowCount(len(results))
        Adm3.Tb_adm3.setColumnCount(len(results[0]))

        # Preenche a tabela com os dados do banco
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                Adm3.Tb_adm3.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
    else:
        print("Nenhum dado encontrado ou erro na conexão.")

def rebaixar_adm3_para_2():
    try:
        # Pega a linha selecionada pelo usuário no formulário Adm3
        linha_selecionada = Adm3.Tb_adm3.currentRow()
        
        # Assume o id como a primeira coluna (coluna 0)
        id_Adm = Adm3.Tb_adm3.item(linha_selecionada, 0).text()

        if not id_Adm:
            # Se id_Adm for None ou uma string vazia, exibe a mensagem de erro
            mensagem = QMessageBox()
            mensagem.setText("Nenhum Adm selecionado!")
            mensagem.setWindowTitle("Selecione um Adm na Tabela")
            mensagem.setIcon(QMessageBox.Warning)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()
        else:
            # Mensagem de sucesso ao rebaixar o adm para nível 2
            mensagem = QMessageBox()
            mensagem.setText("O Adm foi rebaixado ao nível 2, acesse o painel do nível para visualizar a alteração.")
            mensagem.setWindowTitle("Adm Rebaixado!")
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec()

            # Rebaixar o adm para nível 2
            db.promover_Adm1(id_Adm)  # Usa a função que seta o nível de acesso para 2
            # Carrega novamente os dados da tabela
            Carrega_dados_tbadm_Nvl3()
    except:
        mensagem = QMessageBox()
        mensagem.setText("Erro ao rebaixar")
        mensagem.setWindowTitle("ERRO")
        mensagem.setIcon(QMessageBox.Critical)
        mensagem.setStandardButtons(QMessageBox.Ok)
        mensagem.exec()


# Função para exibir a imagem em uma QLabel específica
def exibir_foto(label, caminho_foto):
    foto = QPixmap(caminho_foto)
    if foto.isNull():
        print("Erro ao carregar a imagem.")
    label.setPixmap(foto)
    label.setScaledContents(True)
# Inicializando CadastroAdm
app = QApplication(sys.argv)

# Caminho dos Formularios:
CadastroAdm = uic.loadUi(r"C:\Users\MARCIO\Desktop\Projeto patas amigas\Front\Cadastro_Adm.ui")
LoginAdm = uic.loadUi(r"C:\Users\MARCIO\Desktop\Projeto patas amigas\Front\login_adm.ui")
Escolha = uic.loadUi(r"C:\Users\MARCIO\Desktop\Projeto patas amigas\Front\Cadastro_ou_login_Adm.ui")
UserControle = uic.loadUi(r"C:\Users\MARCIO\Desktop\Projeto patas amigas\Front\Controle_de_user.ui")
ReclamacaoControle = uic.loadUi(r"C:\Users\MARCIO\Desktop\Projeto patas amigas\Front\Controle_de_reclamaçao.ui")
Tela_Inicial = uic.loadUi(r"C:\Users\MARCIO\Desktop\Projeto patas amigas\Front\Tela_Inicial.ui")
Crtl_Adm = uic.loadUi(r"C:\Users\MARCIO\Desktop\Projeto patas amigas\Front\Ctrl_Adm.ui")
Rec_Salvas = uic.loadUi(r"C:\Users\MARCIO\Desktop\Projeto patas amigas\Front\Reclamações_salvas.ui")
Adm1 = uic.loadUi(r"C:\Users\MARCIO\Desktop\Projeto patas amigas\Front\NívelUmADM.ui")
Adm2 = uic.loadUi(r"C:\Users\MARCIO\Desktop\Projeto patas amigas\Front\NívelDoisADM.ui")
Adm3 = uic.loadUi(r"C:\Users\MARCIO\Desktop\Projeto patas amigas\Front\NívelTrêsADM.ui")
Escolha_Adm = uic.loadUi(r"C:\Users\MARCIO\Desktop\Projeto patas amigas\Front\ADM-Setor.ui")

# Adicionando a função nos objetos dos respectivos formulários
    # Formulário de Escolha
Escolha.Btn_irCadastro.clicked.connect(Escolha_para_cadastro)
Escolha.Btn_irlogin.clicked.connect(Escolha_para_login)
exibir_foto(Escolha.lbl_icone1, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (11).png")
exibir_foto(Escolha.lbl_icone2, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (4).png")
exibir_foto(Escolha.lbl_logo, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/logo 1.png")
    # Formulário de Gravar dados
CadastroAdm.Btn_Cadastrar.clicked.connect(gravar_e_ir_para_login)
CadastroAdm.Btn_Voltar.clicked.connect(Cadastro_para_telainicial)
exibir_foto(CadastroAdm.lbl_usuario, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (4).png")
exibir_foto(CadastroAdm.lbl_pc, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (10).png")
exibir_foto(CadastroAdm.lbl_senha, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (9).png")
exibir_foto(CadastroAdm.lbl_cpf, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (8).png")
exibir_foto(CadastroAdm.lbl_email, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (7).png")
exibir_foto(CadastroAdm.lbl_senha_2, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (9).png")
    # Formulário de Login
LoginAdm.Btn_Login.clicked.connect(login_adm)

    #Formulario de Controle de Reclamações
ReclamacaoControle.Btn_irparaUsers.clicked.connect(Reclamacao_Para_User)
ReclamacaoControle.Btn_AtualizarRec.clicked.connect(carregar_dados_tabela_Reclamacoes)
ReclamacaoControle.Btn_fecharRec.clicked.connect(deletar_reclamacao)
ReclamacaoControle.Btn_irparatelainicial.clicked.connect(Reclamacoes_para_telainicial)
ReclamacaoControle.Btn_IrparaAdms.clicked.connect(Reclamacao_Para_ADM)
ReclamacaoControle.Btn_irparasalvas.clicked.connect(Reclamacao_Para_RecSalva)
ReclamacaoControle.Btn_SalvarRecc.clicked.connect(Salvar_Reclamacao)
exibir_foto(ReclamacaoControle.lbl_icone1, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (7).png")
exibir_foto(ReclamacaoControle.lbl_icone2, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (4).png")
exibir_foto(ReclamacaoControle.lbl_icone3, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (3).png")
exibir_foto(ReclamacaoControle.lbl_icone4, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (6).png")
exibir_foto(ReclamacaoControle.lbl_icone5, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (12).png")
    #Formulario de Controle de Users
UserControle.Btn_IrparaAdms.clicked.connect(User_Para_Adms)
UserControle.btn_atualizar.clicked.connect(carregar_dados_tabela_User)
UserControle.Btn_BanirUser.clicked.connect(banir_user)
UserControle.Btn_irparatelainicial2.clicked.connect(User_Para_Telainicial)
UserControle.Btn_irparaRec.clicked.connect(User_Para_Reclamacoes)
UserControle.Btn_Usersobaviso.clicked.connect(Por_sob_aviso)
    #Formulario de Controle de Adm
Crtl_Adm.Btn_AttAdm.clicked.connect(carregar_dados_tabela_Adm2)
Crtl_Adm.Btn_RecusarAdm.clicked.connect(Reprovar_Adm)
Crtl_Adm.Btn_AprovarAdm.clicked.connect(aprovar_adm)
Crtl_Adm.Btn_IrparaInicio.clicked.connect(Adm_Para_Telainicial)
Crtl_Adm.Btn_irParaEscolhadm.clicked.connect(Adm_Para_Controle)
    #Formulario de reclamacoes salvas:
Rec_Salvas.Btn_Voltar.clicked.connect(SalvaRec_Para_Reclamacao)
Rec_Salvas.Btn_att.clicked.connect(Carregar_RecSalvas)
Rec_Salvas.Btn_fecharRec.clicked.connect(deletar_RecSalva)
Rec_Salvas.Btn_IrparaAdms.clicked.connect(SalvarRec_Para_Adm)
Rec_Salvas.Btn_irparaUsers.clicked.connect(SalvarRec_Para_Usuario)
    # Formulario da tela inical
Tela_Inicial.Btn_reclamacao.clicked.connect(telainical_para_reclamacoes)
Tela_Inicial.Btn_CtrUser.clicked.connect(telainicial_para_Usuarios)
Tela_Inicial.Btn_irparaadm.clicked.connect(Tela_Inicial_Para_Ctrl_Adm)
exibir_foto(Tela_Inicial.lbl_icone1, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (4).png")
exibir_foto(Tela_Inicial.lbl_icone2, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (6).png")
exibir_foto(Tela_Inicial.lbl_icone3, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/icone (7).png")
exibir_foto(Tela_Inicial.lbl_logo, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/logo 1.png")
    #Formulario de Adm1:
Adm1.Btn_irparaNvl2.clicked.connect(Adm1_Para_adm2)
Adm1.Btn_irparaNvl3.clicked.connect(adm1_Para_adm3)
Adm1.Btn_Voltar.clicked.connect(Adm1_Para_ControleAdm)
Adm1.Btn_Atualizar.clicked.connect(Carrega_dados_tbadm_Nvl1)
Adm1.Btn_Banir.clicked.connect(banir_adm1)
Adm1.Btn_Promover.clicked.connect(promover_adm1)
    #Formulario de Adm2:
Adm2.Btn_irparaNvl1.clicked.connect(Adm2_Para_adm1)
Adm2.Btn_irparaNvl3.clicked.connect(Adm2_Para_Adm3)
Adm2.Btn_Voltar.clicked.connect(Adm2_Para_ControleAdm)
Adm2.Btn_Atualizar.clicked.connect(Carrega_dados_tbadm_Nvl2)
Adm2.Btn_Promover.clicked.connect(promover_adm2)
Adm2.Btn_Rebaixar.clicked.connect(rebaixar_nivel_para_1)
    #Formulario de Adm3:
Adm3.Btn_irparaNvl1.clicked.connect(Adm3_Para_adm1)
Adm3.Btn_irparaNvl2.clicked.connect(Adm3_Para_adm2)
Adm3.Btn_Voltar.clicked.connect(Adm3_Para_ControleAdm)
Adm3.Btn_Atualizar.clicked.connect(Carrega_dados_tbadm_Nvl3)
Adm3.Btn_rebaixar.clicked.connect(rebaixar_adm3_para_2)
    #Formulario de Escolha do nivel de ADM:
Escolha_Adm.Btn_Adm1.clicked.connect(Escolha_Para_Adm1)
Escolha_Adm.Btn_Adm2.clicked.connect(Escolha_Para_Adm2)
Escolha_Adm.Btn_Adm3.clicked.connect(Escolha_Para_Adm3)
exibir_foto(Escolha_Adm.lbl_icon1, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/logo 1.png")
exibir_foto(Escolha_Adm.lbl_icon2, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/Icone (13).png")
exibir_foto(Escolha_Adm.lbl_icon3, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/Icone (14).png")
exibir_foto(Escolha_Adm.lbl_icon4, r"C:/Users/MARCIO/Desktop/Projeto patas amigas/Front2/icone/Icone (15).png")
# Instânciando as classes
db = Data_base()
Tela_Inicial.show()
sys.exit(app.exec_())