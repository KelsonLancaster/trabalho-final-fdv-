import click
from PIL import Image, UnidentifiedImageError
from rich.console import Console
from rich.panel import Panel
import os

# Inicializa o console do Rich (para textos coloridos)
console = Console()

@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.option('--output', '-o', default='output.jpg', help='Nome do arquivo de saída.')
def process_image(input_path, output):
    """
    Ferramenta CLI para converter imagens para Preto e Branco.
    Uso: python main.py CAMINHO_DA_IMAGEM [OPCOES]
    """
    # Funcionalidade Visual (Rich): Painel de abertura
    console.print(Panel(f"[bold blue]Iniciando processamento de:[/bold blue] {input_path}", title="Image CLI Tool"))

    try:
        # Funcionalidade de Manipulação (Pillow): Abrir a imagem
        with Image.open(input_path) as img:
            
            # Avisando o usuário
            console.print(f"[yellow]Convertendo para escala de cinza...[/yellow]")
            
            # Lógica: Converter para Grayscale (Modo 'L')
            grayscale_img = img.convert("L")
            
            # Salvar o resultado
            grayscale_img.save(output)
            
            # Sucesso (Rich)
            console.print(f"[bold green]✔ Sucesso![/bold green] Imagem salva como: [italic]{output}[/italic]")

    except UnidentifiedImageError:
        console.print("[bold red]✖ Erro:[/bold red] O arquivo fornecido não é uma imagem válida.")
    except Exception as e:
        console.print(f"[bold red]✖ Erro inesperado:[/bold red] {e}")

if __name__ == '__main__':
    process_image()