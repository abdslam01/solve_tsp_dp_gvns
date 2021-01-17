import csv
def read_data(file_path,file_path_1):
    with open(f'{file_path}') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',' if file_path.endswith('.csv') else '\t')
        costs = []
        for line in csv_reader:
            costs.append(line)
    with open(f'{file_path_1}', "w+") as csv_file:
        for i in costs:
            csv_file.write(",".join(i))
            csv_file.write("\n")
for i in range(4):
    read_data(f"instance{i}.txt",f"instance{i}.csv")
print("done")