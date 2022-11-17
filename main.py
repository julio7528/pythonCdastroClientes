import sqlite3
import os
from datetime import datetime

def clear():
    os.system("cls")

def log(message):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open('log.txt','a+') as f:
        f.write(f'Log:{dt_string} - {message}\n')

def menu():
    global navegador
    os.system("cls")
    print('Selecione uma opção:')
    print(f'\t[1] Listar Clientes')
    print(f'\t[2] Cadastrar Clientes')
    print(f'\t[3] Editar Clientes')
    print(f'\t[4] Apagar Clientes')
    navegador = input()
    return navegador

clear()
log('***** INICIO DA MAIN *****')

try:
    #Connect to Database
    sqliteConnection = sqlite3.connect('database.db')
    cursor = sqliteConnection.cursor()
    log("Database created and Successfully Connected to SQLite")
    #Select Query Version
    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    log(f'SQLite Database Version is: , {str(record)}')
    #Check Table exists or need to create
    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Cad_Cliente' ''')
    if cursor.fetchone()[0]==1 : 
        log('Table already exists.')
    else:    
        log('Table not exists - creating.')
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Cad_Cliente (
                                        ID       INTEGER    PRIMARY KEY ASC AUTOINCREMENT
                                                            NOT NULL,
                                        NOME     TEXT (250) NOT NULL,
                                        IDADE    INTEGER    NOT NULL,
                                        ENDERECO TEXT (250) NOT NULL,
                                        NUMERO   INTEGER    NOT NULL,
                                        CIDADE   TEXT (50)  NOT NULL
                                    );'''
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
    log("SQLite table created")

    acessoMenu = True
    while acessoMenu:
        menu()
        if navegador == str('1'):
            cursor.execute("SELECT * FROM Cad_Cliente order by ID asc")
            myresult = cursor.fetchall()
            for x in myresult:
                print(x)
            log('Realizado consulta de cadastro')
            
            continuar = input('Voltar para o Menu? [S]Sim [N]Não ')
            if continuar == 'S' or continuar == 's':
                acessoMenu = True
            elif continuar == 'N' or continuar == 'n' :
                acessoMenu = False
            else:
                print('Selecionou uma opção inválida')
                exit()    
        elif navegador == str('2'):
            nome = input('Digite nome: ')
            idade = input('Digite idade: ')
            endereco = input('Digite endereco: ')
            numero = input('Digite numero: ')
            cidade = input('Digite cidade: ')

            cursor.execute("insert into Cad_Cliente (NOME, IDADE, ENDERECO, NUMERO, CIDADE) values (?, ?, ?, ?, ?)",
                (nome, idade, endereco, numero, cidade))
            sqliteConnection.commit()
            log(f'Realizado Cadastro dos dados: {nome}, {idade}, {endereco}, {numero}, {cidade}')
        elif navegador == str('3'):       
            relatorio = input('Gostaria de Consultar o relatorio completo Antes? [S]Sim [N]Não ')
            if relatorio == 'S' or relatorio == 's':
                        cursor.execute("SELECT * FROM Cad_Cliente order by NOME asc")
                        myresult = cursor.fetchall()
                        for x in myresult:
                            print(x)
            elif relatorio == 'N' or relatorio == 'n':
                clear()
            else:
                print('Opção Inválida')
                exit()
            busca = input('Digite tipo de Busca: [N]Nome ou [I]ID ')
            if busca == 'N' or busca == 'n':
                nome = input('Digite nome: ')
                clear()
                print(f'Resultado para {nome}')
                cursor.execute("SELECT ID, IDADE, ENDERECO, NUMERO, CIDADE FROM Cad_Cliente WHERE NOME = ?", (nome,))
                myresult = cursor.fetchall()
                for x in myresult:                
                    print(x)
                selecionar = input('[I]DADE, [E]NDERECO, [N]UMERO, [C]IDADE ')
                log(f'Alterou dado {selecionar} de {nome}')
                if selecionar == 'I' or selecionar == 'i':
                    selecionar = input('DIGITE A IDADE PARA ATUALIZAR: ')
                    cursor.execute("UPDATE Cad_Cliente SET IDADE = ? WHERE NOME = ? ", (selecionar, nome,))
                    sqliteConnection.commit()            
                elif selecionar == 'E' or selecionar == 'e':
                    selecionar = input('DIGITE A IDADE PARA ATUALIZAR: ')
                    cursor.execute("UPDATE Cad_Cliente SET ENDERECO = ? WHERE NOME = ? ", (selecionar, nome,))
                    sqliteConnection.commit()
                elif selecionar == 'N' or selecionar == 'N':
                    selecionar = input('DIGITE A IDADE PARA ATUALIZAR: ')
                    cursor.execute("UPDATE Cad_Cliente SET NUMERO = ? WHERE NOME = ? ", (selecionar, nome,))
                    sqliteConnection.commit()
                elif selecionar == 'C' or selecionar == 'c':
                    selecionar = input('DIGITE A IDADE PARA ATUALIZAR: ')
                    cursor.execute("UPDATE Cad_Cliente SET CIDADE = ? WHERE NOME = ? ", (selecionar, nome,))
                    sqliteConnection.commit()
                else:
                    print('Selecionou uma opção inválida')
                    exit()

                print(f'Cliente {nome} atualizado com sucesso!')
            elif busca == 'I' or busca == 'i':
                ide = input('Digite ID: ')
                clear()
                print(f'Resultado para ID:{ide}')
                cursor.execute("SELECT NOME, IDADE, ENDERECO, NUMERO, CIDADE FROM Cad_Cliente WHERE ID = ?", (ide,))
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x)
                selecionar = input('[NO]NOME, [I]DADE, [E]NDERECO, [N]UMERO, [C]IDADE ')
                log(f'Alterou dado {selecionar} de {ide}')
                if selecionar == 'I' or selecionar == 'i':
                    selecionar = input('DIGITE A IDADE PARA ATUALIZAR: ')
                    cursor.execute("UPDATE Cad_Cliente SET IDADE = ? WHERE ID = ? ", (selecionar, ide,))
                    sqliteConnection.commit()            
                elif selecionar == 'E' or selecionar == 'e':
                    selecionar = input('DIGITE A IDADE PARA ATUALIZAR: ')
                    cursor.execute("UPDATE Cad_Cliente SET ENDERECO = ? WHERE ID = ? ", (selecionar, ide,))
                    sqliteConnection.commit()
                elif selecionar == 'N' or selecionar == 'N':
                    selecionar = input('DIGITE A IDADE PARA ATUALIZAR: ')
                    cursor.execute("UPDATE Cad_Cliente SET NUMERO = ? WHERE ID = ? ", (selecionar, ide,))
                    sqliteConnection.commit()
                elif selecionar == 'C' or selecionar == 'c':
                    selecionar = input('DIGITE A IDADE PARA ATUALIZAR: ')
                    cursor.execute("UPDATE Cad_Cliente SET CIDADE = ? WHERE ID = ? ", (selecionar, ide,))
                    sqliteConnection.commit()
                elif selecionar == 'NO' or selecionar == 'no':
                    selecionar = input('DIGITE O NOME PARA ATUALIZAR: ')
                    cursor.execute("UPDATE Cad_Cliente SET NOME = ? WHERE ID = ? ", (selecionar, ide,))
                    sqliteConnection.commit()
                else:
                    print('Selecionou uma opção inválida')
                    exit()
                print(f'Cliente {ide} atualizado com sucesso!')
                
                continuar = input('Voltar para o Menu? [S]Sim [N]Não ')
                if continuar == 'S' or continuar == 's':
                    acessoMenu = True
                elif continuar == 'N' or continuar == 'n' :
                    acessoMenu = False
                else:
                    print('Selecionou uma opção inválida')
                    exit() 
        elif navegador == str('4'):
            relatorio = input('Gostaria de Consultar o relatorio completo Antes? [S]Sim [N]Não ')
            if relatorio == 'S' or relatorio == 's':
                        cursor.execute("SELECT * FROM Cad_Cliente order by NOME asc")
                        myresult = cursor.fetchall()
                        for x in myresult:
                            print(x)
            elif relatorio == 'N' or relatorio == 'n':
                clear()
            else:
                print('Opção Inválida')
                exit()        
            ide = input('Digite o ID que será apagado: ')
            confirma = input(f'Tem Certeza que deseja apagar dados do ID {ide}? [S]Sim [N]Não ')
            if confirma == 'S' or confirma =='s':
                cursor.execute("DELETE FROM Cad_Cliente WHERE ID = ? ", (ide,))
                sqliteConnection.commit()
                print(f'Cliente {ide} apagado com sucesso!')
                log(f'Cliente {ide} apagado')
            elif confirma == 'N' or confirma =='n':
                exit()
            else:
                exit()
        else:
            print('Selecionou uma opção inválida')
        continuar = input('Voltar para o Menu? [S]Sim [N]Não ')
        if continuar == 'S' or continuar == 's':
            acessoMenu = True
        elif continuar == 'N' or continuar == 'n' :
            acessoMenu = False
        else:
            print('Selecionou uma opção inválida')
            exit()    

    
    cursor.close()

except sqlite3.Error as error:
    log(f'Error while connecting to sqlite, {str(error)}')

finally:
    if sqliteConnection:
        sqliteConnection.close()
        log("The SQLite connection is closed")
    log('***** FIM DA MAIN *****')
