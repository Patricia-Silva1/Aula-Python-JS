#!/usr/bin/env python3

# ---------------------------------------------------
# Importando bibliotecas 
# ---------------------------------------------------
# (CGI = "Common Gateway Interface")
# Um padrão de script para escrita de programas interativos
# para tratar requisições ao servidor por meio de biblioteca
import cgi
# Formatação da saída padrão e conjunto de caracteres (opcional)
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# ---------------------------------------------------
# Lógica do script:
# Recebe os dados do formulário e exibe cada campo em
# uma linha.
# ---------------------------------------------------
# ---------------------------------------------------
# Passo 1: Recupera os campos enviados pela tela de autenticação
# ---------------------------------------------------
formulario = cgi.FieldStorage()
# ---------------------------------------------------
# Passo 2: Montando e devolvendo uma página como resposta
# ---------------------------------------------------
# Cabeçalho (IMPORTANTE: tem que ser a primeira coisa a enviar)
print('Content-type: text/html;charset=utf-8')
print('')  # Uma linha vazia indica o fim do cabeçalho
print('''
<!DOCTYPE html>
<html>
    <body>
        <h1>Resposta do servidor:</h2>
        <h2>Campos Enviados pelo Formulário</h2>
        <p style="color:blue;">
''')
for cp in formulario.keys():
    campo = str(cp)
    print(campo+'='+str(formulario.getvalue(campo))+'<br>')
print('''
        </p>
        <p>Clique <a href="http://localhost:8000/">AQUI</a>
            para retornar à página inicial</p>
    </body>
</html>
''')
# ----------------------------------------------------
