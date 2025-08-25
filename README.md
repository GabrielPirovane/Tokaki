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
- [x] **Login (/login)**;
- [x] Esqueci a senha (/esqueci-senha);
- [x] **Cadastro (/cadastro);**
- [x] Verificação de email (/verificacao);
- [x] Sobre (/sobre);
- [x] Contatos (/contatos);
- [x] Catálogo de músicos (/catalogo);
- [x] Detalhes de um músico (/detalhes);
- [x] Galeria (/galeria);
- [x] Foto (/foto);

**Rotas comuns para todos os tipos de usuário (o prefixo da url é o nome de usuário. Portanto, é necessário estar logado)**  
100%

- [x] Home usuário (nav footer usuário) (/); 
- [x] Perfil (/perfil); 
- [x] Alterar dados (/perfil/alterar-dados); 
- [x] Alterar senha (/perfil/alterar-senha); 
- [x] Encerrar conta (/perfil/encerrar-conta); 
- [x] _Sair (/sair);_
- [x] Conversas (/conversas);
- [x] Detalhes conversas (/conversas/detalhes);
- [x] Solicitar contratação (/contratacao).

**Rotas únicas para o usuário do tipo músico(prefixo é o nome do usuário). Necessário estar logado numa conta do tipo músico)**

- [x] Home músico (/);
- [x] Agenda (/agenda);
- [x] Alterar disponibilidade (/agenda/disponibilidade);
- [x] Galeria de fotos (/galeria);
- [x] Detalhes da galeria (/galeria/detalhes);
- [x] Cadastrar galeria (/galeria/cadastrar);
- [x] Alterar galeria (/galeria/alterar);
- [x] Excluir galeria (/galeria/excluir);
- [x] Ampliar foto (/galeria/foto);
- [x] Сadastrar foto (/galeria/foto/upload);
- [x] Alterar foto (/galeria/foto/alterar);
- [x] Minhas contratações (/contratacoes);
- [x] Solicitações de contratação (/contratacoes/solicitacoes);
- [x] Gerenciar solicitação (/contratacoes/solicitacoes);
- [x] Categorias (/categorias);
- [x] Atribuir categorias (/categorias/atribuir);
- [x] Remover categorias (/categorias/remover).

**Rotas Contratante (prefixo é o nome de usuário. Necessário estar logado numa conta padrão ou músico)**

- [x] Home contratante (/);
- [x] Minhas contratações (/minhas-contratacoes);
- [x] Solicitações de contratação (/minhas-contratacoes/solicitacoes);
- [x] Cancelar solicitação (/minhas-contratacoes/solicitacoes/cancelar);
- [x] Detalhes de solicitação (/minhas-contratacoes/solicitacoes/detalhes);
- [x] Realizar pagamento (/pagamento);

**Rotas de administração, exclusivas para staff**
- [x] **Home admin (/admin);**
- [x] **Ver administradores (/admin/administradores);**
- [x] **Inserir administrador (/admin/administradores/inserir);**
- [x] **Excluir administrador (/admin/administradores/excluir);**
- [] ~~Alterar administrador (/admin/administradores/alterar)~~;
- [x] **Ver categorias (/admin/categorias);**
- [x] **Inserir categoria (/admin/categorias/inserir);**
- [x] **Alterar categoria (/admin/categorias/alterar);**
- [x] **Excluir categoria (/admin/categorias/excluir);**
- [x] Ver fotos (/admin/fotos);
- [x] Moderar foto (/admin/fotos/moderar);




