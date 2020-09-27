import pandas as pd
fixed_df = pd.read_table('telrecords.csv', ";")

base_of_numbers = list(fixed_df.loc[:, 'caller'])
base_of_innumbers = list(fixed_df.loc[:, 'caller'])
accepted = []
def inline_calls(number):
    for i in base_of_numbers:
        right = base_of_numbers[base_of_numbers['caller'] == number]['caller'].count()
        print(right)
        accepted.append(right)
        return accepted

def is_in_base(number):
    if number in base_of_numbers:
        print(number)
    else:
        print("Phone number not found")
        return False


def perform(number):
    if number:
        is_in_base(number)
    elif number == "":
        print("Bye!")
        exit()

def statistics(number):
    inline_calls(number)
    average_time = []
    incoming_calls = []
    print("{} accepted outgoing calls".format(accepted))
    print("average time: " + str(average_time))
    print("{} accepted incoming calls".format(incoming_calls))

def choose(choice): # функция выбора пользователя
    if choice == "1":
        statistics(number)
    elif choice == "2":
        question()
    elif choice == "3":
        print("Bye!")
        exit()

def question():
    print("1) Enter your phone number: ")
    number = int(input())
    print()
    perform(number)

while True:
    print("1) Enter your phone number: ")
    number = int(input())
    print()
    perform(number)
    print("Select an action:")
    print("1 - Call statistics")
    print("2 - Call history with other contact")
    print("3 - Exit")
    print("Your choice: ")
    choice = input()
    print()
    choose(choice)