import uuid


def generate_workflow(workflow_name, workflow_description):
    workflow_id = str(uuid.uuid4())
    workflow_payload = {
        "id": workflow_id,
        "name": workflow_name,
        "description": workflow_description,
        "transform": {"x": 0, "y": 0, "k": 1},
        "nodes": [],
        "edges": [],
    }

    return workflow_payload, workflow_id


def generate_model_module(model_id, workflow_id, model_config_id=None):
    model_module_uuid = str(uuid.uuid4())
    config_output_uuid = str(uuid.uuid4())
    default_config_output_uuid = str(uuid.uuid4())

    model_label = model_config_id
    if model_label:
        model_label = model_label.capitalize()

    model_payload = {
        "id": model_module_uuid,
        "workflowId": workflow_id,
        "operationType": "ModelOperation",
        "displayName": "Model",
        "x": 400,
        "y": 150,
        "state": {"modelId": model_id, "modelConfigurationIds": [model_config_id]},
        "inputs": [],
        "outputs": [
            {
                "id": default_config_output_uuid,
                "type": "modelConfigId",
                "label": "Default config",
                "value": ["18d01d84-120e-452e-9ef5-1cee4c18bac1"],
                "status": "not connected",
            },
            {
                "id": config_output_uuid,
                "type": "modelConfigId",
                "label": model_label,
                "value": [model_config_id],
                "status": "connected",
            },
        ],
        "statusCode": "invalid",
        "width": 180,
        "height": 220,
    }

    return (
        model_payload,
        model_module_uuid,
        config_output_uuid,
        default_config_output_uuid,
    )


def generate_dataset_module(dataset_id, workflow_id):
    module_uuid = str(uuid.uuid4())

    dataset_output_uuid = str(uuid.uuid4())

    dataset_module_payload = {
        "id": module_uuid,
        "workflowId": workflow_id,
        "operationType": "Dataset",
        "displayName": "Dataset",
        "x": 375,
        "y": 550,
        "state": {"datasetId": dataset_id},
        "inputs": [],
        "outputs": [
            {
                "id": dataset_output_uuid,
                "type": "datasetId",
                "label": "traditional",
                "value": [dataset_id],
                "status": "connected",
            }
        ],
        "statusCode": "invalid",
        "width": 180,
        "height": 220,
    }

    return dataset_module_payload, module_uuid, dataset_output_uuid


def generate_calibrate_simulate_ciemms_module(
    workflow_id, config_id, dataset_id, simulation_output
):
    module_uuid = str(uuid.uuid4())

    config_uuid = str(uuid.uuid4())
    dataset_uuid = str(uuid.uuid4())
    sim_output_uuid = str(uuid.uuid4())

    module_payload = {
        "id": module_uuid,
        "workflowId": workflow_id,
        "operationType": "CalibrationOperationCiemss",
        "displayName": "Calibrate & Simulate (probabilistic)",
        "x": 1100,
        "y": 200,
        "state": {
            "chartConfigs": [],
            "mapping": [{"modelVariable": "", "datasetVariable": ""}],
            "simulationsInProgress": [],
        },
        "inputs": [
            {
                "id": config_uuid,
                "type": "modelConfigId",
                "label": config_id,
                "status": "connected",
                "value": [config_id],
            },
            {
                "id": dataset_uuid,
                "type": "datasetId",
                "label": dataset_id,
                "status": "connected",
                "value": [dataset_id],
            },
        ],
        "outputs": [
            {
                "id": sim_output_uuid,
                "type": "number",
                "label": "Output 1",
                "value": [{"runId": simulation_output}],
                "status": "not connected",
            }
        ],
        "statusCode": "invalid",
        "width": 420,
        "height": 220,
    }

    return module_payload, module_uuid, config_uuid, dataset_uuid


def generate_simulate_ciemms_module(workflow_id, config_id, simulation_output):
    module_uuid = str(uuid.uuid4())

    config_uuid = str(uuid.uuid4())
    sim_output_uuid = str(uuid.uuid4())

    module_payload = {
        "id": module_uuid,
        "workflowId": workflow_id,
        "operationType": "SimulateCiemssOperation",
        "displayName": "Simulate (probabilistic)",
        "x": 1100,
        "y": 200,
        "state": {
            "simConfigs": {"runConfigs": {}, "chartConfigs": []},
            "currentTimespan": {"start": 1, "end": 100},
            "numSamples": 100,
            "method": "dopri5",
            "simulationsInProgress": [],
        },
        "inputs": [
            {
                "id": config_uuid,
                "type": "modelConfigId",
                "label": "Model configuration",
                "status": "connected",
                "value": [config_id],
                "acceptMultiple": False,
            }
        ],
        "outputs": [
            {
                "id": sim_output_uuid,
                "type": "simOutput",
                "label": "Output 1",
                "value": [simulation_output],
                "status": "not connected",
            }
        ],
        "status": "invalid",
        "width": 420,
        "height": 220,
    }

    return module_payload, module_uuid, config_uuid


def generate_calibrate_ensemble_ciemss_module(
    workflow_id, config_ids, dataset_id, simulation_output
):
    module_uuid = str(uuid.uuid4())

    config_uuid = str(uuid.uuid4())
    dataset_uuid = str(uuid.uuid4())
    sim_output_uuid = str(uuid.uuid4())

    module_payload = {
        "id": module_uuid,
        "workflowId": workflow_id,
        "operationType": "CalibrateEnsembleCiemms",
        "displayName": "Calibrate ensemble (probabilistic)",
        "x": 1100,
        "y": 200,
        "state": {
            "chartConfigs": [],
            "mapping": [{"modelVariable": "", "datasetVariable": ""}],
            "simulationsInProgress": [],
            "extra": {"numSamples": 50, "totalPopulation": 1000, "numIterations": 10},
        },
        "inputs": [
            {
                "id": config_uuid,
                "type": "modelConfigId",
                "label": "Model configuration",
                "status": "connected",
                "value": config_ids,
                "acceptMultiple": True,
            },
            {
                "id": dataset_uuid,
                "type": "datasetId",
                "label": dataset_id,
                "status": "connected",
                "value": [dataset_id],
            },
        ],
        "outputs": [
            {
                "id": sim_output_uuid,
                "type": "number",
                "label": "Output 1",
                "value": [{"runId": simulation_output}],
                "status": "not connected",
            }
        ],
        "statusCode": "invalid",
        "width": 420,
        "height": 220,
    }

    return module_payload, module_uuid, config_uuid, dataset_uuid


def generate_simulate_ensemble_ciemms_module(workflow_id, config_ids):
    module_uuid = str(uuid.uuid4())

    config_uuid = str(uuid.uuid4())
    sim_output_uuid = str(uuid.uuid4())

    module_payload = {
        "id": module_uuid,
        "workflowId": workflow_id,
        "operationType": "SimulateEnsembleCiemms",
        "displayName": "Simulate ensemble (probabilistic)",
        "x": 1100,
        "y": 200,
        "state": {
            "chartConfigs": [],
            "mapping": [{"modelVariable": "", "datasetVariable": ""}],
            "simulationsInProgress": [],
            "extra": {"numSamples": 50, "totalPopulation": 1000, "numIterations": 10},
        },
        "inputs": [
            {
                "id": config_uuid,
                "type": "modelConfigId",
                "label": "Model configuration",
                "status": "connected",
                "value": config_ids,
                "acceptMultiple": True,
            }
        ],
        "outputs": [
            {
                "id": sim_output_uuid,
                "type": "number",
                "label": "Output 1",
                "value": [{"runId": "123"}],
                "status": "not connected",
            }
        ],
        "statusCode": "invalid",
        "width": 420,
        "height": 220,
    }

    return module_payload, module_uuid, config_uuid


# "Simulate (deterministic)"
def generate_simulate_sciml_module(workflow_id, model_id, simulation_output):
    module_uuid = str(uuid.uuid4())

    config_uuid = str(uuid.uuid4())
    sim_output_uuid = str(uuid.uuid4())

    module_payload = {
        "id": module_uuid,
        "workflowId": workflow_id,
        "operationType": "SimulateJuliaOperation",
        "displayName": "Simulate (deterministic)",
        "x": 1100,
        "y": 200,
        "state": {
            "currentTimespan": {"end": 100, "start": 1},
            "simConfigs": {"chartConfigs": [], "runConfigs": {}},
            "simulationsInProgress": [],
        },
        "inputs": [
            {
                "id": config_uuid,
                "type": "modelConfigId",
                "label": "Model configuration",
                "status": "connected",
                "value": [model_id],
                "acceptMultiple": False,
            }
        ],
        "outputs": [
            {
                "id": sim_output_uuid,
                "type": "simOutput",
                "label": "Output 1",
                "value": [simulation_output],
                "status": "not connected",
            }
        ],
        "status": "invalid",
        "width": 420,
        "height": 220,
    }

    return module_payload, module_uuid, config_uuid


# "Calibrate (deterministic)"
def generate_calibrate_sciml_module(
    workflow_id, model_id, dataset_id, simulation_output
):
    module_uuid = str(uuid.uuid4())

    config_uuid = str(uuid.uuid4())
    dataset_uuid = str(uuid.uuid4())
    sim_output_uuid = str(uuid.uuid4())

    module_payload = {
        "id": module_uuid,
        "workflowId": workflow_id,
        "operationType": "CalibrationOperationJulia",
        "displayName": "Calibrate (deterministic)",
        "x": 1100,
        "y": 200,
        "state": {
            "chartConfigs": [],
            "mapping": [{"modelVariable": "", "datasetVariable": ""}],
            "simulationsInProgress": [],
        },
        "inputs": [
            {
                "id": config_uuid,
                "type": "modelConfigId",
                "label": "Model configuration",
                "status": "connected",
                "value": [model_id],
                "acceptMultiple": False,
            },
            {
                "id": dataset_uuid,
                "type": "datasetId",
                "label": "Dataset",
                "status": "connected",
                "value": [dataset_id],
            },
        ],
        "outputs": [
            {
                "id": sim_output_uuid,
                "type": "number",
                "label": "Output 1",
                "value": [simulation_output],
                "status": "not connected",
            }
        ],
        "statusCode": "invalid",
        "width": 420,
        "height": 220,
    }

    return module_payload, module_uuid, config_uuid, dataset_uuid


def generate_edge(workflow_id, source_id, target_id, source_port, target_port):
    edge_uuid = str(uuid.uuid4())
    edge_payload = {
        "id": edge_uuid,
        "workflowId": workflow_id,
        "source": source_id,
        "sourcePortId": source_port,
        "target": target_id,
        "targetPortId": target_port,
        "points": [
            {
                "x": 0,
                "y": 0,
            },
            {
                "x": 0,
                "y": 0,
            },
        ],
    }
    return edge_payload, edge_uuid


def workflow_builder(
    workflow_name,
    workflow_description,
    simulation_type,
    model_id,
    simulation_output,
    dataset_id=None,
    config_ids=[],  # for ensemble
):
    workflow_payload, workflow_id = generate_workflow(
        workflow_name, workflow_description
    )

    if model_id:
        (
            model_payload,
            model_module_uuid,
            config_output_uuid,
            default_config_output_uuid,
        ) = generate_model_module(model_id, workflow_id, model_id)

        workflow_payload["nodes"].append(model_payload)

    if config_ids:
        config_uuids = []
        for id in config_ids:
            (
                model_payload,
                model_module_uuid,
                config_output_uuid,
                default_config_output_uuid,
            ) = generate_model_module(id, workflow_id, id)

            workflow_payload["nodes"].append(model_payload)
            config_uuids.append(config_output_uuid)

    if dataset_id:
        (
            dataset_payload,
            dataset_module_uuid,
            dataset_output_uuid,
        ) = generate_dataset_module(dataset_id, workflow_id)

        workflow_payload["nodes"].append(dataset_payload)

    match simulation_type:
        case "calibrate_pyciemss":
            (
                calibrate_simulate_payload,
                calibrate_simulation_uuid,
                config_input_uuid,
                dataset_input_uuid,
            ) = generate_calibrate_simulate_ciemms_module(
                workflow_id, model_id, dataset_id, simulation_output
            )
            workflow_payload["nodes"].append(calibrate_simulate_payload)

            model_simulate_edge, model_simulate_edge_uuid = generate_edge(
                workflow_id,
                model_module_uuid,
                calibrate_simulation_uuid,
                config_output_uuid,
                config_input_uuid,
            )
            workflow_payload["edges"].append(model_simulate_edge)

            dataset_simulate_edge, dataset_simulate_edge_uuid = generate_edge(
                workflow_id,
                dataset_module_uuid,
                calibrate_simulation_uuid,
                dataset_output_uuid,
                dataset_input_uuid,
            )
            workflow_payload["edges"].append(dataset_simulate_edge)

            return workflow_payload

        case "simulate_pyciemss":
            (
                simulate_ciemss_payload,
                simulate_ciemss_uuid,
                config_input_uuid,
            ) = generate_simulate_ciemms_module(
                workflow_id, model_id, simulation_output
            )
            workflow_payload["nodes"].append(simulate_ciemss_payload)

            model_simulate_edge, model_simulate_edge_uuid = generate_edge(
                workflow_id,
                model_module_uuid,
                simulate_ciemss_uuid,
                config_output_uuid,
                config_input_uuid,
            )
            workflow_payload["edges"].append(model_simulate_edge)

            return workflow_payload
        case "ensemble-calibrate_pyciemss":
            (
                calibrate_ensemble_payload,
                calibrate_ensemble_uuid,
                config_input_uuid,
                dataset_input_uuid,
            ) = generate_calibrate_ensemble_ciemss_module(
                workflow_id,
                config_ids=config_ids,
                dataset_id=dataset_id,
                simulation_output=simulation_output,
            )
            workflow_payload["nodes"].append(calibrate_ensemble_payload)

            for id in config_uuids:
                model_simulate_edge, model_simulate_edge_uuid = generate_edge(
                    workflow_id,
                    id,
                    calibrate_ensemble_uuid,
                    config_output_uuid,
                    config_input_uuid,
                )
                workflow_payload["edges"].append(model_simulate_edge)

            dataset_simulate_edge, dataset_simulate_edge_uuid = generate_edge(
                workflow_id,
                dataset_module_uuid,
                calibrate_ensemble_uuid,
                dataset_output_uuid,
                dataset_input_uuid,
            )
            workflow_payload["edges"].append(dataset_simulate_edge)

            return workflow_payload
        case "ensemble-simulate_pyciemss":
            (
                simulate_ensemble_payload,
                simulate_ensemble_uuid,
                config_input_uuid,
            ) = generate_simulate_ensemble_ciemms_module(
                workflow_id, config_ids=config_ids
            )
            workflow_payload["nodes"].append(simulate_ensemble_payload)

            for id in config_uuids:
                model_simulate_edge, model_simulate_edge_uuid = generate_edge(
                    workflow_id,
                    id,
                    simulate_ensemble_uuid,
                    config_output_uuid,
                    config_input_uuid,
                )
                workflow_payload["edges"].append(model_simulate_edge)

            return workflow_payload
        case "simulate_sciml":
            (
                simulate_sciml_payload,
                simulate_sciml_uuid,
                config_input_uuid,
            ) = generate_simulate_sciml_module(workflow_id, model_id, simulation_output)
            workflow_payload["nodes"].append(simulate_sciml_payload)

            model_simulate_edge, model_simulate_edge_uuid = generate_edge(
                workflow_id,
                model_module_uuid,
                simulate_sciml_uuid,
                config_output_uuid,
                config_input_uuid,
            )
            workflow_payload["edges"].append(model_simulate_edge)

            return workflow_payload
