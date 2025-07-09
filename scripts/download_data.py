from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(
        'yt776styjsu/labeled-test-set-do-not-submit',
        path='uv/data',
        unzip=True
    )

if __name__ == "__main__":
    download_dataset()
