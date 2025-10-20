import json
from datetime import datetime

# Abrir e ler o ficheiro JSON
with open('stock.json', 'r', encoding='utf-8') as ficheiro:
    dados = json.load(ficheiro)

# Moedas válidas em cêntimos
moedas_validas = {
    '1c': 1, '2c': 2, '5c': 5, '10c': 10, '20c': 20, '50c': 50,
    '1e': 100, '2e': 200, '5e': 500, '10e': 1000, '20e': 2000, 
    '50e': 5000, '100e': 10000, '200e': 20000, '500e': 50000
}

saldo = 0  # Saldo em cêntimos

# Agora podes aceder aos dados
data_atual = datetime.now().date()
print("maq: " + str(data_atual) + ", Stock carregado, Estado atualizado.")
print("maq: Bom dia. Estou disponível para atender o seu pedido.")

def formatar_saldo(saldo_centimos):
    """Converte saldo em cêntimos para formato legível"""
    euros = saldo_centimos // 100
    centimos = saldo_centimos % 100
    
    if euros > 0 and centimos > 0:
        return f"{euros}e{centimos}c"
    elif euros > 0:
        return f"{euros}e"
    else:
        return f"{centimos}c"

def calcular_troco(saldo_centimos):
    """Calcula o troco em moedas"""
    if saldo_centimos == 0:
        return "0c"
    
    troco_moedas = []
    saldo_restante = saldo_centimos
    
    # Moedas ordenadas por valor descendente
    moedas_ordenadas = [
        ('500e', 50000), ('200e', 20000), ('100e', 10000), ('50e', 5000), ('20e', 2000), ('10e', 1000),
        ('5e', 500), ('2e', 200), ('1e', 100), ('50c', 50), ('20c', 20), ('10c', 10), ('5c', 5), ('2c', 2), ('1c', 1)
    ]
    
    for moeda, valor in moedas_ordenadas:
        if saldo_restante >= valor:
            quantidade = saldo_restante // valor
            saldo_restante %= valor
            if quantidade > 0:
                troco_moedas.append(f"{quantidade}x {moeda}")
    
    # Formatar a mensagem do troco
    if len(troco_moedas) == 1:
        return troco_moedas[0] + "."
    elif len(troco_moedas) == 2:
        return f"{troco_moedas[0]} e {troco_moedas[1]}."
    else:
        return ", ".join(troco_moedas[:-1]) + f" e {troco_moedas[-1]}."
    
def guardar_stock():
    """Guarda as alterações no ficheiro stock.json"""
    try:
        with open('stock.json', 'w', encoding='utf-8') as ficheiro:
            json.dump(dados, ficheiro, ensure_ascii=False, indent=4)
        print("maq: Stock atualizado e guardado com sucesso!")
    except Exception as e:
        print(f"maq: Erro ao guardar stock: {e}")

# Sistema de inputs interativo
while True:
    comando = input(">> ").strip()
    
    if comando.upper() == "SAIR":
        # Calcular e mostrar troco se houver saldo
        if saldo > 0:
            troco = calcular_troco(saldo)
            print(f"maq: Pode retirar o troco: {troco}")
            saldo = 0  # Reset do saldo
        else:
            print("maq: Não há troco para retirar.")
        
        # Guardar as alterações no stock antes de sair
        guardar_stock()
        print("maq: Até à próxima!")
        break
        
    elif comando.upper() == "LISTAR":
        print("maq:")
        print("cod | nome      | quantidade | preço")
        print("---------------------------------")
        for produto in dados:
            print(f"{produto['cod']:3} | {produto['nome']:9} | {produto['quant']:10} | {produto['preco']:5.2f}€")
            
    elif comando.upper().startswith("MOEDA"):
        # Extrair a parte das moedas (remover "MOEDA")
        texto_moedas = comando[5:].strip()
        
        # Verificar se termina com ponto
        if not texto_moedas.endswith('.'):
            print("maq: Formato inválido. Deve terminar com '.'")
            continue
            
        # Remover o ponto final
        texto_moedas = texto_moedas[:-1].strip()
        
        # Dividir por vírgulas
        moedas = [moeda.strip() for moeda in texto_moedas.split(',')]
        
        # Processar cada moeda
        total_adicionado = 0
        
        for moeda in moedas:
            # Usar a moeda diretamente (já está em minúsculas no dicionário)
            if moeda in moedas_validas:
                total_adicionado += moedas_validas[moeda]
        
        # Atualizar saldo
        saldo += total_adicionado
        
        # Mostrar resultado
        print(f"maq: Saldo = {formatar_saldo(saldo)}")
    
    elif comando.upper().startswith("SELECIONAR"):
        # Extrair o código do produto
        partes = comando.split()
        if len(partes) < 2:
            print("maq: Comando inválido. Use: SELECIONAR <código>")
            continue
            
        codigo = partes[1].upper()
        
        # Procurar o produto
        produto_encontrado = None
        for produto in dados:
            if produto['cod'].upper() == codigo:
                produto_encontrado = produto
                break
        
        if produto_encontrado is None:
            print(f"maq: Produto {codigo} não encontrado")
            continue
            
        # Verificar stock
        if produto_encontrado['quant'] <= 0:
            print(f"maq: Produto {produto_encontrado['nome']} sem stock")
            continue
            
        # Verificar saldo
        preco_centimos = int(produto_encontrado['preco'] * 100)  # Converter para cêntimos
        if saldo >= preco_centimos:
            # Processar compra
            saldo -= preco_centimos
            produto_encontrado['quant'] -= 1
            
            # Verificar se o stock chegou a 0 e remover o produto
            if produto_encontrado['quant'] == 0:
                dados.remove(produto_encontrado)
                print(f'maq: Pode retirar o produto dispensado "{produto_encontrado["nome"]}"')
                print(f"maq: Produto {produto_encontrado['nome']} esgotado e removido do stock")
                print(f"maq: Saldo = {formatar_saldo(saldo)}")
            else:
                print(f'maq: Pode retirar o produto dispensado "{produto_encontrado["nome"]}"')
                print(f"maq: Saldo = {formatar_saldo(saldo)}")
        else:
            # Saldo insuficiente
            print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
            print(f"maq: Saldo = {formatar_saldo(saldo)}; Pedido = {formatar_saldo(preco_centimos)}")

    elif comando.upper().startswith("..."):
        print(f"maq: Saldo = {formatar_saldo(saldo)}")
            
    elif comando.upper() == "AJUDA" or comando.upper() == "HELP":
        print("maq: Comandos disponíveis:")
        print("maq: - LISTAR: Mostra todos os itens em stock")
        print("maq: - MOEDA <moedas> .: Adiciona moedas (ex: MOEDA 1e, 20c, 5c .)")
        print("maq: - SELECIONAR <código>: Seleciona um produto para comprar")
        print("maq: - SAIR: Encerra o programa")
        print("maq: - AJUDA/HELP: Mostra esta mensagem")
        print("maq: - ...: Mostra o saldo")

        
    elif comando == "":
        continue  # Ignora inputs vazios
        
    else:
        print(f"maq: Comando '{comando}' não reconhecido. Digite AJUDA para ver os comandos disponíveis.")










