from random import randint
import csv
import os

# * No Download: 0
# ? 123663,14,1,10,134,2017-11-06 16:00:04,,0

# * Download: 1
# ? 142508,127,0,0,213,2017-11-06 16:04:00,2017-11-06 16:06:13,1


def gen_qualized_training_data(input_train_path, equalized_train_path, size):
    """
    Generated equalized training data from an input
    unequalized training data file

    Args:
        input_train_path (str): Path to the full unqualized training file.
        equalized_train_path (str): Path to new empty equalized file.
        size (int): The number of records desired in total.
    """

    num_downloads = 0
    num_no_downloads = 0

    with open(input_train_path) as csvDataFile:
        with open(equalized_train_path, "wb") as equalized_train:
            csvReader = csv.reader(csvDataFile)
            csvWriter = csv.writer(equalized_train, delimiter=',')

            for row in csvReader:
                # * Run every 1 in 100 times.
                if (randint(0, 20) == 1):
                    if row[len(row) - 1] == "1" and num_downloads < size / 2:
                        csvWriter.writerow(row)
                        num_downloads += 1
                        print(",".join(row))
                    elif row[len(row) - 1] == "0" and num_no_downloads < size / 2:
                        csvWriter.writerow(row)
                        num_no_downloads += 1
                        print(",".join(row))

                    if num_downloads >= (size / 2) and num_no_downloads >= (size / 2):
                        # print(f"#{size} equalized records generatedd in #{input_train_path}")
                        break


if __name__ == "__main__":
    # * The number of lines we want in the CSV: Spits 50/50.
    num_records_desired = 1000

    # * Paths to input and  output files
    input_train_path = "train.csv"
    equalized_train_path = "equalized_train.csv"

    gen_qualized_training_data(
        input_train_path, equalized_train_path, num_records_desired)
