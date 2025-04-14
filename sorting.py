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
def selection_sort(seznam,direction = "asc"):
    """

    :param list seznam: numerick arrej
    :param str direction: smer ascending nebo descengin
    :return: sorted numeric erej
    """
    delka = len(seznam)
    for i in range(delka):
        min_indx = i
        for j in range(i+1 ,delka):
            if direction == "asc":
                if seznam[j] < seznam[min_indx]:
                    min_indx = j

            elif direction == "desc":
                    if seznam[j] > seznam[min_indx]:
                        min_indx = j

        seznam[i],seznam[min_indx] = seznam[min_indx],seznam[i]
    return seznam


def bubble_sort(number_array):
    """

    :param number_array: list of nambrz
    :return: sorted numberz list
    """
    n = len(number_array)
    for i in range(n-1):
        # pokud podmíka zde tak slozitos o(n)
        for j in range(0,n-i-1):
            if number_array[j] > number_array[j+1]:
                number_array[j],number_array[j+1] = number_array[j+1],number_array[j]
    return number_array
def insertion_sort(number_array):
    """
    :param number_array: nezerazena posloupnost cisel
    :return: serazena posloupnost cisel
    """
    for i in range(1, len(number_array)):
        key = number_array[i]
        j = i - 1
        while j >= 0 and key < number_array[j]:
            number_array[j + 1] = number_array[j]
            j -= 1
        number_array[j + 1] = key
    return number_array
def main():
    data = read_data("numbers.csv")
    # print(data["series_1"])
    select = selection_sort(data["series_1"],"asc")
    print(select)
    bubl = bubble_sort(data["series_2"])
    # print(bubl)
    insert = insertion_sort(data["series_3"])
    # print(insert)
    pass


if __name__ == '__main__':
    main()
