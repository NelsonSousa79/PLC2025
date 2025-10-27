from analisador_lex import lexer

token_atual = None

def erro_sintaxe(token):
    print(f"Erro de sintaxe: token inesperado {token}")

def consumir(tipo_esperado):
    global token_atual
    if token_atual and token_atual.type == tipo_esperado:
        token_atual = lexer.token()
    else:
        erro_sintaxe(token_atual)


def analisar_E():
    global token_atual
    print("E -> T (op T)*")
    
    # Primeiro T
    if token_atual and token_atual.type == 'INT':
        print("T -> INT")
        consumir('INT')
        print("Reconheci T -> INT")
    elif token_atual and token_atual.type == 'P_OP':
        print("T -> ( E )")
        consumir('P_OP')
        analisar_E()
        consumir('P_CLS')
        print("Reconheci T -> ( E )")
    else:
        erro_sintaxe(token_atual)
    
    # Zero ou mais (op T)
    while token_atual and token_atual.type in ['SUM', 'DIF', 'MUL', 'DIV']:
        operador = token_atual.type
        print(f"op -> {operador}")
        consumir(operador)
        print(f"Reconheci op -> {operador}")
        
        # Próximo T
        if token_atual and token_atual.type == 'INT':
            print("T -> INT")
            consumir('INT')
            print("Reconheci T -> INT")
        elif token_atual and token_atual.type == 'P_OP':
            print("T -> ( E )")
            consumir('P_OP')
            analisar_E()
            consumir('P_CLS')
            print("Reconheci T -> ( E )")
        else:
            erro_sintaxe(token_atual)
    
    print("Reconheci E -> T (op T)*")

def iniciar_analise(entrada):
    global token_atual
    lexer.input(entrada)
    token_atual = lexer.token()
    
    if token_atual is None:
        print("Entrada vazia!")
        return
    
    analisar_E()
    
    if token_atual is not None:
        print(f"Atenção: símbolos não processados: {token_atual}")
    else:
        print("Análise terminada com sucesso!")