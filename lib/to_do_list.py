class ToDoList:

    # User-facing properties:
    #   none

    def __init__(self):
        self.task_list = []

    def add_to_list(self, task):
        if not any(char.isalpha() for char in task):
            raise Exception ("You've attempted to add an invalid task to the list, please try again!")
        self.task_list.append(task)
        return self.task_list


    def mark_task_as_complete(self, task):
        if task == "":
            raise Exception("You've attempted to remove an empty task from the list, please try again!")
        elif task not in self.task_list:
            raise Exception("You've attempted to remove a task that is not on the list, please try again!" )

        self.task_list.remove(task)
        return self.task_list