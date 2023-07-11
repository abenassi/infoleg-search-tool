import os
import requests
from zipfile import ZipFile
import pandas as pd


def download_and_read_zip(url, local_zip_path):
    # Check if the ZIP file already exists
    if not os.path.exists(local_zip_path):
        # If not, download the file
        response = requests.get(url)
        with open(local_zip_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded file: {local_zip_path}")
    else:
        print(f"File already exists: {local_zip_path}")

    # Get the directory of the ZIP file
    zip_dir = os.path.dirname(local_zip_path)

    # Extract the ZIP file in the same directory as the ZIP file
    with ZipFile(local_zip_path, "r") as zip_ref:
        zip_ref.extractall(zip_dir)
        print(f"Extracted all files from {local_zip_path} to {zip_dir}")

    # Find the CSV file in the ZIP file
    csv_filename = None
    for file in zip_ref.namelist():
        if file.endswith(".csv"):
            csv_filename = file
            break

    # If a CSV file was found, read it into a dataframe
    if csv_filename:
        df = pd.read_csv(os.path.join(zip_dir, csv_filename))
        return df
    else:
        print("No CSV file found in the ZIP file.")
        return None


def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")
    else:
        print(f"Directory already exists: {directory}")
