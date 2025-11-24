import os
from pathlib import Path

# Paths absolutos
BASE_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = BASE_DIR / "data" / "templates"
OUTPUT_DIR = BASE_DIR / "data" / "output"
INPUT_DIR = BASE_DIR / "data" / "input"

# Configurações de imagem
IMAGE_CONFIG = {
    'default_font': 'arial.ttf',
    'font_sizes': {
        'produto': 36,
        'uf': 24,
        'quantidade': 20,
        'preco': 28
    },
    'colors': {
        'text': (0, 0, 0),  # Preto
        'highlight': (255, 0, 0)  # Vermelho
    },
    'positions': {
        'produto': (50, 50),
        'uf': (50, 100),
        'quantidade': (50, 140),
        'preco': (50, 180)
    }
}