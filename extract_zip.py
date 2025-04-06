"""
This file unzips the source data files and saves them as parquet files to be used with spark
"""

import zipfile
import os

data_root_path = "sample1"

for file in os.listdir(data_root_path+ '/zip'):
    if file.endswith(".zip"):
        with zipfile.ZipFile(os.path.join(data_root_path+ '/zip', file), 'r') as zip_ref:
            zip_ref.extractall(data_root_path + '/raw')
            print(f"Extracted {file}")

