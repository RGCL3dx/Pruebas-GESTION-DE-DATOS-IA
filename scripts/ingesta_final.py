import pandas as pd
from sqlalchemy import create_engine

# Tu conexión (usa tus propios datos inventados aquí)
motor = create_engine('postgresql://mi_usuario:mi_password123@localhost:5432/telco_db')

def mover_datos_a_la_db():
    try:
        print("Leyendo el archivo CSV con codificación Latin-1...")
        # AQUÍ ESTÁ EL CAMBIO:
        df = pd.read_csv('02_Base_WA_Fn-UseC_-Telco-Customer-Churn.csv', encoding='latin-1')
        
        print("Enviando datos a PostgreSQL...")
        df.to_sql('clientes_telco', motor, if_exists='replace', index=False)
        
        print("¡ÉXITO TOTAL! Los datos ya están en la base de datos.")

    except Exception as e:
        print(f"Error en el proceso: {e}")

if __name__ == "__main__":
    mover_datos_a_la_db()