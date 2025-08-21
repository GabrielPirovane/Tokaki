# Tokaki
Tokaki é uma plataforma que conecta o músico com o contratante. 

# OBS: ESSA É A BRANCH MAIN. NÃO DÊ MERGE DE SUA BRANCH SEM FALAR COM AS OUTRAS PESSOAS DO GRUPO

# Como rodar o site para testes:
_**(Opcional, mas recomendado) Antes de começar, baixar a extensão "Python Enviroments" e, logo após,  criar um ambiente python com:**_ ``` python -m venv .venv```
1 - Executar git clone com o link deste repositório;
2 - Configurar o git no computador com:
```
git config --global user.name "Fulano de Tal"
git config --global user.email fulanodetal@exemplo.br
```
4 - Executar ```git checkout (seu nome)``` no terminal;
5- Verificar com ```git branch``` se a branch selecionada é aquela com o seu nome;
6 - Executar no terminal: ```pip install -r .\requirements.txt```
7 - Executar main.py com FastAPI (verificar se .vscode/launch.json está conforme código abaixo):
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
8 - Inserir ufs e cidades no banco de dados com o comando ``` python -m inserts.insert_cidades_ufs ```

# Telas e rotas: 

Link para mapa de telas: https://www.gloomaps.com/XKWlAlTm3G

Público
- [x] Home pública (/);
- [x] Login (/login);
- [x] Esqueci a senha (/esqueci-senha);
- [x] Cadastro (/cadastro);
- [x] Verificação de email (/verificacao);
- [x] Sobre (/sobre);
- [x] Contatos (/contatos);
- [x] Catálogo de músicos (/catalogo);
- [x] Detalhes de um músico (/detalhes);
- [x] Galeria (/galeria);
- [x] Foto (/foto);

Usuário (prefixo é o nome do usuário. Necessário estar logado)

- [x] Home usuário (nav footer usuário) (/);
- [x] Perfil (/perfil/visualizar);
- [x] Alterar dados (/perfil/alterar-dados);
- [x] Alterar senha (/perfil/alterar-senha);
- [x] _Sair (/sair);_
- [x] Conversas (/conversas);
- [x] Detalhes conversas (/conversas/detalhes);
- [] Encerrar conta ;
- [] Solicitar contratação.

Músico(prefixo é o nome do usuário + /musico. Necessário estar logado numa conta do tipo músico)

- [] Home músico;
- [] Agenda;
- [] Alterar disponibilidade;
- [] Galeria de fotos;
- [] Detalhes da galeria;
- [] Ampliar foto;
- [] Сadastrar foto;
- [] Alterar foto;
- [] Excluir galeria;
- [] Cadastrar galeria;
- [] Alterar galeria;
- [] Minhas contratações;
- [] Solicitações de contratação;
- [] Gerenciar solicitação;
- [] Categorias;
- [] Atribuir categorias;
- [] Remover categorias.

Contratante (prefixo é o nome de usuário. Necessário estar logado numa conta padrão ou músico)

- [] Home contratante;
- [] Minhas contratações;
- [] Solicitações de contratação;
- [] Cancelar solicitação;
- [] Detalhes de solicitação;
- [] Cancelar solicitação;

Admin
- [x] Home admin (/admin);
- [x] Ver administradores (/admin/administradores);
- [x] Inserir administrador (/admin/administradores/inserir);
- [x] Excluir administrador (/admin/administradores/excluir);
- [] Alterar administrador (/admin/administradores/alterar);
- [x] Ver categorias (/admin/categorias);
- [x] Inserir categoria (/admin/categorias/inserir);
- [x] Alterar categoria (/admin/categorias/alterar);
- [x] Excluir categoria (/admin/categorias/excluir);
- [x] Ver fotos (/admin/fotos);
- [] Moderar foto (/admin/fotos/moderar);




