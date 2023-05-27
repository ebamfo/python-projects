import json
import os.path

class ToDo:
    def __init__(self):
        #Checks whether file exist
        self.path = './tasks.json'
        self.check_file = os.path.isfile(self.path)


    #This function creates a task   
    def create_task(self):
        #Takes task name and task description from user, creates dict 
        #of that then adds that entry to the to-do list

        task_descript=''   ##Var for task description, initialises to '' to allow for empty task description
        task_name=None
        
        #Getting task name and description from user
        while task_name==None:
            task_name=input('Enter name of task you want to create: ')
        task_descript=input('Enter description of task (optional): ')

        created_task={"title":task_name, "description":task_descript} #dict of created task 

        #Checks whether file exist        
        #if file exists, read contents and if file is empty, initialise var to be read to to {}
        if self.check_file==True: 
            with open('tasks.json',"r") as f:
                try:
                    task_list=json.load(f)
                #Except allows for empty files to be opened and sets tasks to {} when empty
                except json.JSONDecodeError:
                    task_list={}
        if not self.check_file:
            #If it does not exist, initialise tasks_list to {}
            task_list={}
            

        #Key/Number of the new task created
        #creates key for new entry, key is the nth task
        key=str(len(task_list)+1)
        task_list[key]=created_task
        
        ##w mode creates file so caters for when check_file is false
        with open("tasks.json","w") as b:
            json.dump(task_list,b,indent=4)



    #Displays current tasks
    def print_task(self):
        if self.check_file==True:
            with open("tasks.json","r") as f:
                try:
                    task_list=json.load(f) 
                #Except allows for empty files to be opened and sets tasks to {} when empty
                except json.JSONDecodeError:
                    task_list={}
                    print('No tasks available')
        if not self.check_file:
            with open("tasks.json","x") as b:
                #print('No Tasks available')
                task_list={}

        if len(task_list) > 0:
            for num,tasks in task_list.items():
                print(f'{num}  {tasks["title"]}\n{tasks["description"]}')
        else:
            print('Task list is empty, Create a task first')



    #This function takes the tasks and re-numbers it in numerical order
    #Used in delete_task function
    def num_tasklist(self,numbered_tasks):
        old_keys=[]
        new_keys=[]

        #Generates new numbers in numerical order and length is based on number of current tasks
        for num, tasks in numbered_tasks.items():
            old_keys.append(num)

        #temp_keys=new numbers but are ints  
        temp_keys=list(range(1,len(old_keys)+1))

        #converts list on new key ints to str
        for n in temp_keys:
            new_keys.append(str(n))

        #list of tuple pair consisting of newkeys, old keys
        combined_keys=list(zip(new_keys,old_keys))

        #
        for i,j in combined_keys:
            numbered_tasks[i]=numbered_tasks.pop(j)

        return numbered_tasks


    #This function deletes a task 
    def delete_task(self):
        #User enters number of task to be deleted
        index=input('Enter task number you want to delete: ')
        if self.check_file==True:
            try:
                with open('tasks.json',"r") as f:
                    task_list=json.load(f)
                    task_list.pop(index)
                    #takes new list and re-numbers it numerically
                    task_list=self.num_tasklist(task_list)
            except json.JSONDecodeError:
                    task_list={}
                    print('\nNo tasks available to delete')
            with open('tasks.json',"w") as t:
                    json.dump(task_list,t,indent=4)
        if not self.check_file:
            with open("tasks.json","x") as b:
                task_list={}
            print('\nNo Tasks available to delete')
            
        
        




