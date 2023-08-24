import tempfile
from django.test import TestCase
from .data_utils import get_file_structure, load_data_from_file


class DataUtilsTestCase(TestCase):
    def test_get_file_structure(self):
        csv_content = "name,age\nAlice,25\nBob,30\n"

        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_csv:
            temp_csv.write(csv_content)
            temp_csv_path = temp_csv.name

        structure = get_file_structure(temp_csv_path)
        self.assertEqual(len(structure), 2)

    def test_load_data_from_file(self):
        csv_content = "name,age\nAlice,25\nBob,30\n"
        temp_csv = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        temp_csv.write(csv_content)
        temp_csv.seek(0)

        data = load_data_from_file(temp_csv.name)
        self.assertEqual(len(data), 2)

        temp_csv.close()
