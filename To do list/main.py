from TodoListFunc import ToDo

todo=ToDo()

def tasks():

    while True:
        print('\n\nWhat do you want to do today \n')
        print('1. View Tasks')
        print('2. Create a task')
        print('3. Delete a task')
        print('4. Enter 9 if you want to quit\n')

        choice=input('Enter Choice: ')
        print()

        match choice:
            case '1':
                todo.print_task()
                continue
            
            case '2':
                todo.create_task()
                continue

            case '3':
                todo.delete_task()
                continue

            case '9':
                break

            case _:
                print('You entered an invalid option')
                tasks()



if __name__ == "__main__":
        tasks()







