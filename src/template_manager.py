# template_manager.py (OPCIONAL - pode deletar)
class TemplateManager:
    def validate_template(self, template_path):
        """Valida se template existe e é imagem válida"""
        from PIL import Image
        try:
            with Image.open(template_path) as img:
                return True, img.size
        except Exception as e:
            return False, str(e)