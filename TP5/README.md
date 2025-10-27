# TP5 - Análise Léxica e Sintática de Expressões Aritméticas

Feito por:
  
  <img width="180" height="180" alt="image" src="https://github.com/user-attachments/assets/37338582-83b4-4b7d-933b-ecc82cbd9d91" />
  
  **Nelson Sousa - A109068**

## Objetivo do Trabalho

O objetivo deste trabalho é implementar um **analisador léxico** e **analisador sintático** para expressões aritméticas simples. O sistema é capaz de reconhecer e validar expressões matemáticas contendo números inteiros, operadores básicos (+, -, *, /) e parênteses, verificando se seguem a estrutura gramatical correta.

## Implementação

- Sistema completo com 3 ficheiros interligados

- Reconhece: números inteiros, operadores (+, -, *, /) e parênteses

- Valida se a expressão segue as regras gramaticais corretas

- Deteta erros tanto de caracteres inválidos como de estrutura

### Explicação por Códigos
<ol>
<li>
  
  **[Analisador Léxico](analisador_lex.py)**
  
  Função principal: Transformar o texto de entrada em tokens (unidades básicas)

  O que faz:

  - Lê caracter por caracter da expressão matemática

  - Agrupa caracteres para formar "tokens" reconhecíveis

  - Identifica e classifica cada elemento:
  
        INT → números (ex: 123)

        SUM → sinal de mais (+)

        DIF → sinal de menos (-)

        MUL → sinal de multiplicação (*)

        DIV → sinal de divisão (/)

        P_OP → parêntese de abertura "("

        P_CLS → parêntese de fechamento ")"

  - Ignora espaços em branco e tabs

  - Deteta e reporta caracteres inválidos</li>

<li> 
  
  **[Analisador Sintático](analisador_sin.py)**
  
  Função principal: Verificar se a sequência de tokens forma uma expressão válida

  O que faz:

  - Recebe os tokens do analisador léxico

  - Verifica se seguem a "gramática" das expressões matemáticas

  - Regras gramaticais implementadas:

        Expressão (E) → Termo (T) seguido de zero ou mais [operador + Termo]

        Termo (T) → pode ser um número OU uma expressão entre parênteses

        Operador (op) → +, -, *, /

  - Usa recursão para lidar com parênteses

  - Mostra o passo-a-passo do reconhecimento

  - Deteta e reporta erros de estrutura (ex: parênteses desbalanceados)</li>

<li>
  
  **[Interface com Utilizador](conta.py)**
  
  Função principal: Ser o ponto de entrada do programa

  O que faz:

  - Pede ao utilizador para inserir uma expressão matemática

  - Inicia todo o processo de análise

  - Chama os outros módulos na ordem correta</li>

</ol>

### **Fluxo de Execução**
<ol>
<li>Utilizador insere expressão → conta.py</li>

<li>Texto é convertido em tokens → analisador_lex.py</li>

<li>Tokens são validados estruturalmente → analisador_sin.py</li>

<li>Resultado é mostrado: sucesso ou erro identificado</li>
</ol>

### **Exemplos**

- **[Expressões Aritméticas Simples](contas_basicas.png)** - Expressões com apenas um operador.
- **[Expressões Aritméticas](contas.png)** - Expressões com dois ou mais operadores.
- **[Expressões Aritméticas Com Erros Sintáticos](contas_com_erros.png)** - Expressões com erros de sintaxe.
