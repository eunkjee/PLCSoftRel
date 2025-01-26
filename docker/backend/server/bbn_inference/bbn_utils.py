import arviz as az
import numpy as np
import time
import pymc as pm
import pymc.sampling.jax as pmjax
from scipy import stats

# histogram intepolation
def from_posterior(param, samples, bins=100):
    smin, smax = np.min(samples), np.max(samples)
    width = smax - smin
    x = np.linspace(smin, smax, bins)
    # y = stats.gaussian_kde(samples)(x)
    y = stats.rv_histogram(np.histogram(samples, bins=bins)).pdf(x)
    return pm.Interpolated(param, x, y)

def print_pymc_version():
    print(f"Running on PyMC v{pm.__version__}")

monitor_var_names = [
    "SR_DevH_post", "SR_DevM_post", "SR_DevL_post",
    "SR_VVH_post", "SR_VVM_post", "SR_VVL_post",
    "SR_Defect_introduced_in_current",
    "SR_Total_Remained_Defect",
    "SD_DevH_post", "SD_DevM_post", "SD_DevL_post",
    "SD_VVH_post", "SD_VVM_post", "SD_VVL_post",
    "SD_Defect_introduced_in_current", "SD_Total_Remained_Defect",
    "IM_DevH_post", "IM_DevM_post", "IM_DevL_post",
    "IM_VVH_post", "IM_VVM_post", "IM_VVL_post",
    "IM_Defect_introduced_in_current", "IM_Total_Remained_Defect",
    "ST_DevH_post", "ST_DevM_post", "ST_DevL_post",
    "ST_VVH_post", "ST_VVM_post", "ST_VVL_post",
    "ST_Defect_introduced_in_current", "ST_Total_Remained_Defect",
    "IC_DevH_post", "IC_DevM_post", "IC_DevL_post",
    "IC_VVH_post", "IC_VVM_post", "IC_VVL_post",
    "IC_Defect_introduced_in_current", "IC_Total_Remained_Defect",
    "generic_IC_Total_Remained_Defect",
    "generic_number_of_defects",
    "generic_SFP", "generic_FSD", "PFD"
]

func_dict = {
    "mean": np.mean,
    "std": np.std,
    "5%": lambda x: np.percentile(x, 5),
    "median": lambda x: np.percentile(x, 50),
    "95%": lambda x: np.percentile(x, 95),
}

def filtered_var_names(data):
    return list(filter(lambda x: x in [i for i in data.posterior.data_vars], monitor_var_names))

def print_summary(data, round_to=5):
    var_names = filtered_var_names(data)
    if not var_names:
        print(az.summary(data, stat_funcs=func_dict, round_to=round_to, extend=False))
    else:
        print(az.summary(data, var_names=filtered_var_names(data), stat_funcs=func_dict, round_to=round_to, extend=False))

def run_sampling(model, numpyro=False, draws=1000, tune=1000, chains=1):
    start = time.time()
    with model:
        if numpyro:
            trace = pmjax.sample_numpyro_nuts(draws=draws, tune=tune, chains=chains)
        else:
            trace = pm.sample(draws=draws, tune=tune, chains=chains)
    end = time.time()
    print("sampling time: ", end - start)
    print_summary(trace)

    return trace
