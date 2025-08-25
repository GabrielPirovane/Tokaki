# Tokaki
Tokaki é uma plataforma que conecta o músico com o contratante. 

# OBS: ESSA É A BRANCH MAIN. NÃO DÊ MERGE DE SUA BRANCH SEM FALAR COM AS OUTRAS PESSOAS DO GRUPO

# Como rodar o site para testes:
_**(Opcional, mas recomendado) Antes de começar, baixar a extensão "Python Enviroments" e, logo após,  criar um ambiente python com:**_ ``` python -m venv .venv```
1. Executar git clone com o link deste repositório;
2. Configurar o git no computador com:
```
git config --global user.name "Fulano de Tal"
git config --global user.email fulanodetal@exemplo.br
```
3. Executar ```git checkout (seu nome)``` no terminal;
4. Verificar com ```git branch``` se a branch selecionada é aquela com o seu nome;
5. Executar no terminal: ```pip install -r .\requirements.txt```
6. Executar main.py com FastAPI (verificar se .vscode/launch.json está conforme código abaixo):
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: FastAPI",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "main:app",
                "--reload"
            ],
            "jinja": true
        }
    ]
}
```
7. Inserir ufs e cidades no banco de dados com o comando ``` python -m inserts.insert_cidades_ufs ```

# Telas e rotas: 

Link para mapa de telas: https://www.gloomaps.com/XKWlAlTm3G  
Link para o protótipo de interface: https://www.canva.com/design/DAGmtF6l3IY/AZC2mX-GrKfBh9qfN4qIow/edit  
Rotas com ✅: funcionais, mas front-end e back-end em desenvolvimento;  
Rotas com ✅ em negrito: prontas e totalmente funcionais;

**Rotas públicas**
- [x] Home pública (/);
- [x] Login (/login);
- [x] Esqueci a senha (/esqueci-senha);
- [x] **Cadastro (/cadastro);**
- [x] Verificação de email (/verificacao);
- [x] Sobre (/sobre);
- [x] Contatos (/contatos);
- [x] Catálogo de músicos (/catalogo);
- [x] Detalhes de um músico (/detalhes);
- [x] Galeria (/galeria);
- [x] Foto (/foto);





