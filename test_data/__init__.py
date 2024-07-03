import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename):
    return os.path.join(FILES_DIR, filename)

CSV_FILE_PATH = get_path('books.csv')
JSON_FILE_PATH = get_path('users.json')