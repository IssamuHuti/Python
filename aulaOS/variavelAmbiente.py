import os

os.chdir('aulaOS')

# Acessar uma variável do sistema
usuario = os.environ.get("USERNAME") or os.environ.get("USER")
print("Usuário atual:", usuario)

os.environ["MEU_TOKEN"] = "123456" # Criar ou modificar uma variável (válido só durante a execução)
print("Token:", os.environ["MEU_TOKEN"])

# Acessar todas as variáveis disponíveis
for chave, valor in os.environ.items():
    print(f"{chave} = {valor}")

