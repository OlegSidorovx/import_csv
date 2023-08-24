import csv


def get_file_structure(uploaded_file):
    with open(uploaded_file.path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader, [])

    structure = [{"column_name": col, "data_type": "unknown"} for col in header]
    return structure


def load_data_from_file(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data
