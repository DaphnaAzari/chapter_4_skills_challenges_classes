

# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface



_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE


class ToDoList:

    # User-facing properties:
    #   none

    def __init__(self):
        # Parameters: none
        # Side effects:none
        #intialise list of self object like this: self.task_list  =[]
        #no return



     def add_to_list(self, task):
        # Parameters: string
        #task: string representing a single task
        #append task to list
        #returns list
        #Side-effects: 
        # List in init changed
        #if task not added - throws and Exception


    def mark_task_as_complete(self, task):
        # Parameter task is string needed to take off the list
        # remove task from list in init
        # Returns: list
        # Side-effects: 
        # List in init changed


## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given one added task 
#add_to_list adds to list
"""
def test_add_one_to_list():
to_do_list = ToDoList()
result = to_do_list.add_to_list("Walk the dog")
assert  result == ["Walk the dog"]

"""
Given two added tasks
#add_to_list adds to list
"""
def test_add_two_to_list():
to_do_list = ToDoList()
to_do_list.add_to_list("Walk the dog")
result = to_do_list.add_to_list("wash dishes")
assert result == ["Walk the dog", "wash dishes"]

"""


Given a task made with no alphambetical letters
#add_to_list should throw an error
"""
def test_no_alpha_throws_err():
to_do_list = ToDoList()
result =to_do_list.add_to_list("???")
assert result ==   => "You've attempted to add an invalid task to the list, please try again!" (err message)
```

Given a task made with an emptry string
#add_to_list should throw an error
"""
def test_empty_string_throws_err():
to_do_list = ToDoList()
result =to_do_list.add_to_list("")
assert result ==   => "You've attempted to add an empty task to the list, please try again!" (err message)
```
"""
Given one completed task 
#mark_task_as_complete removes from list and displays the final list
"""
def test_remove_one_task_from_list():
to_do_list = ToDoList()
to_do_list.add_to_list ("Walk the dog")
to_do_list.add_to_list ("Wash dishes")
result = to_do_list.mark_task_as_complete("Walk the dog")
assert result == ["wash dishes"]

"""
Given three completed task 
#mark_task_as_complete removes two from list and displays the final list
"""
def test_remove_two_tasks_from_list():
to_do_list = ToDoList()
to_do_list.add_to_list ("Walk the dog")
to_do_list.add_to_list ("Wash dishes")
to_do_list.add_to_list ("Wash the floor")
to_do_list.mark_task_as_complete("Wash dishes")
result = to_do_list.mark_task_as_complete("Walk the dog")
assert result == ["Wash the floor"]

"""
Given user tries to remove one empty task 
#mark_task_as_complete should throw an err
"""
def test_remove_one_empty_task_from_list():
to_do_list = ToDoList()
to_do_list.add_to_list ("Walk the dog")
to_do_list.add_to_list ("Wash dishes")
result = to_do_list.mark_task_as_complete("")
assert result == "You've attempted to remove an empty task from the list, please try again!" (err message)


Given user tries to remove a task that is not on the to do list 
#mark_task_as_complete should throw an err
"""
def test_remove_a_task__that_isnt_in_list():
to_do_list = ToDoList()
to_do_list.add_to_list ("Walk the dog")
to_do_list.add_to_list ("Wash dishes")
result = to_do_list.mark_task_as_complete("Wash the floor")
assert result == "You've attempted to remove a task that is not on the list, please try again!" (err message)

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
