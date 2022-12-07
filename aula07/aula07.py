curso = "curso de python"


res = "pythonm" in curso  # verifica se em curso existe a palavra python
res1 = "python" not in curso
print(res1)


texto = "Curso de Python"
palavra = "Python"
res2 = palavra in texto
print(res2)


texto2 = "Curso de PYTHON"
palavra2 = "python"
res2 = palavra2.upper() in texto2.upper()
"""neste caso passamos tudo para maiusculo pois a busca de python não encontraria PYTHON,
 porém sanamos este problema colocando tudo em maiusculo"""


print(res2)
cidade = "Belo Horizonte"
dia = 15
mes = "Dezembro"
ano = 2022
tarefa = "Exemplo de Python"
# neste caso, o método .format auxilia na concatenação de informações
# neste caso usamos \" para acrescer aspas sem que atrapalhe as aspas iniciais
data = "{}, {} de {} de {}\n\"{}\""
# são chamados caracteres de escape (\n, \"", \r, \t, \b)
print(data.format(cidade, dia, mes, ano, tarefa))
