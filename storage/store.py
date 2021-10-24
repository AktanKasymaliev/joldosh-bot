import csv
from abc import abstractmethod
from io import TextIOWrapper

class Store:

    @abstractmethod
    def write(self) -> None:
        pass

    @abstractmethod
    def read(self):
        pass


class CsvManage(Store):

    def __init__(self) -> None:
        self.filename = "records.csv"
        self.file = open(self.filename)

    def writer(self, data, rownames) -> None:
        w = csv.writer(self.filename)
        w.writerow(rownames)
        w.writerows(data)
        self.file.close()
    
    def read(self):
        csvreader = csv.reader(self.file)
    
        for i in csvreader:
            print(i)
        self.file.close()