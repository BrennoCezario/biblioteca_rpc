# Biblioteca RPC
 
Implementação de uma biblioteca RPC (Remote Procedure Call) usando apenas bibliotecas padrão do Python, permitindo chamar funções remotamente como se fossem locais. O sistema inclui descoberta e registro de serviços via Binder.

## Estrutura do projeto

biblioteca_rpc/
├── rpc/                      # Código da biblioteca
│   ├── rpc_binder.py         # Serviço de registro/descoberta
│   ├── rpc_server.py         # Implementação do servidor RPC
│   ├── rpc_client.py         # Cliente RPC básico
│   ├── rpc_stub_generator.py # Gerador de stubs
│   └── serializer.py         # Serialização/desserialização
│
├── interface/                # Interfaces de serviço
│   └── math_service.py       # Exemplo: serviço matemático
│
├── examples/                 # Exemplos de uso
│   ├── server_example.py     # Servidor de exemplo
│   └── client_example.py     # Cliente de exemplo
│
└── README.md                 # Este arquivo

## Como iniciar o Binder, Servidor e Cliente.

**1) Binder**

```sh
    python -m rpc.rpc_binder
```

**2) Servidor**

```sh
    python -m examples.server_example
```

**3) Cliente**

```sh
    python -m examples.client_example
```

## Como adicionar novos serviços à biblioteca

## Exemplos de execução