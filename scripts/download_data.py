import os
import sys
from kaggle.api.kaggle_api_extended import KaggleApi

def main():
    kaggle_json = os.path.expanduser("~/.kaggle/kaggle.json")
    if not os.path.exists(kaggle_json):
        print("[ERROR] kaggle.json not found at ~/.kaggle/kaggle.json")
        print("Download from Kaggle account > Create New API Token")
        sys.exit(1)

    api = KaggleApi()
    api.authenticate()

    data_dir = "uv/data"
    os.makedirs(data_dir, exist_ok=True)

    competition = "digit-recognizer"

    print(f"[INFO] Downloading competition data: '{competition}'...")
    api.competition_download_files(
        competition,
        path=data_dir,
        force=True
    )

    zip_path = os.path.join(data_dir, f"{competition}.zip")
    if os.path.exists(zip_path):
        print("[INFO] Unzipping...")
        os.system(f"unzip -o {zip_path} -d {data_dir}")
        print("[INFO] Done!")
    else:
        print("[ERROR] Download failed or zip not found.")

if __name__ == "__main__":
    main()