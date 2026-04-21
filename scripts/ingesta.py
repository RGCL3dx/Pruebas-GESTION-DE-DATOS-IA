import pandas as pd # Para manejar los datos en tablas (DataFrames)
from sqlalchemy import create_engine # Para conectar Python con la base de datos
import os # Para manejar rutas de carpetas y archivos
import sys # Para configurar la lectura de caracteres en Windows

# 1. SOLUCIÓN AL ERROR DE WINDOWS:
# Esto obliga a Python a usar UTF-8 para evitar errores con tildes o la "ñ" en las rutas
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def ejecutar_ingesta():
    # 2. CONFIGURAR LA CONEXIÓN:
    # Definimos: usuario (mi_usuario), contraseña (mi_password), servidor (localhost) y base de datos (telco_db)
    engine = create_engine('postgresql://mi_usuario:mi_password@localhost:5432/telco_db')
    
    # 3. RUTA DEL ARCHIVO:
    # Apuntamos a la carpeta 'data' donde está tu archivo CSV
    ruta_archivo = 'data/02_Base_WA_Fn-UseC_-Telco-Customer-Churn.csv'
    
    # 4. VALIDACIÓN:
    # Verificamos si el archivo realmente existe en esa carpeta antes de intentar leerlo
    if os.path.exists(ruta_archivo):
        # 5. EXTRACCIÓN (READ):
        # Leemos el archivo CSV y lo guardamos en la variable 'df'
        df = pd.read_csv(ruta_archivo)
        
        print(f"Archivo encontrado. Filas a cargar: {len(df)}")
        
        # 6. CARGA (LOAD):
        # Enviamos el contenido a la tabla 'clientes_churn' en PostgreSQL
        # if_exists='replace' borra la tabla vieja y crea la nueva cada vez que corres el script
        # index=False evita que se cree una columna extra con los números de fila
        df.to_sql('clientes_churn', engine, if_exists='replace', index=False)
        
        print("¡Éxito! Los datos han sido guardados en PostgreSQL.")
    else:
        # Si el nombre del archivo o la carpeta están mal, avisamos aquí:
        print(f"Error: No se encontró el archivo en la ruta: {ruta_archivo}")

# Punto de entrada para ejecutar el script
if __name__ == "__main__":
    ejecutar_ingesta()