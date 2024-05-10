# Real Estate Python CLI Project 

This CLI project is used to manage properties where you can add properties,clients,realtors and contracts.The application is for demonstrating Python Object Relation Mapping.The project contains a ```Models folder``` that contains the following files 
```clients,connect,contracts,property and a real_estate database file```. The database file is generated anew when ```initialize.py``` is run.

## Contents
1. ```property.py``` contains Property class to define properties and its methods.
2. ```realtor.py``` contains Realtor class to define realtors and its methods.
3. ```clients.py``` contains Client class to define clients and its methods.
4. ```contracts.py``` contains Contract class to define contracts and its methods and establishes a relation between all other classes.
5. ```connect.py``` establish connection to the database.
6. ```initialize.py``` clears and generates a new database file with empty tables.
7. ```cli.py``` starts the application.


## Built With
The code in the project is written using:

- Python


## Prerequisites
You need to have installed 
1. PyCharm or any other code editor
2. Python 3.10 installed
3. Sqlite extension or any other plugin/application in your editor to view database file

### Steps
1. Fork then clone the repository in the terminal:

    ```git@github.com:collinsbett023/collins-bett-real-estate.git```

2. Open the folder in your editor.
3. Open the Terminal in your code editor.
4. Run ```python3 initialize.py```.
5. Run ```python3 cli.py```.
6. Select any of the options presented in the terminal.


## Author
The repo is maintained by:
- Collins Bett

## LICENSE
```
Copyright 2024 COLLINS BETT

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```