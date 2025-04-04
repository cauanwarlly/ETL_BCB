import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)

    return


def salvarSqlite(df: pd.DataFrame, nome_banco: str, nome_tebla: str):
    conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tebla, conn, if_exists="replace", index=False)
    conn.close()


# 1. primeiro criar o schama (etlbcb) no MySQL workbench
def salavarMySQL(
    df: pd.DataFrame,
    usuario: str,
    senha: str,
    host: str,
    nome_banco: str,
    nome_tabela: str,
):
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{nome_banco}")
    df.to_sql(nome_banco, con=engine, if_exists="replace", index=False)
