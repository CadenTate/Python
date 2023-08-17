import requests
import base64
import csv

app_id = "d0c5ded6fae89b7f8dea7146a0b40087ebe639c5a0eb375cc28fea5eaf266b64"
app_secret = "5009377a60f31755114ff720c7b43e72ebf6e1cf2864e404b1073e7425f30d38"

credentials = f"{app_id}:{app_secret}"
encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

headers = {
    "Authorization": f"Basic {encoded_credentials}"
}

url = "https://api.planningcenteronline.com/people/v2/people"
data = requests.get(url, headers=headers)

if data.status_code == 200:
    data = data.json()

# Extract 'data' from JSON
people_data = data.get('data', [])

# Specify the CSV file name
csv_filename = 'people_data.csv'

# Extracted CSV headers
csv_headers = [
    'id', 'first_name', 'middle_name', 'last_name', 'gender', 'birthdate',
    'anniversary', 'membership', 'status', 'created_at', 'updated_at'
]

# Extracted CSV rows
csv_rows = []

for person in people_data:
    attributes = person.get('attributes', {})
    person_id = person.get('id', '')
    
    csv_row = [
        person_id,
        attributes.get('first_name', ''),
        attributes.get('middle_name', ''),
        attributes.get('last_name', ''),
        attributes.get('gender', ''),
        attributes.get('birthdate', ''),
        attributes.get('anniversary', ''),
        attributes.get('membership', ''),
        attributes.get('status', ''),
        attributes.get('created_at', ''),
        attributes.get('updated_at', '')
    ]
    
    csv_rows.append(csv_row)

# Write CSV data to a file
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write headers
    csv_writer.writerow(csv_headers)
    
    # Write rows
    csv_writer.writerows(csv_rows)

print(f'CSV data has been written to {csv_filename}')

