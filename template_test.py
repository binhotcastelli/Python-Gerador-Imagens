from PIL import Image, ImageDraw
import os

# Cria templates para cada produto
templates = [
    'template_camiseta.jpg',
    'template_caneca.jpg', 
    'template_bone.jpg'
]

for template_name in templates:
    # Cria imagem 800x600 com cor diferente para cada template
    colors = {
        'template_camiseta.jpg': (173, 216, 230),  # Azul claro
        'template_caneca.jpg': (255, 218, 185),    # Pêssego  
        'template_bone.jpg': (144, 238, 144)       # Verde claro
    }
    
    img = Image.new('RGB', (800, 600), color=colors[template_name])
    draw = ImageDraw.Draw(img)
    
    # Adiciona borda e área do título
    draw.rectangle([0, 0, 799, 599], outline=(100, 100, 100), width=3)
    draw.rectangle([0, 0, 800, 50], fill=(70, 130, 180), outline=(70, 130, 180))
    
    # Adiciona nome do template
    draw.text((20, 15), template_name.replace('.jpg', '').upper(), fill=(255, 255, 255))
    
    # Salva
    img.save(f'data/templates/{template_name}', quality=95)
    print(f"✅ Criado: {template_name}")

print("\n🎯 Todos os templates criados em data/templates/")