# MCP server para linux

Em um primeiro momento criação de um mcp server para esse servidor linux ubuntu com um hello world.

Usuário e senhas do servidor estão no arquivo passwords.json, não sincronizados com o github.

O mcp server deve ser conectado por http

Para subir localmente (HTTP em 0.0.0.0:8000):
```
source venv/bin/activate
fastmcp run server.py -t http --host 0.0.0.0 --port 8000
```
ou sem ativar:
```
venv/bin/fastmcp run server.py -t http --host 0.0.0.0 --port 8000
```

Recursos expostos:
- `resource://about/hello`: instruções da tool hello (text/plain).
- `resource://system/overview`: overview do host e Python (application/json).

## Instruções para o python

Crie uma venv, chamada venv
Utilize a library fast mcp para o projeto
Crie o requirements.txt

mencione essa incialização e instruções no readme.md
