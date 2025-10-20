import json
from datetime import datetime

def carregar_stock():
    """Carrega os dados do ficheiro stock.json"""
    try:
        with open('stock.json', 'r', encoding='utf-8') as ficheiro:
            return json.load(ficheiro)
    except FileNotFoundError:
        print("Erro: Ficheiro stock.json não encontrado!")
        return []
    except json.JSONDecodeError:
        print("Erro: Ficheiro stock.json corrompido!")
        return []

def guardar_stock(dados):
    """Guarda os dados no ficheiro stock.json"""
    try:
        with open('stock.json', 'w', encoding='utf-8') as ficheiro:
            json.dump(dados, ficheiro, ensure_ascii=False, indent=4)
        print("Stock guardado com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao guardar stock: {e}")
        return False

def listar_produtos(dados):
    """Lista todos os produtos em stock"""
    if not dados:
        print("Não há produtos em stock.")
        return
    
    print("\n--- STOCK ATUAL ---")
    print("cod | nome           | quantidade | preço")
    print("----------------------------------------")
    for produto in dados:
        print(f"{produto['cod']:3} | {produto['nome']:14} | {produto['quant']:10} | {produto['preco']:5.2f}€")
    print(f"Total de produtos: {len(dados)}")

def adicionar_produto(dados):
    """Adiciona um novo produto ou aumenta stock se já existir"""
    print("\n--- ADICIONAR PRODUTO ---")
    
    codigo = input("Código do produto (ex: A23): ").strip().upper()
    if not codigo:
        print("Erro: Código não pode estar vazio!")
        return dados
    
    # Verificar se código já existe
    for produto in dados:
        if produto['cod'] == codigo:
            # Produto já existe, aumentar stock
            try:
                quantidade = int(input(f"Quantidade a adicionar ao '{produto['nome']}': ").strip())
                if quantidade < 0:
                    print("Erro: Quantidade não pode ser negativa!")
                    return dados
                produto['quant'] += quantidade
                print(f"Stock de '{produto['nome']}' aumentado para {produto['quant']} unidades!")
                return dados
            except ValueError:
                print("Erro: Quantidade deve ser um número inteiro!")
                return dados
    
    # Produto não existe, criar novo
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Erro: Nome não pode estar vazio!")
        return dados
    
    try:
        quantidade = int(input("Quantidade: ").strip())
        if quantidade < 0:
            print("Erro: Quantidade não pode ser negativa!")
            return dados
    except ValueError:
        print("Erro: Quantidade deve ser um número inteiro!")
        return dados
    
    try:
        preco = float(input("Preço (€): ").strip())
        if preco <= 0:
            print("Erro: Preço deve ser maior que 0!")
            return dados
    except ValueError:
        print("Erro: Preço deve ser um número!")
        return dados
    
    # Criar novo produto
    novo_produto = {
        "cod": codigo,
        "nome": nome,
        "quant": quantidade,
        "preco": preco
    }
    
    dados.append(novo_produto)
    print(f"Produto '{nome}' adicionado com sucesso!")
    return dados

def remover_produto(dados):
    """Remove unidades de um produto ou remove completamente se stock chegar a 0"""
    if not dados:
        print("Não há produtos para remover.")
        return dados
    
    print("\n--- REMOVER PRODUTO ---")
    codigo = input("Código do produto: ").strip().upper()
    
    # Procurar o produto
    for i, produto in enumerate(dados):
        if produto['cod'] == codigo:
            print(f"Produto encontrado: {produto['nome']} (Stock atual: {produto['quant']})")
            
            try:
                quantidade_remover = int(input("Quantidade a remover: ").strip())
                if quantidade_remover <= 0:
                    print("Erro: Quantidade deve ser maior que 0!")
                    return dados
                
                if quantidade_remover > produto['quant']:
                    print(f"Erro: Só existem {produto['quant']} unidades em stock!")
                    return dados
                
                # Remover unidades
                produto['quant'] -= quantidade_remover
                
                # Verificar se stock chegou a 0
                if produto['quant'] == 0:
                    confirmacao = input("Stock chegou a 0. Deseja remover o produto completamente da máquina? (s/N): ").strip().lower()
                    if confirmacao == 's':
                        produto_removido = dados.pop(i)
                        print(f"Produto '{produto_removido['nome']}' removido completamente da máquina!")
                    else:
                        print(f"Produto '{produto['nome']}' mantido com 0 unidades de stock.")
                else:
                    print(f"Removidas {quantidade_remover} unidades de '{produto['nome']}'. Stock restante: {produto['quant']}")
                
                return dados
                
            except ValueError:
                print("Erro: Quantidade deve ser um número inteiro!")
                return dados
    
    print(f"Produto com código '{codigo}' não encontrado.")
    return dados

def menu_administrador():
    """Menu principal do administrador"""
    dados = carregar_stock()
    if dados is None:
        return
    
    print("\n" + "="*50)
    print("        SISTEMA ADMINISTRADOR - MÁQUINA DE VENDING")
    print("="*50)
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("Digite AJUDA para ver os comandos disponíveis")
    
    while True:
        comando = input("\nadmin>> ").strip().upper()
        
        if comando == "SAIR":
            if guardar_stock(dados):
                print("Alterações guardadas. Até à próxima!")
            break
            
        elif comando == "LISTAR":
            listar_produtos(dados)
            
        elif comando == "ADICIONAR":
            dados = adicionar_produto(dados)
            
        elif comando == "REMOVER":
            dados = remover_produto(dados)
            
        elif comando == "AJUDA" or comando == "HELP":
            print("\n--- COMANDOS DISPONÍVEIS ---")
            print("LISTAR    - Mostra todos os produtos em stock")
            print("ADICIONAR - Adiciona novo produto ou aumenta stock")
            print("REMOVER   - Remove unidades de um produto")
            print("AJUDA     - Mostra esta mensagem")
            print("SAIR      - Guarda alterações e encerra")
            
        elif comando == "":
            continue
            
        else:
            print(f"Comando '{comando}' não reconhecido. Digite AJUDA para ver os comandos.")

# Executar o programa
if __name__ == "__main__":
    menu_administrador()