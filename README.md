# Sistema de Login e Registro com Flask

## 📌 Sobre o Projeto

Este é um sistema simples de autenticação desenvolvido com Flask e SQLite. O projeto permite que usuários criem contas e realizem login de forma segura utilizando criptografia de senhas.

## 🚀 Funcionalidades

* Cadastro de usuários
* Login de usuários
* Armazenamento de dados em SQLite
* Criptografia de senhas com Werkzeug
* Interface moderna e responsiva
* Validação de autenticação

## 🛠️ Tecnologias Utilizadas

* Python
* Flask
* SQLite3
* HTML5
* CSS3
* JavaScript
* Werkzeug Security

## 📂 Estrutura do Projeto

```
projeto/
│
├── app.py
├── dev.db
│
├── templates/
│   ├── login.html
│   └── registro.html
│
└── README.md
```

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Entre na pasta:

```bash
cd seu-repositorio
```

Instale as dependências:

```bash
pip install flask werkzeug
```

Execute o projeto:

```bash
python app.py
```

Acesse:

```
http://127.0.0.1:5000
```

## 🔒 Segurança

As senhas não são armazenadas em texto puro. O sistema utiliza hash de senha através do Werkzeug Security para proteger os dados dos usuários.

## 📈 Melhorias Futuras

* Área logada após autenticação
* Sistema de logout
* Recuperação de senha
* Perfil de usuário
* Painel administrativo
* Integração com banco de dados PostgreSQL

## 👨‍💻 Autor

Desenvolvido por Matheus Dev.
