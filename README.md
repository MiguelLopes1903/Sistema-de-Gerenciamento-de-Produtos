# 📦 Sistema de Gerenciamento de Produtos

Aplicação web desenvolvida em **Python + Flask** para gerenciamento de produtos e estoque de uma loja de roupas (**ISP Clothes**). O projeto reúne duas frentes:

1. **CRUD funcional** de itens (nome e quantidade) com banco de dados SQLite.
2. **Interface do painel administrativo** (Início, Produtos, Financeiro e Pedidos) com formulário de cadastro de produto e upload de imagem.

---

## ✨ Funcionalidades

### CRUD de itens (`app/app.py`)
- ✅ **Listar** itens cadastrados em uma tabela
- ✅ **Adicionar** novo item (nome e quantidade)
- ✅ **Editar** item existente
- ✅ **Excluir** item, com confirmação antes de deletar
- 💾 Persistência em banco **SQLite** via SQLAlchemy

### Painel administrativo (`templates/` e `static/`)
- 🏠 **Início** – página inicial com menu de navegação
- 🛍️ **Produtos** – formulário de cadastro com:
  - upload de imagem com pré-visualização (JavaScript)
  - nome, time, estoque, data, SKU, preço, material, marca e descrições
- 💰 **Financeiro** – página em construção
- 📋 **Pedidos** – tabela de pedidos com nome do cliente, nº do pedido, data, valor, forma de pagamento, status e detalhes
- 🖼️ Validação de extensões de imagem no upload (`png`, `jpg`, `jpeg`, `gif`)

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.12 |
| Framework web | Flask 3.1 |
| ORM | Flask-SQLAlchemy 3.1 / SQLAlchemy 2.0 |
| Banco de dados | SQLite |
| Front-end | HTML5, CSS3, JavaScript |
| Templates | Jinja2 |

---

## 📁 Estrutura do projeto

```
Sistema-de-Gerenciamento-de-Produtos/
├── app/
│   ├── app.py            # Aplicação Flask com o CRUD (ponto de entrada)
│   ├── viwes.py          # Rotas do painel (Início, Produtos, Financeiro, Pedidos)
│   ├── connect.py        # Conexão com PostgreSQL (psycopg2) – uso futuro
│   ├── requests.py       # Script de teste de requisições HTTP
│   ├── main.py           # Inicialização alternativa
│   ├── model.py          # Reservado para os modelos
│   ├── instance/
│   │   └── projeto.db    # Banco SQLite
│   └── templates/
│       ├── adicao.html   # Listagem + formulário de criação
│       └── edit.html     # Formulário de edição
├── templates/            # Páginas do painel
│   ├── inicio.html
│   ├── produtos.html
│   ├── financeiro.html
│   └── pedidos.html
└── static/               # CSS e JavaScript do painel
    ├── inicio.css
    ├── produtos.css
    ├── produtos.js
    ├── financeiro.css
    └── pedidos.css
```

---

## 🚀 Como executar

### Pré-requisitos
- [Python 3.10+](https://www.python.org/downloads/)
- `pip`

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/<seu-usuario>/Sistema-de-Gerenciamento-de-Produtos.git
cd Sistema-de-Gerenciamento-de-Produtos

# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

# 3. Instale as dependências
pip install flask flask-sqlalchemy

# 4. Execute a aplicação
python app/app.py
```

Acesse no navegador: **http://127.0.0.1:8000**

> O banco SQLite e a tabela são criados automaticamente na primeira execução.

---

## 🔗 Rotas do CRUD

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Lista os itens e exibe o formulário de criação |
| `POST` | `/create` | Cria um novo item |
| `GET` | `/edit/<id>` | Exibe o formulário de edição |
| `POST` | `/update/<id>` | Atualiza um item |
| `POST` | `/delete/<id>` | Remove um item |

## 🔗 Rotas do painel

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` ou `/inicio` | Página inicial |
| `GET`, `POST` | `/Produtos` | Cadastro de produto e upload de imagem |
| `GET` | `/Financeiro` | Página financeira |
| `GET` | `/Pedidos` | Lista de pedidos |

---

## 🗄️ Modelo de dados

**Tabela `user`**

| Campo | Tipo | Restrições |
|---|---|---|
| `id` | Integer | Chave primária |
| `name` | String(80) | Obrigatório |
| `quantidade` | String(10) | Obrigatório |

---

## 🚧 Status e próximos passos

O projeto está **em desenvolvimento**. Melhorias previstas:

- [ ] Integrar o painel (Início, Produtos, Financeiro, Pedidos) ao CRUD em uma única aplicação
- [ ] Criar a rota `/cadastrar` e salvar os dados completos do produto no banco
- [ ] Renomear a tabela `user` para `produto` e usar tipo numérico em `quantidade`
- [ ] Concluir a página Financeiro e popular a tabela de Pedidos com dados do banco
- [ ] Migrar para PostgreSQL (`connect.py`), usando variáveis de ambiente para as credenciais
- [ ] Adicionar autenticação (Flask-JWT-Extended)
- [ ] Criar o arquivo `requirements.txt` e o `.gitignore`

---
