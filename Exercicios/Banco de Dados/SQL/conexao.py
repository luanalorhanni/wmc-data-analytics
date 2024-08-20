import sqlite3

#Criando a conexão
conexao = sqlite3.connect('db-teste')
cursor = conexao.cursor()

#Tabela criada - CREATE
#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100))')

#Modificando a tabela - RENAME TO
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')

#Criando uma coluna com erro - ALTER TABLE
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')

#Renomeando a coluna com erro - RENAME COLUMN
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')            

#Excluindo uma tabela - DROP
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100))')
#cursor.execute('DROP TABLE produtos')

#Adicionando dados - INSERT
#cursor.execute('INSERT INTO usuario(id,nome,endereco) VALUES(0,"Luana","Cohatrac")')
# cursor.execute('INSERT INTO usuario(id,nome,endereco) VALUES(1,"Maria","Cohatrac2")')
# cursor.execute('INSERT INTO usuario(id,nome,endereco) VALUES(2,"Joana","Cohatrac3")')
# cursor.execute('INSERT INTO usuario(id,nome,endereco) VALUES(3,"Fernanda","Cohatrac4")')

#Deletando dados da tabela - DELETE FROM
#cursor.execute('DELETE FROM usuario where id=3')

#Ordenando informações - ORDER BY
# total = cursor.execute('SELECT * FROM usuario ORDER BY nome') #Ordem alfabética
# for usuario in total:
#     print(usuario)

# total = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC') #Ordem decrescente
# for usuario in total:
#     print(usuario)

#GROUP BY e HAVING
# dados = cursor.execute('SELECT id,nome FROM usuario GROUP BY nome') #Ordem decrescente
# for usuario in dados:
#     print(usuario)
# #Groupby não tem clásula WHERE
# having = cursor.execute('SELECT endereco,nome FROM usuario GROUP BY nome HAVING id>0')
# for usuario in having:
#     print(usuario)    
      
#Dados limitados ou distintos - LIMIT e DISTINCT
# limitado = cursor.execute('SELECT * FROM usuario LIMIT 3')
# for usuario in limitado:
#     print(usuario)

# distinto = cursor.execute('SELECT DISTINCT * FROM usuario')
# for usuario in distinto:
#     print(usuario)   
    
#Visualizando informações - SELECT
# total = cursor.execute('SELECT * FROM usuario')
# for usuario in total:
#     print(usuario)

# nome = cursor.execute('SELECT nome FROM usuario')
# for usuario in nome:
#     print(usuario)
    
# nome_telefone = cursor.execute('SELECT nome, telefone FROM usuario')
# for usuario in nome_telefone:
#     print(usuario)    
    
# condicao = cursor.execute('SELECT email FROM usuario WHERE id>1')    
# for usuario in condicao:
#     print(usuario) 

#Alterando dados em linhas - UPDATE
#cursor.execute('UPDATE usuario SET endereco="Angelim" WHERE endereco="Cohatrac3"')

#Diferentes tipos de JOIN's - Lidando com informações de duas tabelas
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100))')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco) VALUES(1,"Maria","Cohatrac2")')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco) VALUES(11,"Vanessa","Anjo da Guarda")')

#INNER JOIN - Saber onde os ids forem iguais 
# usuarios = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')
# for i in usuarios:
#     print(i)

# #LEFT JOIN - Saber onde os ids forem iguais da tabela da esquerda, correspondente a da direita
# usuarios = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.nome = gerentes.nome')
# for i in usuarios:
#     print(i)

# #RIGHT JOIN - Saber onde os ids forem iguais da tabela da direita, correspondente a da esquerda
# usuarios = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.nome = gerentes.nome')
# for i in usuarios:
#     print(i)
      
# #FULL JOIN - Saber onde os ids forem iguais da tabela como um tipo
# usuarios = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')
# for i in usuarios:
#     print(i)      
    
#SUB-CONSULTAS ou SUB-SELECT
#Irá selecionar todos os usuarios onde o nome esteja em gerentes
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN(SELECT nome FROM gerentes)')    
for i in dados:
    print(i)

      
#Confirmando alterações
conexao.commit()
conexao.close