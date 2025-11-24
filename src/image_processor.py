from PIL import Image, ImageDraw, ImageFont
import os
from .config import TEMPLATES_DIR, OUTPUT_DIR, IMAGE_CONFIG

class ImageGenerator:
    def __init__(self):
        self.config = IMAGE_CONFIG
        
    def load_template(self, template_name):
        """Carrega imagem template"""
        template_path = TEMPLATES_DIR / template_name
        if not template_path.exists():
            raise FileNotFoundError(f"Template não encontrado: {template_name}")
        return Image.open(template_path)
    
    def add_text_to_image(self, image, text, position, font_size, color):
        draw = ImageDraw.Draw(image)
        
        try:
            # Tenta fonte do sistema
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            try:
                # Fallback para fontes comuns
                font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", font_size)
            except:
                # Último fallback
                font = ImageFont.load_default()
                
        draw.text(position, text, fill=color, font=font)
        return image
    
    def generate_product_image(self, product_data, output_filename):
        """Gera imagem customizada para um produto"""
        try:
            # Carrega template
            template = self.load_template(product_data['imagem_template'])
            image = template.copy()
            
            # Adiciona textos
            image = self.add_text_to_image(
                image, 
                product_data['produto'], 
                self.config['positions']['produto'],
                self.config['font_sizes']['produto'],
                self.config['colors']['text']
            )
            
            image = self.add_text_to_image(
                image, 
                f"UF: {product_data['uf']}", 
                self.config['positions']['uf'],
                self.config['font_sizes']['uf'],
                self.config['colors']['text']
            )
            
            image = self.add_text_to_image(
                image, 
                f"Qtd: {product_data['quantidade']}", 
                self.config['positions']['quantidade'],
                self.config['font_sizes']['quantidade'],
                self.config['colors']['text']
            )
            
            image = self.add_text_to_image(
                image, 
                f"R$ {product_data['preco']:.2f}", 
                self.config['positions']['preco'],
                self.config['font_sizes']['preco'],
                self.config['colors']['highlight']
            )
            
            # Salva imagem
            output_path = OUTPUT_DIR / output_filename
            image.save(output_path, quality=95)
            return True, str(output_path)
            
        except Exception as e:
            return False, str(e)