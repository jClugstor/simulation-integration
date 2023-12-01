from glob import glob
import json
import os
import logging

import requests

from utils import create_project, add_asset

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

TDS_URL = os.environ.get("TDS_URL", "http://data-service:8000")


if __name__ == "__main__":
    # Get project ID from environment
    project_id = os.environ.get("PROJECT_ID")

    if project_id:
        logging.info(f"Found project ID in environment: {project_id}")
        proj_resp = requests.get(f"{TDS_URL}/projects/{project_id}")
        if proj_resp.status_code == 404:
            raise Exception(
                f"Project ID {project_id} does not exist in TDS at {TDS_URL}"
            )

        # if the project exists, remove all simulations from it
        types = ["simulations"]
        sim_resp = requests.get(
            f"{TDS_URL}/projects/{project_id}/assets", params={"types": types}
        )
        if sim_resp.status_code >= 300:
            raise Exception(
                f"Failed to check project for existing simulations: {sim_resp.status_code}: {sim_resp.json()}"
            )
        else:
            logging.info(f"Sim response: {sim_resp.json()}")
            for sim in sim_resp.json().get("simulations", []):
                sim_id = sim["id"]
                logging.info(f"Deleting {sim_id} from project {project_id}")
                del_resp = requests.delete(
                    f"{TDS_URL}/projects/{project_id}/assets/simulations/{sim_id}"
                )
                if del_resp.status_code >= 300:
                    logging.info(f"Failed to delete simulation {sim_id}")
    # if it does not exist, create it
    else:
        project_id = create_project()
        logging.info(
            f"No project ID found in environment. Created project with ID: {project_id}"
        )

    with open("project_id.txt", "w") as f:
        f.write(f"{project_id}")

    model_configs = glob("./data/models/*.json")
    for config_path in model_configs:
        config = json.load(open(config_path, "rb"))
        model = config["configuration"]
        model["id"] = config["id"]
        model_response = requests.post(
            TDS_URL + "/models",
            json=model,
            headers={"Content-Type": "application/json"},
        )
        if model_response.status_code >= 300:
            raise Exception(
                f"Failed to POST model ({model_response.status_code}): {config['id']}"
            )
        else:
            add_asset(model_response.json()["id"], "models", project_id)
        config["model_id"] = model_response.json()["id"]
        config_response = requests.post(
            TDS_URL + "/model_configurations",
            json=config,
            headers={"Content-Type": "application/json"},
        )

        if config_response.status_code >= 300:
            raise Exception(
                f"Failed to POST config ({config_response.status_code}): {config['id']}"
            )

    datasets = glob("./data/datasets/*.csv")
    for filepath in datasets:
        filename = filepath.split("/")[-1]
        dataset_name = filename.split(".")[0]
        dataset = {"id": dataset_name, "name": dataset_name, "file_names": [filename]}
        dataset_response = requests.post(
            TDS_URL + "/datasets",
            json=dataset,
            headers={"Content-Type": "application/json"},
        )
        if dataset_response.status_code >= 300:
            raise Exception(
                f"Failed to POSt dataset ({dataset_response.status_code}): {dataset['name']}"
            )
        else:
            add_asset(dataset_response.json()["id"], "datasets", project_id)

        url_response = requests.get(
            TDS_URL + f"/datasets/{dataset_name}/upload-url",
            params={"filename": filename},
        )
        upload_url = url_response.json()["url"]
        with open(filepath, "rb") as file:
            requests.put(upload_url, file)
