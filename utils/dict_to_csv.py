import csv


def write_dict_to_csv(data: dict, filename: str) -> None:
    # Flatten the dictionary to write to CSV
    flattened_data = []
    for layer, fields in data['layers'].items():
        for field_name, value in fields.items():
            flattened_data.append({
                'number': data['number'],
                'length': data['length'],
                'sniff_time': data['sniff_time'],
                'sniff_timestamp': data['sniff_timestamp'],
                'layer': layer,
                'field_name': field_name,
                'value': value
            })

    # Specify the CSV file headers
    headers = ['number', 'length', 'sniff_time', 'sniff_timestamp', 'layer', 'field_name', 'value']

    # Write to CSV file
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for row in flattened_data:
            writer.writerow(row)
