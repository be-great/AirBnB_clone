# Quit method 
## Add print new line when quit the console
**i don't sure should i add this new line or not**
```python
print()
```
## The final code of method
```python
    def do_quit(self, arg):
        """Quit command to exit the program"""
        print()
        return True

```
# Default method:
## I added a dictionary contain all methods of HBNB  to use it later in this form \<class\>.\<method\>
```python
        subcommands = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count}
        # This way is easer than old way
        # How it's work:
        # A dictionary mapping subcommand names to their corresponding methods
        # Call the corresponding method from the subcommands dictionary,
        # passing the classname as an argument

```
## return specific method 
```python 
            if methodname in subcommands.keys():
                return subcommands[methodname](f"{classname} {idArg}")

```

## handle \<class\>.\<method\>
```python
            idArg = parts[1].split("(")[1].split(")")[0] ## The problem is this method not work if id number inside "" and work without "" try it

```

## The final code of method
```python
    def default(self, arg):
        subcommands = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count}
        # This way is easer than old way
        # How it's work:
        # A dictionary mapping subcommand names to their corresponding methods
        # Call the corresponding method from the subcommands dictionary,
        # passing the classname as an argument

        parts = arg.split(".")
        if len(parts) > 1:
            classname = parts[0]
            methodname = parts[1].split("(")[0]
            idArg = parts[1].split("(")[1].split(")")[0] ## The problem is this method not work if id number inside "" and work without "" try it
            if methodname in subcommands.keys():
                return subcommands[methodname](f"{classname} {idArg}")
        print("*** Unknown syntax: ()".format(parts))
        return False

```

# Count method 
## Use count variable to count how many instances of class
```python
        countOfInstances = 0
```
---
```python
                    if (obj.to_dict())["__class__"] == arguments[0]:
                        countOfInstances += 1  # Increment the counter if their
                        # class matches
                print(countOfInstances)

```

## The final code 
```python
    def do_count(self, arg):
        countOfInstances = 0
        arguments = arg.split()
        if arguments:
            if arguments[0] not in self.__classnames:
                # if class name passed but not exist
                print("** class doesn't exist **")
            else:
                all_objs = storage.all()
                for obj_class in all_objs.keys():
                    obj = all_objs[obj_class]
                    # Check if the object's class matches the specified class
                    if (obj.to_dict())["__class__"] == arguments[0]:
                        countOfInstances += 1  # Increment the counter if their
                        # class matches
                print(countOfInstances)
        else:
            # If no class name passed
            print("** class name missing **")

```