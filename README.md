# 🚀 Sistema de Login e Cadastro - Marcus Tech

Este é um sistema de autenticação (Cadastro e Login) desenvolvido em **Python** e integrado com banco de dados **SQL (SQLite3)**. 

O foco principal deste projeto foi ir além do básico: construí um código organizado, seguro e que resolve problemas reais de armazenamento de dados de forma inteligente.

---

## 🧠 O que foi estudado e aplicado? (De forma simples)

Diferente de sistemas comuns que misturam tudo, este software foi planejado em blocos, pensando na segurança e na experiência de quem está usando:

*   **Banco de Dados Inteligente (SQL):** O programa gerencia tudo sozinho. Logo de início, ele checa se o banco de dados existe; se não existir, ele cria na hora. Você pode rodar o programa quantas vezes quiser que ele nunca vai dar erro ou apagar o que já foi feito.
*   **Zero Dados Duplicados (Chave Primária):** Defini o CPF como a **Chave Primária** (`PRIMARY KEY`). Na programação, isso significa que o banco de dados funciona como um "leão de chácara": ele garante que nenhum usuário consiga se cadastrar com um CPF que já pertence a outra pessoa. Usei a própria inteligência do SQL para proteger o sistema.
*   **Código Organizado e Sem Bagunça (Funções e Return):** Em vez de deixar o código solto e confuso, dividi cada ação em "caixinhas" chamadas funções (`nomeação_cpf`, `nomeação_senha`, etc.). Usei o comando `return`, que funciona como um mensageiro: ele pega o dado digitado dentro da função, leva para fora com segurança e entrega direto nas colunas certas do banco de dados.
*   **Pensado na Experiência do Usuário (Validação em Tempo Real):** O sistema é inteligente no diálogo. Quando a pessoa vai se cadastrar, o programa faz uma busca no banco de dados logo após o CPF ser digitado. Se o CPF já existir, ele avisa na hora. Assim, o usuário não perde tempo preenchendo o nome e a senha para só descobrir o erro no final.
*   **Fluxo de Cima para Baixo (Modo Silencioso):** O código foi montado de forma que o banco de dados e as ferramentas fiquem guardados no topo do arquivo (em "off"), fazendo com que o terminal inicie limpo, mostrando direto a pergunta principal para o usuário.

---

## 🛠️ Tecnologias Utilizadas

*   **Python 3** (Controle das perguntas, conversas e lógica do sistema)
*   **SQLite3** (O banco de dados que guarda todas as contas com segurança)
