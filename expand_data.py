import os
import csv

# This code is primarily to duplicate rows the number of times specified in one of the
# columns. Specify which column has the duplication counts here.
DUPLICATE_COUNT_COLUMN_NAME = "ETareapixelcount"

INPUT_FOLDER = r"C:\Users\dsx\Box\#SWFTeam\15_Cross-Cutting_Research\Alfalfa_Flex_Paper\Data\ET\County_Aggregates"
OUTPUT_FOLDER = r"C:\Users\dsx\Downloads"

FILENAMES = ["ETfieldmedium.csv", "ETfieldL.csv", "ETfieldML.csv", "ETfieldextrashort.csv", "ETfieldshort.csv"]
OUTPUT_SUFFIX = "_duplicated.csv"


def write_file(input_path, output_path):
    with open(input_path, "r") as csv_read_file:
        reader = csv.DictReader(csv_read_file)
        first_line = next(reader)
        with open(output_path, "w", newline="") as csv_write_file:
            writer = csv.DictWriter(csv_write_file, fieldnames=first_line.keys())
            writer.writeheader()
            for row in reader:
                num_times_to_add = int(row[DUPLICATE_COUNT_COLUMN_NAME])
                row[DUPLICATE_COUNT_COLUMN_NAME] = ""
                
                # multiply the row by the specified amount into a new list of dicts
                multiplied_rows = [row,] * num_times_to_add
                writer.writerows(multiplied_rows)  # write them all at once to avoid a loop of writes


for filename in FILENAMES:
    base_name = os.path.splitext(filename)[0]
    input_path = os.path.join(INPUT_FOLDER, filename)
    output_path = os.path.join(OUTPUT_FOLDER, f"{base_name}{OUTPUT_SUFFIX}")
    write_file(input_path, output_path)

