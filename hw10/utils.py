import json
import os

def load_data(data_folder, data_filename):

    """загружает данные из файла Json и возвращает в виде словаря"""
    data_file_path = os.path.join(data_folder, data_filename)
    with open(data_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data