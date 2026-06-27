# 🐸 Ouvidoria Sapinho

Sistema de ouvidoria desenvolvido como projeto acadêmico na **Unifacisa**,
com o objetivo de facilitar o registro, acompanhamento e resolução de
manifestações da comunidade acadêmica de forma simples e organizada.

---

## 👥 Integrantes

| Nome                           |
|--------------------------------|
| Kevin Macedo Gonçalves         |
| Ariberto Andrade da Silva      |
| Hymura Natsuki Rodrigues Sousa |
| Rafael Henrique                |
| Nicolas dos Santos             |

---

## 🎯 Funcionalidades

- ✅ Inserir comentários por categoria (Sugestão, Reclamação ou Elogio)
- 🔢 Contar o total de manifestações registradas
- 📋 Listar todos os comentários cadastrados
- 🔍 Pesquisar manifestação pelo código
- 🗂️ Pesquisar manifestações por categoria
- ✏️ Atualizar uma mensagem existente pelo código
- 🗑️ Excluir uma mensagem pelo código

---

## 🛠️ Tecnologias utilizadas

- **Python 3.x**
- **MySQL** (banco de dados relacional)
- **mysql-connector-python** (biblioteca de conexão)

---

## 📁 Estrutura do projeto

```
ouvidoria-sapinho/
│
├── main.py          # Menu principal e loop de interação com o usuário
├── ouvidoria.py     # Funções de negócio (inserir, listar, pesquisar etc.)
└── operacoesbd.py   # Funções de acesso ao banco de dados (CRUD genérico)
```

---

## ⚙️ Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado:

- [Python 3.8+](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/mysql/)
- A biblioteca `mysql-connector-python`:

```bash
pip install mysql-connector-python
```

---

## 🗄️ Configuração do banco de dados

1. Abra o MySQL e crie o banco de dados e a tabela:

```sql
CREATE DATABASE esquema;

USE esquema;

CREATE TABLE ouvidoria (
    codigo     INT AUTO_INCREMENT PRIMARY KEY,
    categoria  VARCHAR(20)  NOT NULL,
    titulo     VARCHAR(100) NOT NULL,
    comentario TEXT         NOT NULL
);
```

2. Certifique-se de que o usuário e a senha conferem com o arquivo `main.py`:

```python
conexao = criarConexao("localhost", "root", "1664", "esquema")
#                       ^host        ^user   ^senha  ^banco
```

> Se suas credenciais do MySQL forem diferentes, edite essa linha antes de rodar.

---

## ▶️ Como executar

1. Clone ou baixe o repositório:

```bash
git clone https://github.com/seu-usuario/ouvidoria-sapinho.git
cd ouvidoria-sapinho
```

2. Garanta que o MySQL está rodando e o banco está criado (veja seção acima).

3. Execute o programa:

```bash
python main.py
```

---

## 🖥️ Como usar o programa

Ao iniciar, o menu principal será exibido:

```
OUVIDORIA!
1) Inserir
2) Quantidade de Comentário
3) Listar
4) Pesquisar com código
5) Pesquisar por Categoria
6) Atualizar com Código
7) Excluir pelo Código
8) Sair
Digite a opção desejada:
```

### Opção 1 — Inserir comentário

Escolha a categoria e preencha o título e o texto da mensagem:

```
1- Sugestão
2- Reclamação
3- Elogio
Escolha a categoria desejada: 1
Digite o titulo do assunto:
Melhorar o laboratório de informática
Digite seu comentário:
Seria ótimo ter mais computadores disponíveis.
Comentário adicionado com sucesso nº: 1
```

### Opção 2 — Quantidade de comentários

Exibe o total de manifestações cadastradas no sistema.

```
3 - Mensagem(s) disponível(is)
```

### Opção 3 — Listar todos os comentários

Mostra todos os registros armazenados:

```
Mensagens registradas na Ouvidoria
- Código: 1  Categoria: Sugestão
  Assunto: Melhorar o laboratório
  Comentario: Seria ótimo ter mais computadores.
```

### Opção 4 — Pesquisar pelo código

Informe o número do código para buscar uma manifestação específica:

```
Digite o código da mensagem: 1
Mensagem encontrada
Categoria: Sugestão
Assunto: Melhorar o laboratório
Mensagem: Seria ótimo ter mais computadores.
```

### Opção 5 — Pesquisar por categoria

Filtra os comentários por tipo:

```
1- Sugestão
2- Reclamação
3- Elogio
Escolha a categoria de pesquisa desejada: 2
```

### Opção 6 — Atualizar pelo código

Permite editar o texto de uma mensagem já registrada:

```
Digite o código mensagem: 1
Digite a nova mensagem:
Precisamos de mais cadeiras também.
Comentário registrado com sucesso!
```

### Opção 7 — Excluir pelo código

Remove permanentemente uma manifestação:

```
Digite o código da mensagem: 1
Comentário excluído com sucesso!
```

### Opção 8 — Sair

Encerra a conexão com o banco de dados e fecha o programa:

```
Obrigado por usar o app!
```

---

## 📄 Licença

Este projeto é de uso acadêmico e foi desenvolvido para fins educacionais na Unifacisa.


