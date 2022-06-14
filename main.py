from flask import Flask, jsonify
from rom import rom_parse, rom_generate

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def homepage():
    
    return '<h2>A API está no ar, digite "/alguma_palavra_qualquer" na sua barra de pesquisa para acessar a API, ou faça uma requisição http para o link: https://convertromanapi.herokuapp.com/</h2><br><h3>Esta API converte algarismos romanos em inteiros ou retorna o maior algarismo/valor encontrado em uma palavra ou frase, você escolhe!</h3>'


# RECEBE UMA PALAVRA E RETORNA O MAIOR ALGARISMO ROMANO ENCONTRADO
@app.route("/<alfanumericos>")
def search(alfanumericos): 
    
    # TRANSFORMA A STRING RECEBIDA EM UMA LISTA
    resposta = [*alfanumericos.upper()]

    # APLICA "CAIXA ALTA" NA STRING RECEBIDA 
    resposta2 = alfanumericos.upper()
    
    valores_permitidos = ["I", "V", "X", "L", "C", "D", "M"]

    i = 0
    lista = []
    lista_romanos = []
    lista_valores = []
    lista_resultado = []


    # CRIA UMA LISTA COM NUMEROS INTEIROS DE 1 A 3999 
    while i < 3999:
        i += 1
        lista.append(i)

    # GERA UMA LISTA COM TODOS OS NUMEROS ROMANOS POSSIVEIS DE 1 A 3999(MAIOR ALGARISMO ROMANO POSSIVEL DE ESCREVER)
    for u in lista:
        string = rom_generate(u)
        lista_romanos.append(string)

    # GERA UMA LISTA COM OS ALGARISMOS ROMANOS ENCONTRADOS NA STRING RECEBIDA
    for elemento in lista_romanos:
        if elemento in resposta2:
            lista_valores.append(elemento)

    # GERA UMA LISTA COM OS ALGARISMOS ROMANOS ENCONTRADOS NA STRING RECEBIDA CONVERTIDOS EM INTEIROS
    for o in lista_valores:
        string = rom_parse(o)
        lista_resultado.append(string)

    try:
        # VERIFICA QUAL É E ATRIBUI A "VALUE" O MAIOR VALOR ENCONTRADO NA LISTA DE ROMANOS CONVERTIDOS EM INTEIROS
        value = max(lista_resultado) 
        # CONVERTE O MAIOR VALOR ENCONTRADO PARA ROMANOS E ATRIBUI A "NUMBER"
        number = rom_generate(value)
    except ValueError:
        # CASO O INPUT RECEBIDO NÃO CONTENHA PELO MENOS 1 ALGARISMO ROMANO 
        value = "Requisição inválida, a palavra digitada não contem nenhum algarismo romano."
        number = "Requisição inválida, a palavra digitada não contem nenhum algarismo romano."




    for item in resposta:
        if item not in valores_permitidos:
            pos = resposta.index(item)
            resposta[pos] = "-" # substitui itens não permitidos por um "-"


    
    
    return jsonify({"requisição": resposta}, {"value": value, "number": number})
            


    
if __name__ == '__main__':
    app.run()


