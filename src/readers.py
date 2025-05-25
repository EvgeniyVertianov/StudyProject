import csv



def reader_csv_file(path_to_file: str) -> list:
    with open(path_to_file) as file:
        reader = csv.DictReader(file, delimiter=";")
        result = []
        for row in reader:
            result.append(row)
        return result


def reader_xlsx_file(path_to_file: str) -> None:
    pass


if __name__ == "__main__":
    print(reader_csv_file("/Users/vertianovev/Учеба/Code/StudyProject/data/transactions.csv"))

if __name__ == "__main__":
    print(reader_xlsx_file("/Users/vertianovev/Учеба/Code/StudyProject/data/transactions_excel.xlsx"))