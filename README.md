# AirBnB_clone
<img src="imgs/logo.png">
AirBnB stand for <b style="color:red"> AirBedandBreakfast</b> a service lets property owners rent out their spaces to travelers looking for a place to stay.


<img src="imgs/diagram.png">

## Steps:-
- create data models : User, State, City, Place.
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store in JSON file


## Files and Directories

- models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- tests directory will contain all unit tests.
- console.py file is the entry point of our command interpreter.
- models/base_model.py file is the base class of all our models. It contains common elements:

    attributes: id, created_at and updated_at
    methods: save() and to_json()

- models/engine directory will contain all storage classes (using the same prototype). For the moment we will have only one: file_storage.py

## Storage or DataBase structure:-

<img src="imgs/datadiagram.jpg">

## command interpreter to manage your AirBnB objects

<h3>Functions:-<h3>

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

### Examples Commands-
    
```bash
(hbnb) help                                                 # show commands
(hbnb) EOF                                                  # exiting console
(hbnb) quit                                                 # exiting console
(hbnb) create <classname>                                   # create new object class 
(hbnb) all <classname>                                      # display storage of classname
(hbnb) show <instance id>                                   # show object with id
(hbnb) update <classname> <instance id> <attribute> <value> # update object data
(hbnb) count <classname>                                    # count number of object created of specific class.
(hbnb) destroy <classname>  <instance id>                   # destroy or delete the instance by id 
```

        
    
## we going to read the file exist reload it and save them again with new data