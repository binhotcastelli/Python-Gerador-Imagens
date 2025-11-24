import sys
import os
from pathlib import Path

# Adiciona src ao path
sys.path.append(str(Path(__file__).parent / "src"))

from data_handler import DataHandler
from image_processor import ImageGenerator
import pandas as pd

def main():
    # Inicializa componentes
    data_handler = DataHandler()
    image_gen = ImageGenerator()
    
    # Carrega dados
    try:
        df = data_handler.load_data("dados_produtos.csv")
        data_handler.validate_data(df)
    except Exception as e:
        print(f"❌ Erro ao carregar dados: {e}")
        return
    
    # Processa cada produto
    success_count = 0
    for index, row in df.iterrows():
        product_data = row.to_dict()
        
        # Gera nome do arquivo de saída
        output_filename = f"{product_data['produto'].replace(' ', '_')}_{product_data['uf']}.jpg"
        
        # Gera imagem
        success, result = image_gen.generate_product_image(product_data, output_filename)
        
        if success:
            print(f"✅ Gerado: {output_filename}")
            success_count += 1
        else:
            print(f"❌ Erro em {product_data['produto']}: {result}")
    
    print(f"\n🎯 Processamento concluído: {success_count}/{len(df)} imagens geradas")

if __name__ == "__main__":
    main()