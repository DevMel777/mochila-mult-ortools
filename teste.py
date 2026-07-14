from ortools.linear_solver import pywraplp

def main():

    solver = pywraplp.Solver.CreateSolver("SCIP")

    if not solver:
        print("Erro ao criar solver.")
        return
 
    # Variáveis de decisão
    # Valor item
    valoir = [60, 100, 120]
    # Peso item
    peso = [10, 20, 30]
    # Capacidade máxima da mochila
    capacidade = 50
   
   

if __name__ == "__main__":
    main()