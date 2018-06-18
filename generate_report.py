import json
import os
from pyreportjasper import JasperPy


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
JSON_FILENAME = '/tmp/users-list.json'
OUTPUT_FILENAME = '/tmp/users-list-report'


def json_to_reports():
    users = {'results': [{"name": "User {}".format(i)} for i in range(1, 11)]}
    input_file = os.path.join(CURRENT_DIR, 'users-list.jrxml')

    with open(JSON_FILENAME, 'w') as f:
        json.dump(users, f)

    json_query = 'results.name'

    jasper = JasperPy()
    jasper.process(
        input_file,
        output_file=OUTPUT_FILENAME,
        format_list=['pdf', 'docx', 'html'],
        parameters={},
        db_connection={
            'data_file': JSON_FILENAME,
            'driver': 'json',
            'json_query': json_query,
        },
        locale='pt_BR'
    )
    print('Files available in /tmp/ directory.')


if __name__ == '__main__':
    json_to_reports()
