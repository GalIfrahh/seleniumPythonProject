# seleniumPythonProject
selenium web automation using python + pytest + pytest-html reporter & pytest-testconfig 
for loading data from external file to the program (running same program for different client by different Json files).

# the project can run parallel testing using the excellent pytest abilities & plugins.

# the project use the conftest.py class for setting up the driver & all the project fixtures.

# the project is based on pageObjects architecture. 

The pageObjects concept

PageObject is a design pattern used to:

Simplify the way we identify and maintain the UI of the application we are testing
Write readable code that will be easy to other developers to understand and use
You can see many approaches to using PageObject. this one is mine:

First of all we will create a class called a GenericPageObject. this class will contain an instance of the webDriver/RemoteWebDriver (Which I like to put in a wrapping class , usually called webDriverWrapper) 
