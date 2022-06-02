# Python CLI App for Big Data
Custom Order Form for a Business

## Project Description

A Python CLI application. This application performs basic CRUD operations with data stored in a MongoDB database. Users can interact with the application while it is running to perform such operations. Git and Github used for version control management.
This CLI application allows users to place a new custom order, modify their own information, cancel an order, and have record of their past orders.

## Technologies Used

- Python 3.10.4
- MongoDB 5.0.8
- Pymongo 4.1.1
- Git 2.35.1.windows.2

## Features

Current Features
- Pymongo connects the application to MongoDB
- Imports data from a JSON file into MongoDB

To-do list
- format check of user input to specific fields
- shipping updates and payment connect

## Getting Started
- git clone https://github.com/tammy508/project1

- ON WINDOWS 

- Installing Python
- 1. Install Python in Windows
- Go to https://www.python.org/downloads/
- Install the latest version of Python 3
- In the installation Wizard, be sure to check the box that you want to download pip
	- If you forgot to do this, you can always modify the installation later by openning up the installation wizard again.

- 2. Verify if python is properly installed
- Go to Command Prompt or PowerShell and type 'python'
	--- or ---
- Go to Command Prompt or PowerShell and type 'py'
- You should see something like this:

Result: Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

3. Verify pip is properly installed
- Open command prompt or PowerShell
- enter 'pip -V'
- You should see something like this:

Result: pip 21.2.4 from C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.752.0_x64__qbz5n2kfra8p0\lib\site-packages\pip (python 3.10)

- Installing MongoDB
- Follow instructions in: https://www.mongodb.com/try/download/community

## Usage
- Create a new order form by selecting from the menu. Prompts will ask for information.
- Delete the most recent order by selecting from the menu. Prompt will ask for email associated with orders.
- Create a .json file will all past orders by selecting from the menu. A file will be generated and saved to local machine.
- Update customer information by selecting from the menu. Prompt will ask for email associated with the account and changes can be made.
- Quit the application

## Contributors
- Tammy Huynh


## License
- No licenses were used.
