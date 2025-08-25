import os

def loading_config(file_name: str) -> dict:
   
    path = f"{file_name}.txt"

    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo {path} não encontrado no diretório atual.")

    variaveis = {}

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
         line = line.strip()
        if not line or line.startswith("#"):  # ignora linhas vazias e comentários
            continue
            if "=" in line:
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"')  # remove aspas
                variaveis[key] = value

    return variaveis


# Example:
if __name__ == "__main__":
    config = loading_config("config")  # read "config.txt"
    print(config)
    # Access as variables:
    print("Token:", config.get("token"))
    print("Type :", config.get("type"))