import requests


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def download_data():
    file_ids = {
        'yelp_review_full_csv.tar.gz': '0Bz8a_Dbh9QhbZlU4dXhHTFhZQU0',
        # 'sogou_news_csv.tar.gz': '0Bz8a_Dbh9QhbUkVqNEszd0pHaFE'
    }
    for destination, file_id in file_ids.items():
        download_file_from_google_drive(file_id, "dataset/" + destination)
