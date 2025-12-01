# 📸 Image CLI Tool

Ferramenta de linha de comando (CLI) para processamento de imagens, desenvolvida para a disciplina de FDV.
O software recebe uma imagem colorida e a converte para escala de cinza (Preto e Branco), utilizando container Docker para portabilidade total.

## 👥 Grupo
- **Kelson Lancaster**
- Geraldez Santos
- [Gilmara Maria]

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.11
- **Gerenciador de Dependências:** PDM
- **Bibliotecas:** Click (CLI), Pillow (Processamento), Rich (Interface)
- **Container:** Docker & GitHub Container Registry (GHCR)

## 🚀 Como Executar (Sem instalar nada)

A imagem Docker já está pública. Você não precisa clonar o código nem instalar Python.
Basta ter o Docker instalado e rodar o comando abaixo na pasta onde está sua foto.

### 🪟 No Windows (PowerShell):
```powershell
docker run --rm -v "${PWD}:/app/data" ghcr.io/kelsonlancaster/image-cli-tool:latest /app/data/SUA_FOTO.jpg -o /app/data/resultado.jpg