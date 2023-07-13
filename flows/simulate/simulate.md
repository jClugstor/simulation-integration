# Simulate Flow

## Kick off simulate
1. HMI -> SIM: [request an operation to be done](start.json)
1. SIM -> TDS: [create simulation](../../schemas/simulation.json)
  1. SIM -> TDS: [fetch model](3715ec46-b900-458c-8141-2974bafc92ff.json) 
1. SIM -> HMI: [returns the id of the job](../../schemas/job_id.json)

## Update simulate
1. SIM -> TDS: [update simulation object](start.json)

## Complete job
1. SIM -> TDS: [request presigned url to upload target]
  1. TDS -> SIM: [return url](../../schemas/simulation.json)
1. SIM -> S3: upload file to URL
1. SIM -> TDS [complete simulation object](../../schemas/simulation.json)
