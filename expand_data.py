import csv

with open("input/data.csv", "r") as csv_read_file:
    reader = csv.reader(csv_read_file)
    first_line = next(reader)
    with open("output/output.csv", "w", newline="") as csv_write_file:
        writer = csv.writer(csv_write_file)
        writer.writerow(first_line)
        for row in reader:
            num_times_to_add = int(row[4])
            row[4] = ""
            for i in range(num_times_to_add):
                writer.writerow(row)
