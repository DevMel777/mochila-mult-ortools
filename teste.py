from ortools.linear_solver import pywraplp

def main():

    solver = pywraplp.Solver.CreateSolver("SCIP")

    if not solver:
        print("Erro ao criar solver.")
        return


if __name__ == "__main__":
    main()