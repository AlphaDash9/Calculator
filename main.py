import datetime as d

class Operations :
    
    work_done = {}

    def __str__(self):
        return str(self.work_done)

    def addition(self, args):
        ans = 0
        for num in args :
            ans += num
        work_string = ""
        for num in args :
            work_string += f'{num} + '
        work_string = work_string[0:-3]
        work_list = [work_string, f'{d.datetime.now().strftime("%Y/%M/%d")}']
        self.work_done[ans] = work_list
        del work_string, work_list
        return ans

    def substraction(self, num1, num2):
        ans = num1 - num2
        work_list = [f'{num1} - {num2}', f'{d.datetime.now().strftime("%Y/%M/%d")}']
        self.work_done[ans] = work_list
        del work_list
        return ans

    def multiply(self, args):
        ans = 1
        for num in args :
            ans = ans * num
        work_string = ""
        for num in args :
            work_string += f'{num} * '
        work_string = work_string[0:-3]
        work_list = [work_string, f'{d.datetime.now().strftime("%Y/%M/%d")}']
        self.work_done[ans] = work_list
        del work_list
        return ans

    def divide(self, num1, num2):
        ans = num1 / num2
        work_list = [f'{num1} / {num2}', f'{d.datetime.now().strftime("%Y/%M/%d")}']
        self.work_done[ans] = work_list
        del work_list
        return ans

    def display_history(self, date):
        with open("operation_list.txt", "r") as reading_file :
            if date == "all":
                for line in reading_file :
                    print(line)
            else :
                for line in reading_file :
                    if date in line :
                        print(line)
                    else :
                        continue

    def operation_storage(self) :
        with open("operation_list.txt", "a+") as operation_file :
            for keys, values in self.work_done.items() :
                operation_file.write(f'{keys} : {values}, ')
            operation_file.write('\n')

test = Operations()
while True :
    action = int(input("Enter the operation you want to perform (1 - Calculate / 2 - Display History) : "))
    if action == 1:
        work = int(input("Which calculation you want to perform (1 - Add / 2 - Substract / 3 - Multiply / 4 - Divide) : "))
        if work == 1:
            items = int(input("How many numbers you want to add : "))
            items_list = []
            for i in range(0, items):
                input_data = int(input())
                items_list.append(input_data)
                del input_data
            print(test.addition(items_list))
        elif work == 2:
            num1 = int(input())
            num2 = int(input())
            print(test.substraction(num1, num2))
        elif work == 3:
            items = int(input("How many numbers you want to multiply : "))
            items_list = []
            for i in range(0, items):
                input_data = int(input())
                items_list.append(input_data)
                del input_data
            print(test.multiply(items_list))
        elif work == 4:
            num1 = int(input())
            num2 = int(input())
            print(test.divide(num1, num2))
        else :
            break
    elif action == 2:
        date = input("Input the date (Year/Month/Day) ('all' for entire history) : ")
        if date == "all":
            test.display_history("all")
        else :
            test.display_history(date)
    else :
        break

    break_or_not = int(input("Do you want to continue (0 - No / 1 - Yes) : "))
    if break_or_not == 0:
        test.operation_storage()
        break
    elif break_or_not == 1 :
        continue
    else :
        test.operation_storage()
        break
