import json
import os
from config import BASE_PATH


def read_json(system, file, filename):
    file_path = BASE_PATH + os.sep + "data" + os.sep + system + os.sep + file + os.sep + filename
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data


if __name__ == '__main__':
    print(read_json("admin", "page", "login_success.json")['password'])
