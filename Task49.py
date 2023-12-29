'''Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.'''

def print_menu():
    print('1) Create contact')
    print('2) Change contact')
    print('3) Find contact')
    print('4) Delate contact')
    print('5) Show phone book')
    print('6) Transfer a contact')
    print('7) Copy the phone book')
    print('8) Exit')

def count_phone_book(fail_name):
    with open(fail_name, "r") as fp:
        return sum([1 for line in fp])

def create_contact(fail_name):
    count = count_phone_book(fail_name)
    with open(fail_name, "a") as fail:
        contact = list()
        contact.append(str(count))
        contact.append(input('Enter the contacts name: '))
        contact.append(input('Enter the contacts phone: '))
        contact.append(input('Enter the contacts nik: '))
        fail.writelines(':'.join(contact) + '\n')

def change_contact(fail_name):
    with open(fail_name, "r") as fail:
        lines = fail.readlines()
    for line in lines:
        print(line, end='')
    id_for_change = int(input('Enter the ID number?:'))
    if 0 <= id_for_change <= len(lines):
        contact = list()
        contact.append(str(id_for_change))
        contact.append(input('Enter the contacts name: '))
        contact.append(input('Enter the contacts phone: '))
        contact.append(input('Enter the contacts nik: '))
        contact = ':'.join(contact) + '\n'
        lines[id_for_change] = contact
    with open(fail_name, "w") as fail:
        fail.writelines(lines)

def find_contact(fail_name):
    name = input('Enter the person name: ')
    with open(fail_name, "r") as fail:
        lines = fail.readlines()
    for line in lines:
        if name in line:
            print(line)
        else:
            print('Name not found')

def delate_contact(fail_name):
    with open(fail_name, "r") as fail:
        lines = fail.readlines()
    for line in lines:
        print(line, end='')
    id_for_change = int(input('Enter the ID number?:'))
    if 0 <= id_for_change <= len(lines):
        del lines[id_for_change]
    with open(fail_name, "w") as fail:
        fail.writelines(lines)

def show_phone_book(fail_name):
    with open(fail_name, "r") as fail:
        for line in fail:
            print(line, end="")

def transfer_contact(fail_name):
    with open(fail_name, "r") as fail:
        lines = fail.readlines()
    for line in lines:
        print(line, end='')
    id_transfer = int(input('Enter the ID number?:'))
    if 0 <= id_transfer <= len(lines):
        clone = lines[id_transfer]
    with open('copy_contact.txt', "w") as fail:
        fail.writelines(clone)    

def copy_the_phone_book(fail_name):
    with open(fail_name, "r") as fail:
        lines = fail.readlines()
    for line in lines:
        print(line, end='')
    with open('copy_the_phone_book.txt', "w") as fail:
        fail.writelines(lines)

def main():

    fail_book = ('phone_book.txt')
    while True:
        print_menu()
        input_number = int(input('Enter the number?: '))
        if input_number == 1:
            create_contact (fail_book)
        elif input_number == 2:
            change_contact(fail_book)
        elif input_number == 3:
            find_contact(fail_book)
        elif input_number == 4:
            delate_contact(fail_book)
        elif input_number == 5:
            show_phone_book(fail_book)
        elif input_number == 6:
            transfer_contact(fail_book)
        elif input_number == 7:
            copy_the_phone_book(fail_book)
        elif input_number == 8:
            break
    print('You have logged out of the phone book!')
    

main()