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
# O script apenas envia uma página contendo uma mensagem
# onde avisa que o servidor recebeu a requisição, mas 
# não faz nenhum tratamento com os dados captados.
# ---------------------------------------------------
# ---------------------------------------------------
# Passo 1: Montando e devolvendo uma página como resposta
# ---------------------------------------------------
# Cabeçalho (IMPORTANTE: tem que ser a primeira coisa a enviar)
print('Content-type: text/html;charset=utf-8')
print('')  # Uma linha vazia indica o fim do cabeçalho
print('''
<!DOCTYPE html>
<html>
    <body>
        <h1>Resposta do servidor: Alô Mundo!</h1>
        <h1>Funcionou!</h1>
        <p style="color:red;">
            Esta página foi construída pelo servidor<br>
            para servir de resposta padrão a qualquer<br>
            requisição enviada por uma página HTML.</p>
        <p style="color:blue;" id="resp"></p>
        <p>Clique <a href="http://localhost:8000/">AQUI</a>
            para retornar à página inicial</p>
        <script>
            document.getElementById("resp").innerHTML = new Date();
        </script>
    </body>
</html>
''')
# ----------------------------------------------------
