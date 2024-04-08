import pymc as pm
import numpy as np
from scipy import stats
from bbn_utils import run_sampling, from_posterior

def filter_outsiders(data, threshold=3):
    z_scores = stats.zscore(data[0])
    mask = np.abs(z_scores) < threshold
    return data[0][mask]

def demand_model_func(demand, observed_failures, pfd_trace):
    demand_model = pm.Model()
    with demand_model:
        pfd_prior = from_posterior("pfd_prior", pfd_trace, bins=1000)
        failures = pm.Binomial("failures", n=demand, p=pfd_prior, observed=observed_failures)
    return demand_model

def get_confidence(data, goal):
    return np.count_nonzero(data.posterior["pfd_prior"] <= goal) / data.posterior["pfd_prior"]["draw"].size

demands = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
iterations = len(demands)

def get_number_of_required_demand(trace, pfd_goal, confidence_goal):
    # filter out outliers for interpolation
    filtered_pfd_trace = filter_outsiders(trace.posterior["PFD"])

    original_confidence = np.count_nonzero(trace.posterior["PFD"] <= pfd_goal) / trace.posterior["PFD"]["draw"].size

    demand_traces = []
    max_confidence = original_confidence
    confidence_levels = []
    means = []

    for i in range(iterations):
        print("number of demands: ", demands[i])
        confidence = 0
        while confidence < max_confidence:
            demand_trace = run_sampling(demand_model_func(demands[i], 0, filtered_pfd_trace))
            confidence = get_confidence(demand_trace, pfd_goal)
            print("confidence: ", confidence)
            max_confidence = max(confidence, max_confidence)
        confidence_levels.append(confidence)
        means.append(demand_trace.posterior["pfd_prior"].mean().item())
        demand_traces.append(demand_trace)
        if confidence >= confidence_goal:
            break

    required_demand = None
    for index, level in enumerate(confidence_levels):
        if level == confidence_goal:
            required_demand = demands[index]
            break
        if level > confidence_goal and index - 1 > 0:
            required_demand = ((confidence_goal - confidence_levels[index-1]) / (level - confidence_levels[index-1]) * (demands[index] - demands[index-1])) + demands[index-1]
            break
    return required_demand
