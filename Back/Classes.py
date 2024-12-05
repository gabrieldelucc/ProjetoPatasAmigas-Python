import mysql.connector
from mysql.connector import Error

import mysql.connector
from mysql.connector import Error

class Data_base:
    def __init__(self, name='banco tcc') -> None:
        self.name = name
       

    def connect(self):
        try:
            # Faz a conexão com o banco de dados MySQL
            conn = mysql.connector.connect(
                user='root',
                password='',  # Verifique a senha
                host='localhost',
                database=self.name
            )
            return conn
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
        
   
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def close_connection(self, conn):
        try:
            conn.close()
        except Error as e:
            print(f"Erro ao fechar a conexão: {e}")
   
    def fetch_reclamacoes(self):
      
        #Método para buscar todas as reclamações na tabela `tb_reclamacoes`.
        #Retorna os resultados da consulta como uma lista de tuplas.
   
        try:
            conect = self.connect()
            if conect:
                cursor = conect.cursor()
                cursor.execute("SELECT * FROM tb_reclamacoes")  # Executa a consulta na tabela de reclamações
                result = cursor.fetchall()  # Obtém todos os registros da tabela
                cursor.close()
                self.close_connection(conect)  # Fecha a conexão após a consulta
                return result
            else:
                print("Conexão não estabelecida.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None

    def delete_reclamacao(self, id):
      
        #Método para deletar uma reclamação com base no ID (CR) na tabela `tb_reclamacoes`.
  
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute(f"DELETE FROM tb_reclamacoes WHERE CR = {id}")
                conn.commit()
                cursor.close()
                self.close_connection(conn)
                print(f"Reclamação com CR {id} foi deletada.")
            else:
                print("Conexão não estabelecida.")
        except Error as e:
            print(f"Erro ao deletar o registro: {e}")
            
    def fetch_user(self):
       
        #Método para buscar todas as reclamações na tabela `tb_user`.
        #Retorna os resultados da consulta como uma lista de tuplas.
      
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM tb_user")  # Executa a consulta na tabela de Usuarios
                result = cursor.fetchall()  # Obtém todos os registros da tabela
                cursor.close()
                self.close_connection(conn)  # Fecha a conexão após a consulta
                return result
            else:
                print("Conexão não estabelecida.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None

    def delete_user(self, id):
      
        #Método para deletar um Usuario com base no ID na tabela `tb_user`.
     
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute(f"DELETE FROM tb_user WHERE Id = {id}")
                conn.commit()
                cursor.close()
                self.close_connection(conn)
                print(f"Usuario com Id {id} foi deletado.")
            else:
                print("Conexão não estabelecida.")
        except Error as e:
            print(f"Erro ao deletar o registro: {e}")

    def fetch_adm(self):
       
        #Método para buscar todas as reclamações na tabela `tb_adm2`.
        #Retorna os resultados da consulta como uma lista de tuplas.
      
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM tb_adm2")  # Executa a consulta na tabela de Adm
                result = cursor.fetchall()  # Obtém todos os registros da tabela
                cursor.close()
                self.close_connection(conn)  # Fecha a conexão após a consulta
                return result
            else:
                print("Conexão não estabelecida.")
                return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None

    def delete_adm(self, id):
      
        #Método para deletar um Adm com base no ID na tabela `tb_adm2`.
     
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute(f"DELETE FROM tb_adm2 WHERE Id = {id}")
                conn.commit()
                cursor.close()
                self.close_connection(conn)
                print(f"Adm com Id {id} foi deletado.")
            else:
                print("Conexão não estabelecida.")
        except Error as e:
            print(f"Erro ao deletar o registro: {e}")

    def Aprovar_novo_Adm(self, id):
        
        #Método para aprovar um novo Adm, movendo-o da tabela tb_adm2 (temporária) para a tb_adm (definitiva).
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()

                # Primeiro, busca o registro do Adm na tabela temporária
                cursor.execute("SELECT Id, Nome, Email, Cpf, Senha, Rsenha, Setor FROM tb_adm2 WHERE Id = %s", (id,))
                adm_data = cursor.fetchone()

                if adm_data:
                    try:
                        # Insere os dados na tabela definitiva tb_adm
                        cursor.execute("""
                            INSERT INTO tb_adm (Id, Nome, Email, Cpf, Senha, Rsenha, Setor, Nivel_de_Acesso) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, 1)
                        """, adm_data)

                        # Commit após a inserção para garantir que ocorreu corretamente
                        conn.commit()
                        print(f"Adm com Id {id} foi aprovado e movido para a tabela definitiva.")

                        # Agora sim, remove o Adm da tabela temporária tb_adm2
                        cursor.execute("DELETE FROM tb_adm2 WHERE Id = %s", (id,))
                        conn.commit()
                        print(f"Adm com Id {id} foi deletado da tabela temporária.")

                    except Error as e:
                        print(f"Erro ao inserir na tabela definitiva: {e}")
                        return  # Interrompe o processo se ocorrer erro na inserção

                else:
                    print(f"Nenhum registro encontrado com Id {id} na tabela temporária.")

                cursor.close()
                self.close_connection(conn)
            else:
                print("Conexão não estabelecida.")
        except Error as e:
            print(f"Erro ao aprovar o Adm: {e}")

    def Registrar_aviso(self, id):
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()

                # Busca o campo avisos para o ID fornecido
                cursor.execute("SELECT avisos FROM tb_user WHERE Id = %s", (id,))
                aviso_data = cursor.fetchone()

                if aviso_data:
                    # Incrementa o valor do campo avisos
                    novo_aviso = aviso_data[0] + 1
                    cursor.execute("UPDATE tb_user SET avisos = %s WHERE Id = %s", (novo_aviso, id))

                    # Commit para salvar a alteração
                    conn.commit()
                    print(f"Aviso atualizado para o usuário com Id {id}. Novo valor: {novo_aviso}")
                else:
                    print(f"Nenhum registro encontrado com Id {id}.")

                cursor.close()
                self.close_connection(conn)
            else:
                print("Conexão não estabelecida.")
        except Error as e:
            print(f"Erro ao registrar aviso: {e}")
    
    def Guardar_Rec(self, CR):
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()

                # Primeiro, busca o registro da tabela de Reclamações
                cursor.execute("SELECT * FROM tb_reclamacoes WHERE CR = %s", (CR,))

                Rec_data = cursor.fetchone()

                if Rec_data:
                    try:
                        # Insere os dados na tabela definitiva tb_adm
                        cursor.execute("""
                            INSERT INTO `tb_reclamacoes_salva`(`CR_Primaria`, `Motivo`, `Descricao`, `Afetado`, `id_Afetado`, `Acusado`, `id_Acusado`)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            """, Rec_data)


                        # Commit após a inserção para garantir que ocorreu corretamente
                        conn.commit()
                        print(f"Reclamação com Cr {CR} foi salva com sucesso")

                    except Error as e:
                        print(f"Erro ao inserir na tabela de salvamentos: {e}")
                        return  # Interrompe o processo se ocorrer erro na inserção

                else:
                    print(f"Nenhum registro encontrado com CR {CR} na tabela de salvamentos.")

                cursor.close()
                self.close_connection(conn)
            else:
                print("Conexão não estabelecida.")
        except Error as e:
            print(f"Erro ao salvar reclamação: {e}")
    
    def fetch_slvRec(self):

        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM tb_reclamacoes_salva")  # Executa a consulta na tabela de Adm
                result = cursor.fetchall()  # Obtém todos os registros da tabela
                cursor.close()
                self.close_connection(conn)  # Fecha a conexão após a consulta
                return result
            else:
                print("Conexão não estabelecida.")
            return None
        except Error as e:
                    print(f"Erro ao buscar dados: {e}")
                    return None
    
    def delete_RecSalva(self, CR):
      
        #Método para deletar uma Reclamação salava com base no CR da tabela `tb_reclamacoes_salva`.
     
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute(f"DELETE FROM tb_reclamacoes_salva WHERE CR_Primaria = {CR}")
                conn.commit()
                cursor.close()
                self.close_connection(conn)
                print(f"Adm com Id {CR} foi deletado.")
            else:
                print("Conexão não estabelecida.")
        except Error as e:
            print(f"Erro ao deletar o registro: {e}")

    def fetch_Adm_nivel1(self):
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM tb_adm Where Nivel_de_Acesso = 1")  # Executa a consulta na tabela de Adm
                result = cursor.fetchall()  # Obtém todos os registros da tabela
                cursor.close()
                self.close_connection(conn)  # Fecha a conexão após a consulta
                return result
            else:
                print("Conexão não estabelecida.")
            return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None
        
            
    def fetch_Adm_nivel2(self):
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM tb_adm Where Nivel_de_Acesso = 2")  # Executa a consulta na tabela de Adm
                result = cursor.fetchall()  # Obtém todos os registros da tabela
                cursor.close()
                self.close_connection(conn)  # Fecha a conexão após a consulta
                return result
            else:
                print("Conexão não estabelecida.")
            return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None

            
    def fetch_Adm_nivel3(self):
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM tb_adm Where Nivel_de_Acesso = 3")  # Executa a consulta na tabela de Adm
                result = cursor.fetchall()  # Obtém todos os registros da tabela
                cursor.close()
                self.close_connection(conn)  # Fecha a conexão após a consulta
                return result
            else:
                print("Conexão não estabelecida.")
            return None
        except Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None
        
    def banir_Adm1(self, id):
        
            #Método para deletar um Adm com base no ID na tabela `tb_adm`.
        
            try:
                conn = self.connect()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute(f"DELETE FROM tb_adm WHERE Id = {id}")
                    conn.commit()
                    cursor.close()
                    self.close_connection(conn)
                    print(f"Adm com Id {id} foi deletado.")
                else:
                    print("Conexão não estabelecida.")
            except Error as e:
                print(f"Erro ao deletar o registro: {e}")

            
    def promover_Adm1(self, id):
        try:
            conn= self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute(f'UPDATE `tb_adm` set Nivel_de_Acesso = 2 where Id= {id}')
                conn.commit()
                cursor.close()
                self.close_connection(conn)
                print(f"ADM com Id {id} foi promovido ao nível 2.")
            else:
                print("Erro na conexão!")
        except Error as e:
            print(f"Erro ao deletar o registro: {e}")

    def promover_Adm3(self, id):
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute(f'UPDATE `tb_adm` SET Nivel_de_Acesso = 3 WHERE Id = {id}')
                conn.commit()
                cursor.close()
                self.close_connection(conn)
                print(f"ADM com Id {id} foi promovido ao nível 3.")
            else:
                print("Erro na conexão!")
        except Error as e:
            print(f"Erro ao atualizar o registro: {e}")

    def rebaixar_Adm2_para_1(self, id):
        try:
            conn = self.connect()
            if conn:
                cursor = conn.cursor()
                cursor.execute(f'UPDATE `tb_adm` SET Nivel_de_Acesso = 1 WHERE Id = {id} AND Nivel_de_Acesso = 2')
                conn.commit()
                cursor.close()
                self.close_connection(conn)
                print(f"ADM com Id {id} foi rebaixado ao nível 1.")
            else:
                print("Erro na conexão!")
        except Error as e:
            print(f"Erro ao atualizar o registro: {e}")

