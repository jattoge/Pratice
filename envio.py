import os
import requests

PASTA = "./Comunicacao"
URL = "http://DESKTOP-TOCB6V1:5000/upload"

files = []
handles = []

for nome_arquivo in os.listdir(PASTA):
    if nome_arquivo.lower().endswith(".txt"):
        if nome_arquivo == "Shhh.txt":
            continue
        caminho = os.path.join(PASTA, nome_arquivo)
        f = open(caminho, "rb")
        handles.append(f)
        files.append(("files", (nome_arquivo, f)))

resp = requests.post(URL, files=files)

for f in handles:
    f.close()

print("Status HTTP:", resp.status_code)
print("Resposta:", resp.text)
