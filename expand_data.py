import csv

with open("input/data.csv", 'r') as csv_read_file:
    reader = csv.reader(csv_read_file)
    first_line = next(reader)
    with open("output/output.csv", 'w', newline='') as csv_write_file:
        writer = csv.writer(csv_write_file)
        writer.writerow(first_line)
        for row in reader:
            for i in range(int(row[4])):
                writer.writerow(row[:4] + [""] + [row[5]])
