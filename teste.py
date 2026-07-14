from ortools.init.python import init
from ortools.linear_solver import pywraplp

def main():

    solver = pywraplp.Solver.CreateSolver("SCIP")

    if not solver:
        print("Erro ao criar solver.")
        return
 
    # Variáveis de decisão
    # Valor item
    valor = [60, 100, 120]
    # Peso item
    peso = [10, 20, 30]
    # Capacidade máxima da mochila
    capacidade = 50

   # Criando variáveis de decisão binárias x0, x1, ..., xn
   # Cada variável pode assumir apenas os valores 0 ou 1
   # x_i ∈ {0,1}
    x = []
    for i in range(len(valor)):
        # Se entra na mochila ou não
        x.append(solver.IntVar(0, 1, f"x{i}"))  
    
    print(f"Variáveis criadas: {x, valor, peso, capacidade}") 

if __name__ == "__main__":
    main()