# MCP server para Linux (Hello World)

Servidor MCP minimalista para Ubuntu usando [FastMCP](https://gofastmcp.com). Ele expõe uma ferramenta `hello` que devolve uma saudação e informa o host e a versão do sistema operacional.

## Inicialização rápida
1. Garanta o Python 3.10+ disponível. Caso seu sistema não tenha o módulo `venv`, instale-o (`sudo apt-get install python3-venv`) ou crie o ambiente com `python3 -m venv --without-pip venv && curl -sS https://bootstrap.pypa.io/get-pip.py | venv/bin/python`.
2. Crie e ative o ambiente virtual chamado `venv`:
   ```bash
   python3 -m venv venv
   # ative com:
   source venv/bin/activate   # ou: . venv/bin/activate
   ```
   (Executar `venv/bin/activate` direto dá “Permission denied” porque o script deve ser *sourced*.)
3. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```
4. Suba o servidor MCP (usa o runner do FastMCP):
   ```bash
   fastmcp run server.py
   ```
   Se preferir sem ativar a venv, rode pelo caminho completo:
   ```bash
   venv/bin/fastmcp run server.py
   ```
   O server expõe a tool `hello`, que responde com um "Hello" e detalhes do host Ubuntu.

## Arquivos sensíveis
- As credenciais do servidor estão em `passwords.json` e já estão no `.gitignore`; não versione esse arquivo.

## Estrutura
- `server.py`: implementação do servidor MCP com a ferramenta `hello`.
- `requirements.txt`: dependências mínimas (FastMCP v2).
- `.gitignore`: ignora `venv/` e `passwords.json`.
