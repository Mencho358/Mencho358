# mt_oop.py

class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __gt__(self, other):
        if self.year != other.year:
            return self.year > other.year
        if self.month != other.month:
            return self.month > other.month
        return self.day > other.day

    def __repr__(self):
        return f'{self.year}/{self.month:02}/{self.day:02}'


# Starting test code
if __name__ == '__main__':
    date1 = Date(2, 12, 2024)
    date2 = Date(12, 11, 2023)
    date3 = Date(16, 11, 2023)

    print(f'{date1 = }') 
    # expected output: date1 = 2024/12/02

    print(f'{date2 = }') 
    # expected output: date2 = 2023/11/12

    print(f'{date3 = }') 
    # expected output: date3 = 2023/11/16

    print(f'{date1 > date2 = }') 
    # expected output: date1 > date2 = True

    print(f'{date2 > date3 = }') 
    # expected output: date2 > date3 = False
