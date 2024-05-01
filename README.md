# Banco DIO - Simulador de Operações Bancárias

Este repositório contém um projeto de simulação de operações bancárias desenvolvido como parte do Bootcamp Vivo Python Backend. O projeto foi construído em Python e está organizado em 3 branches principais que representam diferentes etapas do desenvolvimento: `main`, `Desafio.V2` e `Desafio.V3`.

## Branches

### `main`

A branch `main` contém a versão inicial do simulador bancário. Nesta versão, o programa permite ao usuário realizar operações básicas como depositar, sacar, verificar o extrato e sair do programa. As operações são realizadas em um loop contínuo até que o usuário decida sair. Aqui estão algumas características:

- Interface de texto simples para interação com o usuário.
- Controle de saldo, limite de saques diários e registro de todas as operações em um extrato.
- Não há distinção entre diferentes usuários ou contas bancárias.

### `Desafio.V2`

A branch `Desafio.V2` evolui o projeto introduzindo conceitos de funçoes, modularização de código e funcionalidades mais complexas como a criação de usuários e contas. As principais adições incluem:

- Funções para criar novos usuários e contas bancárias.
- Listagem de todas as contas cadastradas.
- Depósito e saque agora são operações associadas a contas específicas.
- Melhoria na organização do código utilizando funções para cada operação específica.

### `Desafio.V3`

A branch `Desafio.V3` representa uma evolução significativa no projeto de simulação de operações bancárias, introduzindo recursos avançados de orientação a objetos, tratamento de exceções e uma maior profundidade nas funcionalidades bancárias. Aqui estão algumas das principais adições e melhorias implementadas:

#### Estrutura de Classes e Herança

- **Cliente e Pessoa Física:** Extensão da funcionalidade de clientes para suportar especificidades de pessoas físicas, incluindo nome, data de nascimento e CPF, além de um endereço já existente na classe base.
- **Conta e ContaCorrente:** Implementação de uma classe genérica `Conta` com operações básicas de depósito e saque, além de um histórico de transações. A `ContaCorrente` é uma especialização que adiciona regras específicas, como limite de saque e número máximo de saques diários.
- **Histórico:** Cada conta possui um histórico que armazena detalhes de todas as transações realizadas, incluindo tipo, valor e data.

#### Transações como Classes Abstratas

- **Transações Abstratas:** Uso do conceito de classes abstratas para definir um contrato para as transações, garantindo que todas as transações futuras implementem os métodos necessários, como `registrar`.
- **Operações de Saque e Depósito:** Implementadas como classes que estendem a classe abstrata `Transação`, permitindo uma separação clara entre a lógica de transação e as operações de conta específicas.

#### Interface de Usuário e Funcionalidades

- **Menu Interativo:** Uma interface de usuário baseada em texto que permite realizar operações como depósito, saque, exibição de extrato, criação de nova conta, listagem de contas e cadastro de novo usuário.
- **Gestão Avançada de Clientes e Contas:** Funções para filtrar clientes por CPF, recuperar contas de clientes específicos e realizar operações de transação diretamente nas contas dos clientes.
- **Exibição de Extrato:** Possibilidade de visualizar o extrato de transações de uma conta, incluindo detalhes como tipo de transação, valor e saldo atual.

#### Robustez e Manutenção do Código

- **Modularização e Clarezas:** Código organizado em funções claras e específicas para cada tipo de operação, facilitando a manutenção e futuras extensões do projeto.
- **Validações e Tratamento de Exceções:** Inclusão de verificações de validade para entradas de usuário e valores de transação, garantindo a robustez e a usabilidade do sistema.
