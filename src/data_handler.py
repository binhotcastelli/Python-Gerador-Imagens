import pandas as pd
import os
import sys
from pathlib import Path

# Adiciona src ao path para import absoluto
sys.path.append(str(Path(__file__).parent))

from config import INPUT_DIR

class DataHandler:
    def __init__(self):
        self.input_dir = INPUT_DIR
    
    def load_data(self, filename):
        """Carrega dados de entrada"""
        file_path = self.input_dir / filename
        
        if filename.endswith('.csv'):
            return pd.read_csv(file_path)
        elif filename.endswith(('.xlsx', '.xls')):
            return pd.read_excel(file_path, engine='openpyxl')
        else:
            raise ValueError("Formato não suportado. Use CSV ou Excel")
    
    def validate_data(self, df):
        """Valida estrutura dos dados"""
        required_columns = ['produto', 'uf', 'quantidade', 'preco', 'imagem_template']
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Colunas faltantes: {missing_columns}")
        
        return True