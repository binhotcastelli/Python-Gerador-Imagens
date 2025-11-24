from PIL import Image, ImageDraw

# Cria imagem template básica 800x600
img = Image.new('RGB', (800, 600), color=(240, 240, 240))
draw = ImageDraw.Draw(img)

# Adiciona borda e título
draw.rectangle([0, 0, 799, 599], outline=(200, 200, 200), width=2)
draw.rectangle([0, 0, 800, 40], fill=(70, 130, 180), outline=(70, 130, 180))

# Salva
img.save('data/templates/template_basico.jpg', quality=95)
print("✅ Template básico criado: data/templates/template_basico.jpg")