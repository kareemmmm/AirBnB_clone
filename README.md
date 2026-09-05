# AirBnB Clone - The Console

## Description

This project is the first step towards building a full clone of the AirBnB web application. It lays the groundwork for the entire stack: storage, models, console (command interpreter), and eventually a web front end and API.

This first stage focuses on building a **command interpreter** to manage the objects of the project:

* Create a new object (e.g. a new `User` or `Place`)
* Retrieve an object from a file, a database, etc.
* Do operations on objects (count, compute stats, etc.)
* Update attributes of an object
* Destroy an object

All objects are managed through a base class called `BaseModel`, which handles the initialization, serialization, and deserialization of future instances. Objects are stored and persisted to a JSON file through a storage engine called `FileStorage`.

### Project structure

```
AirBnB_clone/
├── console.py          # Entry point of the command interpreter
├── models/
│   ├── __init__.py     # Creates a unique FileStorage instance
│   ├── base_model.py    # BaseModel class: init, save, to_dict
│   ├── engine/
│   │   └── file_storage.py  # Serializes/deserializes instances to/from JSON
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   └── review.py
├── tests/               # Unit tests for the whole project
├── README.md
└── AUTHORS
```

## Command Interpreter

The console is a custom shell built on Python's `cmd` module. It is used to manage the objects of the AirBnB clone project (create, show, update, destroy, and more) before there is a web interface.

### How to start it

Clone the repository and, from the root of the project, run:

```bash
$ ./console.py
```

or

```bash
$ python3 console.py
```

This will launch an interactive prompt:

```
(hbnb)
```

The console can also be run in **non-interactive mode** by piping commands into it:

```bash
$ echo "help" | ./console.py
```

### How to use it

Once inside the console, type `help` to see the list of available commands, or `help <command>` for details on a specific one.

| Command | Description |
| --- | --- |
| `help` | Displays help about available commands |
| `quit` / `EOF` | Exits the console |
| `create <class>` | Creates a new instance of a class, saves it, and prints its id |
| `show <class> <id>` | Prints the string representation of an instance |
| `destroy <class> <id>` | Deletes an instance based on the class name and id |
| `all` / `all <class>` | Prints all string representations of instances, optionally filtered by class |
| `update <class> <id> <attribute name> "<attribute value>"` | Updates an instance by adding or updating an attribute |

Supported classes: `BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`, `Review`.

### Examples

**Interactive mode:**

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907

(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': ..., 'updated_at': ...}

(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {...}"]

(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) quit
$
```

**Non-interactive mode:**

```bash
$ echo "create User" | ./console.py
c4f2b1e2-0c9a-4e6f-9c3b-4a8b2e1d5f6a

$ echo 'all User' | ./console.py
["[User] (c4f2b1e2-0c9a-4e6f-9c3b-4a8b2e1d5f6a) {...}"]
```

## Running Tests

Unit tests are located in the `tests/` folder and can be run with:

```bash
$ python3 -m unittest discover tests
```

## Authors

See the [AUTHORS](AUTHORS) file for the list of contributors to this project.
