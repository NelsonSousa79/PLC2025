import sys
import re

def tokenize(input_string):
    if not input_string.strip():  # Se a string estiver vazia ou só tiver espaços
        return []
        
    reconhecidos = []
    linha = 1
    
    # Expressão regular para todos os tokens da linguagem
    pattern = r'''
        (?P<KEYWORD>select|where|LIMIT|a\b)|
        (?P<VARIABLE>\?[a-zA-Z_][a-zA-Z0-9_]*)|
        (?P<PREFIX>[a-z]+:[a-zA-Z_][a-zA-Z0-9_]*)|
        (?P<STRING>"[^"]*"@[a-z]+)|
        (?P<INT>\d+)|
        (?P<SYMBOL>[{}])|
        (?P<PONTO>\.)|
        (?P<SKIP>[ \t])|
        (?P<NEWLINE>\n)|
        (?P<ERRO>.)
    '''
    
    mo = re.finditer(pattern, input_string, re.VERBOSE | re.IGNORECASE)
    
    for m in mo:
        dic = m.groupdict()
        start, end = m.span()
        
        if dic['KEYWORD']:
            t = ("KEYWORD", dic['KEYWORD'], linha, (start, end))
        elif dic['VARIABLE']:
            t = ("VARIABLE", dic['VARIABLE'], linha, (start, end))
        elif dic['PREFIX']:
            t = ("PREFIX", dic['PREFIX'], linha, (start, end))
        elif dic['STRING']:
            t = ("STRING", dic['STRING'], linha, (start, end))
        elif dic['INT']:
            t = ("INT", dic['INT'], linha, (start, end))
        elif dic['SYMBOL']:
            t = ("SYMBOL", dic['SYMBOL'], linha, (start, end))
        elif dic['PONTO']:
            t = ("PONTO", dic['PONTO'], linha, (start, end))
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, (start, end))
            linha += 1
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, (start, end))
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, (start, end))
        else:
            t = ("UNKNOWN", m.group(), linha, (start, end))
        
        if not dic['SKIP']:
            reconhecidos.append(t)
            
    return reconhecidos

def main():
    print("Analisador Léxico para Linguagem de Query")
    print("Digite sua query (Ctrl+D para terminar):")
    
    try:
        input_text = sys.stdin.read()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo utilizador")
        return
    
    # Verifica se o input está vazio (Ctrl+D sem escrever nada)
    if not input_text:
        print("Nenhum input recebido. A terminar...")
        return
        
    tokens = tokenize(input_text)
    
    if not tokens:
        print("Nenhum token reconhecido.")
        return
    
    # Output no formato das tuplas Python (como no exemplo dos parênteses)
    for token in tokens:
        tipo, valor, linha, pos = token
        # Formata o valor para escapar caracteres especiais
        if valor == '\n':
            valor_formatado = '\\n'
        else:
            valor_formatado = valor
        print(f"('{tipo}', '{valor_formatado}', {linha}, {pos})")

# Versão alternativa com leitura linha a linha
def main_interactive():
    print("Analisador Léxico para Linguagem de Query")
    print("Digite sua query (linha vazia para terminar):")
    
    lines = []
    while True:
        try:
            line = input()
            if line == "":  # Linha vazia para terminar
                break
            lines.append(line)
        except EOFError:  # Ctrl+D pressionado
            break
        except KeyboardInterrupt:  # Ctrl+C pressionado
            print("\nPrograma interrompido")
            return
    
    if not lines:
        print("Nenhum input recebido.")
        return
        
    input_text = "\n".join(lines) + "\n"  # Adiciona newline no final
    tokens = tokenize(input_text)
    
    if not tokens:
        print("Nenhum token reconhecido.")
        return
    
    # Output no formato das tuplas Python
    for token in tokens:
        tipo, valor, linha, pos = token
        if valor == '\n':
            valor_formatado = '\\n'
        else:
            valor_formatado = valor
        print(f"('{tipo}', '{valor_formatado}', {linha}, {pos})")

# Teste com o exemplo fornecido
if __name__ == "__main__":
    # Teste automático com a query exemplo
    query_exemplo = '''select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
'''
    
    print("Teste com query exemplo:")
    tokens = tokenize(query_exemplo)
    for token in tokens:
        tipo, valor, linha, pos = token
        if valor == '\n':
            valor_formatado = '\\n'
        else:
            valor_formatado = valor
        print(f"('{tipo}', '{valor_formatado}', {linha}, {pos})")
    
    # Para testar interativamente, descomenta a linha abaixo:
    # main_interactive()