import arviz as az

from bbn_inference.bbn_utils import run_sampling
from bbn_inference.data import nrc_report_data
from bbn_inference.composite_model import *

def run_example_for_composite_model():

    data = nrc_report_data()
    SR_Dev_model = create_SR_Dev_model(data.attr_states)
    SR_VV_model = create_SR_VV_model(data.attr_states)
    SD_Dev_model = create_SD_Dev_model(data.attr_states)
    SD_VV_model = create_SD_VV_model(data.attr_states)
    IM_Dev_model = create_IM_Dev_model(data.attr_states)
    IM_VV_model = create_IM_VV_model(data.attr_states)
    ST_Dev_model = create_ST_Dev_model(data.attr_states)
    ST_VV_model = create_ST_VV_model(data.attr_states)
    IC_Dev_model = create_IC_Dev_model(data.attr_states)
    IC_VV_model = create_IC_VV_model(data.attr_states)

    SR_Dev_trace = run_sampling(SR_Dev_model, True)
    SR_VV_trace = run_sampling(SR_VV_model, True)
    SD_Dev_trace = run_sampling(SD_Dev_model, True)
    SD_VV_trace = run_sampling(SD_VV_model, True)
    IM_Dev_trace = run_sampling(IM_Dev_model, True)
    IM_VV_trace = run_sampling(IM_VV_model, True)
    ST_Dev_trace = run_sampling(ST_Dev_model, True)
    ST_VV_trace = run_sampling(ST_VV_model, True)
    IC_Dev_trace = run_sampling(IC_Dev_model, True)
    IC_VV_trace = run_sampling(IC_VV_model, True)

    # TODO: run sampling for whole model and save the trace to be used as generic trace (simulation traces for generic number of defects)
    # the below code is used to save simulation traces into a local file
    # eg. whole_model_trace.to_netcdf(filename="whole_model_trace_data_1000.nc")
    # the example trace was collected with the following sampling configuration (draws=1000, tunes=1000, numpyro=True)
    generic_trace = az.from_netcdf("./bbn_inference/examples/whole_model_trace_data_1000.nc")

    model = create_composite_model(SR_Dev_trace=SR_Dev_trace, SR_VV_trace=SR_VV_trace,
                                   SD_Dev_trace=SD_Dev_trace, SD_VV_trace=SD_VV_trace,
                                   IM_Dev_trace=IM_Dev_trace, IM_VV_trace=IM_VV_trace,
                                   ST_Dev_trace=ST_Dev_trace, ST_VV_trace=ST_VV_trace,
                                   IC_Dev_trace=IC_Dev_trace, IC_VV_trace=IC_VV_trace,
                                   generic_trace=generic_trace,
                                   function_point=data.function_point,
                                   complexity=data.complexity,
                                   interpolation_bins=32)
    trace = run_sampling(model)
    return trace
