import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path,"r") as csvfile:
        reader = csv.DictReader(csvfile)
        data = {}
        for row in reader:
            for key,value in row.items():
                if key not in data:
                    data[key] = [int(value)]
                else:
                    data[key].append(int(value))
    return data

def main():
    data = read_data("numbers.csv")
    print(data)
    pass


if __name__ == '__main__':
    main()
