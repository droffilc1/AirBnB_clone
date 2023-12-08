# 0x00. AirBnB clone - The console
A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

## Overview
The Airbnb Clone - The console is a powerful command-line interface designed to manage various aspects of the Airbnb Clone application.
It serves as a control center for administrators and users to interact with the system efficiently and perform essential operations.
<p align="center">
  <img src="https://github.com/droffilc1/AirBnB_clone/assets/97587370/cc285c35-367d-4f0d-869e-a5df4b171db3" alt="HolbertonBnB logo">
</p>
 
## Features

- Create your data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

## Motivation

To gain a deeper understanding of Python programming fundamentals and cement our knowledge of OOP concepts while adhering to best practices of Software Development.

## Running The Project

To get a local copy up and running you just need to follow the following steps in your terminal;
```bash
git clone "url"
```

where "url" (without quotation marks) is the url to this repository.

For example:

```bash
git clone https://github.com/droffilc1/AirBnB_clone.git
```

Here you're copying the contents of the AirBnB_clone repository on GitHub to your computer.

Change to the repository directory on your computer (if you are not already there):

```bash
cd AirBnB_clone
```

### Usage

- Interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
- Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Reference

* [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)
* [cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg)
* [uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)
* [datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)
* [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
* [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)
* [Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw)
* [cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ)
* [python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)

## Project Structure
### models directory
This directory will contain all classes used for the entire project. In object-oriented programming (OOP) projects, a class named "model" represents an object/instance.

### tests directory
This directory will contain all unit tests.

### console.py
The `console.py` file serves as the entry point of our command interpreter.

### models/base_model.py
The `base_model.py` file is the base class of all our models. It contains common elements:

- **Attributes:**
  - `id`
  - `created_at`
  - `updated_at`

- **Methods:**
  - `save()`
  - `to_json()`

### models/engine directory
This directory will contain all storage classes using the same prototype. Currently, there is only one: `file_storage.py`.

## Contributors

This project was created by [Clifford Mapesa](https://www.github.com/droffilc1)


