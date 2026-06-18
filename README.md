# 🛒 Sistema de Compras e Pagamentos em Python

## 📖 Descrição

Este projeto consiste em um sistema simples de processamento de compras desenvolvido em Python. O programa permite ao usuário selecionar diferentes formas de pagamento, validar valores informados e gerar um resumo da transação realizada.

O sistema oferece suporte para pagamentos à vista, crédito e débito, simulando operações comuns encontradas em sistemas de vendas.

---

## 🚀 Funcionalidades

### ✅ Pagamento à Vista

* PIX
* Cartão

  * Débito
  * Crédito
* Dinheiro em espécie

### ✅ Pagamento no Crédito

* Cartão de Crédito

  * Parcelamento de 1 a 12 vezes
  * Aplicação automática de juros de 5%
* Boleto Bancário

### ✅ Pagamento no Débito

* Cartão de Débito
* Transferência Bancária

### ✅ Validações

* Impede valores menores ou iguais a zero.
* Valida respostas de confirmação (`s` ou `n`).
* Trata erros de entrada para números inteiros.

### ✅ Resumo da Compra

Ao final de cada operação é exibido:

* Forma de pagamento
* Valor da compra
* Status da transação

---

## 📂 Estrutura do Código

| Função               | Descrição                              |
| -------------------- | -------------------------------------- |
| `menu()`             | Exibe o menu principal.                |
| `ler_inteiro()`      | Lê e valida números inteiros.          |
| `ler_valor()`        | Lê e valida valores monetários.        |
| `ler_sn()`           | Valida respostas "s" ou "n".           |
| `resumo_pagamento()` | Exibe um resumo da operação realizada. |
| `avista()`           | Processa pagamentos à vista.           |
| `credito()`          | Processa pagamentos no crédito.        |
| `debito()`           | Processa pagamentos no débito.         |

---

## 💳 Regras de Negócio

### PIX

* Gera um QR Code fictício.
* Aguarda confirmação do pagamento.

### Cartão de Crédito

* Aplica juros de **5%** sobre o valor da compra.
* Permite parcelamento entre **1 e 12 parcelas**.

### Boleto Bancário

* Simula a geração de um boleto para pagamento posterior.

### Transferência Bancária

* Simula uma transferência com confirmação imediata.

---

## ▶️ Como Executar

### Pré-requisitos

* Python 3.x instalado

### Executando

```bash
python nome_do_arquivo.py
```

---

## 🖥️ Exemplo de Uso

```text
COMPRAS E SEUS DESCONTOS
====================
Tipo da Compra:
1- À vista
2- Crédito
3- Débito
4- Sair

Qual o tipo da compra? -> 2

1- Cartão de Crédito
2- Boleto Bancário

Qual será a forma de prosseguir? -> 1

VALOR A SER PROCESSADO(R$): 100

Em quantas parcelas deseja dividir? -> 5

Valor original da compra: 100.00 R$
Valor do juros aplicado: 5.00 R$
Valor das parcelas: 21.00 R$
Compra no valor de 105.00 R$ realizada com sucesso!!!
```

---

## ⚠️ Possíveis Melhorias

* Corrigir chamadas incorretas da função `ler_sn()`.
* Corrigir leitura da opção principal (`tipoDaCompra`).
* Utilizar laços de repetição para evitar encerramentos com `exit()`.
* Implementar persistência de dados em arquivo.
* Adicionar histórico de compras.
* Aplicar orientação a objetos (POO).
* Criar interface gráfica com Tkinter ou PyQt.

---

## 👨‍💻 Autor

Projeto desenvolvido para fins de estudo e prática de programação em Python, abordando:

* Estruturas condicionais
* Funções
* Validação de entrada
* Tratamento de exceções
* Simulação de sistemas de pagamento
