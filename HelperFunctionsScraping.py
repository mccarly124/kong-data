import csv

def scrape_json_key(element_block, headers):
    returned_list = []
    for element in element_block:
        data = []
        for head in headers:
            data.append(element[head])
        returned_list.append(data)
    return returned_list


def to_csv(csv_file, header_list, data):
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header_list)  # Write header row
        writer.writerows(data)

def to_database():
    return "Still processing"