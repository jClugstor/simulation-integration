# Simulate Flow

## Kick off simulate
1. HMI -> SIM: [request an operation to be done](start.json): POST `/simulate`
1. SIM -> TDS: [create simulation](../../schemas/simulation.json): POST `/simulations`
  1. SIM -> TDS: [fetch model](3715ec46-b900-458c-8141-2974bafc92ff.json): GET `/model_configurations/$id`
1. SIM -> HMI: [returns the id of the job](../../schemas/job_id.json)`

## Update simulate
1. SIM -> TDS: [update simulation object](../../schemas/simulation.json): PUT `/simulations/$sim_id`

## Complete job
1. SIM -> TDS: request presigned url to upload target: GET `/simulations/$sim_id/upload-url?filename=result.csv`
  1. TDS -> SIM: return url
1. SIM -> S3: upload file to URL
1. SIM -> TDS [complete simulation object](../../schemas/simulation.json): PUT `/simulations/$sim_id`
