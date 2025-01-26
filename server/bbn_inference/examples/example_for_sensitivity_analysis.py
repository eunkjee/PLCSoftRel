from server.bbn_inference.sensitivity_analysis import *
from server.bbn_inference.examples.example_for_composite_model import run_example_for_composite_model
from server.bbn_inference.bbn_utils import run_sampling

def run_for_sensitivity_analysis():
    trace = run_example_for_composite_model()
    demands = get_number_of_required_demand(trace, pfd_goal=0.0001, confidence_goal=0.95)
    print("Number of required demands: ", demands)

def run_for_update_pfd():
    pfd_goal = 0.0001
    demand = 100000
    failures = 2

    trace = run_example_for_composite_model()
    filtered_pfd_trace = filter_outsiders(trace.posterior["PFD"])
    model = demand_model_func(demand=demand, observed_failures=failures, pfd_trace=filtered_pfd_trace)
    # TODO: might need to run sampling for a few times to stablize the results
    updated_trace = run_sampling(model, draws=19500, tune=500)

    print("Mean of prior PFD: ", trace.posterior["PFD"].mean().item())
    print("Mean of updated PFD: ", updated_trace.posterior["pfd_prior"].mean().item())
    print("PFD goal: ", pfd_goal)
    print("Before testing, confidence level: ", get_confidence(data=trace.posterior["PFD"], goal=pfd_goal))
    print(f"Testing results: #test cases: {demand}, #failures: {failures}")
    print("After testing, confidence level: ", get_confidence(data=updated_trace.posterior["pfd_prior"], goal=pfd_goal))

run_example_for_sensitivity_analysis()
