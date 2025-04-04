from dimod import BinaryQuadraticModel
from dimod.reference.samplers import ExactSolver
from dwave.system import LeapHybridSampler, DWaveSampler, EmbeddingComposite
from dimod import BinaryQuadraticModel


# Solve the QUBO model using the specified solver
def solve_qubo_model(Q, offset=0, token=None, solver_type="exact", num_reads=10):

    bqm = BinaryQuadraticModel.from_qubo(Q, offset=offset)

    if solver_type == "exact":
        solver = ExactSolver()
        result = solver.sample(bqm)
    elif solver_type == "hybrid":
        solver = LeapHybridSampler(token=token)
        result = solver.sample(bqm)
    elif solver_type == "quantum":
        solver = EmbeddingComposite(DWaveSampler(token=token))
        result = solver.sample(bqm, num_reads=num_reads, auto_scale=True)
    else:
        raise ValueError(f"Solver {solver_type} is not supported")

    return result
