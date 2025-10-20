# TP4 - Máquina de Vending

Feito por:
  
  <img width="180" height="180" alt="image" src="https://github.com/user-attachments/assets/37338582-83b4-4b7d-933b-ecc82cbd9d91" />
  
  **Nelson Sousa - A109068**


## Objetivo

O objetivo principal do código da máquina de vending (máquina de vendas automáticas) é **simular o funcionamento de uma máquina de vending** real, permitindo:

### Aos Utilizadores:

<ol>
  <li>Comprar Produtos - Selecionar e comprar itens presentes na máquina.</li>
  <li>Gerir Saldo Atual - Inserir moedas e receber o troco.</li>
  <li>Ver Stock Atual da Máquina - Visualizar os produtos atuais da máquina.</li>
</ol>

### Ao Sistema:

<ol>
  <li>Gestão de Stock - Verificar e remover produtos esgotados do stock da máquina.</li>
  <li>Processamento de Pagamentos - Validar moedas e calcular o troco.</li>
  <li>Persistência de Dados - Guardar alterações no ficheiro JSON.</li>
</ol>

## Funcionalidades Específicas:

<ol>
  <li>Autenticação de moedas - Só aceita moedas válidas (1c-500e)</li>
  <li>Cálculo inteligente de troco - Devolve a combinação ótima de moedas</li>
  <li>Gestão automática de stock - Remove produtos quando esgotam</li>
  <li>Interface de comandos - Sistema interativo tipo terminal</li>
  <li>Validação de saldo - Impede compras sem fundos suficientes</li>
</ol>

## Resolução

Para a resolução deste problema foram criados dois códigos, um para simular o [utilizador](maquina.py) e outro para simular um [administrador da máquina](admin.py).

### Código do Utilizador (`maquina.py`)

 Funcionalidades Principais:
<ol>
<li>
  
  **COMPRAS**: Sistema completo de seleção e compra de produtos através do comando `SELECIONAR`</li>


<li> 
  
  **GESTÃO DE MOEDAS**: 
  
  - Comando `MOEDA` para inserir moedas válidas (1c, 2c, 5c, 10c, 20c, 50c, 1e, 2e, 5e, 10e, 20e, 50e, 100e, 200e, 500e)
  
  - Cálculo automático de saldo e conversão para formato legível (ex: "1e30c")</li>
<li> 
  
  **CONSULTA**: Comando `LISTAR` para visualizar todos os produtos em formato de tabela organizada</li>
<li>
  
  **SISTEMA DE TROCO**: Ao usar `SAIR`, calcula e devolve o troco na combinação ótima de moedas</li>
<li>
  
  **GESTÃO AUTOMÁTICA**: Remove automaticamente produtos quando o stock chega a zero</li>
<li>
  
  **AJUDA**: Comando `AJUDA` ou `HELP` para listar todos os comandos disponíveis</li>
<li> 
  
  **SALDO**: Comando `...` para verificar o saldo atual rapidamente</li>
</ol>


 Características Técnicas:
<ol>
<li> 
  
  **Persistência de dados**: Atualiza automaticamente o ficheiro `stock.json` ao sair</li>
<li> 
  
  **Validação rigorosa**: Verifica stock, saldo suficiente e formato dos comandos</li>
<li> 
  
  **Interface intuitiva**: Mensagens claras com prefixo "maq:" para identificação</li>
<li> 
  
  **Processamento em tempo real**: Atualização imediata do stock após cada compra</li>
</ol>

### Código do Administrador (`admin.py`)

 Funcionalidades de Gestão:
<ol>
<li>
  
  **ADIÇÃO INTELIGENTE**: Comando `ADICIONAR` que:
  
  - Adiciona novo produto se o código não existir
  
  - Aumenta stock automaticamente se o produto já existir</li>
<li>
  
  **REMOÇÃO FLEXÍVEL**: Comando `REMOVER` que permite:
  
  - Remover unidades específicas de um produto
  
  - Remove completamente o produto apenas quando o stock chega a zero (com confirmação)</li>
<li>
  
  **VISUALIZAÇÃO**: Comando `LISTAR` para monitorizar stock completo em formato de tabela</li>
<li>
  
  **GESTÃO SEGURA**: Comando `SAIR` guarda automaticamente todas as alterações no ficheiro</li>
</ol>

Características Avançadas:
<ol>
<li>
  
  **Validação de dados**: Verifica entradas numéricas e evita valores negativos</li>
<li>
  
  **Prevenção de erros**: Confirmação para operações destrutivas</li>
<li>
  
  **Interface consistente**: Usa o mesmo estilo iterativo com prompt `admin>>`</li>
<li>
  
  **Gestão eficiente**: Não permite stock negativo e mantém integridade dos dados</li>
</ol>

###  Integração entre Sistemas

 Ficheiro Partilhado (`stock.json`):
<ol>
<li>
  
  Formato estruturado: `[{"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7}]`</li>
<li> Suporte a caracteres especiais (encoding UTF-8)</li>
<li> Atualizações em tempo real entre ambos os sistemas</li>
</ol>

### Fluxo de Trabalho:

<ol>
<li> 
  
  **Administrador** carrega stock inicial através de `admin.py`</li>
<li> 
  
  **Utilizadores** fazem compras através de `maquina.py`</li>
<li> 
  
  **Stock** é automaticamente atualizado e produtos esgotados são removidos</li>
<li> 
  
  **Administrador** monitoriza e reabastece através de `admin.py`</li>
</ol>

### Medidas de Segurança e Robustez
<ol>
<li>
  
  **Validação de moedas**: Apenas aceita valores monetários pré-definidos</li>
<li>
  
  **Controlo de stock**: Impede vendas sem stock disponível</li>
<li>
  
  **Verificação de saldo**: Bloqueia compras sem fundos suficientes</li>
<li>
  
  **Formatação de comandos**: Exige sintaxe correta (ex: `MOEDA ... .`)</li>
<li>
  
  **Gestão de erros**: Mensagens informativas para situações inválidas</li>
</ol>

Este sistema dual permite uma **gestão completa do ciclo de vida** dos produtos, desde o reabastecimento pelo administrador até à venda final ao utilizador, mantendo a integridade dos dados em todos os momentos.

## Testes

Para efeitos de teste dos códigos desenvolvidos, anexam-se várias capturas de ecrã que documentam a execução dos programas em ambiente de linha de comandos.

<ol>
  <li>

  **Testes do Utilizador** - [Teste de Funcionalidades](output1.png) e [Teste de Armazenamento de Informação em stock.JSON](output2.png)
    
  </li>

  <li>

  **Testes do Administrador** - [Interface e Testes de Adicionar Produtos no Stock](output3.png) e [Teste de Remoção Parcial e Remoção Total de Produtos do Stock](output4.png)
  </li>
</ol>
