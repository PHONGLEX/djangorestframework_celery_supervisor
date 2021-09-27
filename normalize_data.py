import os
import json
from pathlib import Path

from datetime import datetime


def processing_data():
    BASE_DIR = Path(__file__).resolve().parent
    DATA_DIR = os.path.join(BASE_DIR, 'book/fixtures')
    
    with open(os.path.join(DATA_DIR, 'mydata.json')) as json_file:
        json_text = json.load(json_file)
        books = []

        for book in json_text:
            book['fields']['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            book['fields']['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            books.append(book)

        f = open(os.path.join(BASE_DIR, 'book/fixtures/mydata.json'), "w")
        f.write(json.dumps(books))
		

if __name__ == '__main__':
    processing_data()


