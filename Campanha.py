import sqlite3
import math
from scipy.integrate import quad


# =====================================================
# Modelo Matemático
# =====================================================

def receita_por_hora(t, A=100.0, k=0.1):
    """
    Receita instantânea:

        r(t) = A * e^(-k*t)

    onde:
        A = receita inicial (R$/hora)
        k = taxa de decaimento
    """
    return A * math.exp(-k * t)


def calcular_receita_total(T, A=100.0, k=0.1):
    """
    Calcula a integral definida da receita entre 0 e T.
    """

    if T < 0:
        raise ValueError("O tempo não pode ser negativo.")

    resultado, _ = quad(receita_por_hora, 0, T, args=(A, k))

    return resultado


# =====================================================
# Banco de Dados
# =====================================================

DB = "campanhas.db"


def criar_banco():

    with sqlite3.connect(DB) as conn:

        conn.execute("""
            CREATE TABLE IF NOT EXISTS campanhas (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                nome TEXT NOT NULL,

                duracao REAL NOT NULL,

                receita_inicial REAL,

                taxa_decaimento REAL,

                receita_total REAL
            )
        """)


def salvar_resultado(nome, duracao, A, k, receita_total):

    with sqlite3.connect(DB) as conn:

        conn.execute("""

            INSERT INTO campanhas
            (nome, duracao, receita_inicial,
             taxa_decaimento, receita_total)

            VALUES (?, ?, ?, ?, ?)

        """, (nome, duracao, A, k, receita_total))


def listar_campanhas():

    with sqlite3.connect(DB) as conn:

        cursor = conn.execute("""

            SELECT
                id,
                nome,
                duracao,
                receita_total

            FROM campanhas

        """)

        return cursor.fetchall()


# =====================================================
# Programa Principal
# =====================================================

def main():

    criar_banco()

    print("=" * 45)
    print(" SIMULADOR DE RECEITA DE CAMPANHA ")
    print("=" * 45)

    try:

        nome = input("Nome da campanha: ")

        duracao = float(input("Duração (horas): "))

        A = float(input("Receita inicial por hora [100]: ") or 100)

        k = float(input("Taxa de decaimento [0.1]: ") or 0.1)

        receita = calcular_receita_total(duracao, A, k)

        print("\nResultado")
        print("-" * 30)
        print(f"Campanha : {nome}")
        print(f"Duração  : {duracao:.2f} horas")
        print(f"Receita  : R$ {receita:,.2f}")

        salvar_resultado(
            nome,
            duracao,
            A,
            k,
            round(receita, 2)
        )

        print("\nResultado salvo com sucesso!")

        print("\nHistórico de campanhas:")

        for campanha in listar_campanhas():

            print(campanha)

    except ValueError as erro:

        print(f"\nErro: {erro}")

    except Exception as erro:

        print(f"\nErro inesperado: {erro}")


if __name__ == "__main__":
    main()