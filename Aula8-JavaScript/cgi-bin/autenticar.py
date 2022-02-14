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
# Verificar usuário e senha enviados pelo formulário
# ---------------------------------------------------
# ---------------------------------------------------
# Passo 1: Recupera os campos enviados pela tela de autenticação
# ---------------------------------------------------
formulario = cgi.FieldStorage() 
usuForm = formulario.getvalue('usuario')
pswForm = formulario.getvalue('senha')
# ---------------------------------------------------
# Passo 2: Definindo um dicionário de senhas para fazer o
#          papel de banco de dados da aplicação.
# ---------------------------------------------------
senhas = {'aluno1':'abcd','aluno2':'1234','aluno3':'aeiou'}
# ---------------------------------------------------
# Passo 3: Testando se o usuário e senha informados
# ---------------------------------------------------
msg = ''
cookieUsuario=''
if (usuForm in senhas):  # Usuário existe. Testando se a senha está correta.
    if (senhas[usuForm] == pswForm):
        msg = 'Usuário [' + usuForm + '] autenticado.'
        cookieUsuario=usuForm
    else:  # Usuário existe, mas a senha está incorreta.
        msg = 'Usuário [' + usuForm + '] Senha incorreta.'
        cookieUsuario=';expires=Thu, 21 Sep 1979 00:00:01 UTC'
else:  # Usuário não existe 
    msg = 'Usuário [' + usuForm + '] não existe.'
    cookieUsuario=';expires=Thu, 21 Sep 1979 00:00:01 UTC'
# ---------------------------------------------------
# Passo 4: Montando e devolvendo uma página como resposta
# ---------------------------------------------------
# Cabeçalho (IMPORTANTE: tem que ser a primeira coisa a enviar)
print('Content-type: text/html;charset=utf-8')
print('Set-Cookie: usuario='+cookieUsuario+'; path=/')
print('')  # Uma linha vazia indica o fim do cabeçalho
print('''
<!DOCTYPE html>
<html>
    <head></head>
    <body>
        <h1>Resposta do servidor:</h2>
        <p style="color:purple;" id="mensagem"></p>
        <p>Clique <a href="http://localhost:8000/">AQUI</a>
            para retornar à página inicial</p>
        <script>
''')
print('document.getElementById("mensagem").innerHTML = "'+msg+'";')
print('''
        </script>
    </body>
</html>
''')
# ----------------------------------------------------
