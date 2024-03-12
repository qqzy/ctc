import requests
import zipfile
import os
from pathlib import Path

def retrieve_ctc_data(url, save_dir):
  zip_file = os.path.join(save_dir, url.split("/")[-1])
  with requests.get(url, stream=True) as req:
    req.raise_for_status()
    with open(zip_file, "wb") as file:
      for chunk in req.iter_content(chunk_size=8192):
        file.write(chunk)
  print(f"Unzip data set {os.path.basename(zip_file)}")
  with zipfile.ZipFile(zip_file) as z:
    z.extractall(save_dir)

  os.remove(zip_file)

if __name__=='__main__':
    data_set = "Fluo-N2DH-SIM+"
    ctc_data_url = "http://data.celltrackingchallenge.net"
    ctc_metrics_url = "http://public.celltrackingchallenge.net/software/EvaluationSoftware.zip"

    training_data_url = os.path.join(ctc_data_url, "training-datasets/")
    challenge_data_url = os.path.join(ctc_data_url, "test-datasets/")

    current_path = Path.cwd()
    data_path = current_path / 'dataset'
    ctc_metrics_path = os.path.join(current_path, "embedtrack", "ctc_metrics", "CTC_eval")

    # Download training data set
    if not os.path.exists(data_path / "train" / data_set):
        dp = os.path.join(data_path, "train", data_set)
        print(f"Downloading training data set to {dp} ...")
        data_url = training_data_url + data_set + ".zip"
        retrieve_ctc_data(data_url, os.path.join(data_path, "train"))

    # Download challenge data set
    if not os.path.exists(data_path / "challenge" / data_set):
        dp = os.path.join(data_path, "challenge", data_set)
        print(f"Downloading challenge data set to {dp} ...")
        data_url = challenge_data_url + data_set + ".zip"
        retrieve_ctc_data(data_url, os.path.join(data_path, "challenge"))

    # Download evaluation software
    if len(os.listdir(ctc_metrics_path)) <= 1:
        print(f"Downloading  ctc metrics to {ctc_metrics_path} ...")
        retrieve_ctc_data(ctc_metrics_url, ctc_metrics_path)