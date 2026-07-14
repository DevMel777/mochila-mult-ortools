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
  
   # Restrição capacidade da mochila:
   # Σ(peso_i * x_i) <= capacidade
    restricao = solver.Constraint(0, capacidade, "peso_maximo")

    expressao = ""

    for i in range(len(peso)):
        restricao.SetCoefficient(x[i], peso[i])
        expressao += f"{peso[i]}{x[i].name()}"
    
        if i < len(peso) - 1:
            expressao += " + "

    print("\nRestrição criada:")
    print(f"{expressao} <= {capacidade}")

    # Função Objetivo:
    # Maximizar o valor total dos itens selecionados.
    # Max Z = Σ(valor_i * x_i)

    func_obj = solver.Objective()

    expressao = ""

    for i in range(len(valor)):
        func_obj.SetCoefficient(x[i], valor[i])

        expressao += f"{valor[i]}{x[i].name()}"

        if i < len(valor) - 1:
            expressao += " + "

    func_obj.SetMaximization()

    print("\nFunção objetivo")
    print(f"Maximizar: Z = {expressao}")

   
   # Executa o modelo utilizando o solver SCIP.
    print("\nResolvendo o modelo...")

    status = solver.Solve()

    # Verifica se uma solução ótima foi encontrada.
    if status != pywraplp.Solver.OPTIMAL:
        print("Não foi encontrada uma solução ótima.")
        return

    print("Modelo resolvido com sucesso!")

    print("\nDescrevendo solução:\n")

    # Valor ótimo da função objetivo.
    print(f"Valor máximo = {func_obj.Value()}")

    peso_total = 0

    # Percorre todas as variáveis de decisão.
    for i in range(len(valor)):

        # Se a variável vale 1, o item foi selecionado.
        if x[i].solution_value() == 1:

            print(
                f"{x[i].name()} (selecionado) | "
                f"Item {i} | "
                f"Valor = {valor[i]} | "
                f"Peso = {peso[i]}"
            )

            peso_total += peso[i]

    print(f"\nPeso utilizado = {peso_total}")
    print(f"Capacidade = {capacidade}")


if __name__ == "__main__":
    main()