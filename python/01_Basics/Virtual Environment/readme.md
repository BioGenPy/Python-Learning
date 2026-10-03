## What is a Virtual Environment?

A **virtual environment** in Python is an isolated environment on your computer, where you can run and test your Python projects.

It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.

Think of a virtual environment as a separate container for each Python project. Each container:

* Has its own Python interpreter
* Has its own set of installed packages
* Is isolated from other virtual environments
* Can have different versions of the same package

Using virtual environments is important because:

* It prevents package version conflicts between projects
* Makes projects more portable and reproducible
* Keeps your system Python installation clean
* Allows testing with different Python versions

## Creating a Virtual Environment

Python has the built-in `venv` module for creating virtual environments.

To create a virtual environment on your computer, open the command prompt, and navigate to the folder where you want to create your project, then type this command:


## Activate Virtual Environment

C:\Users\ *Your Name* > myfirstproject\Scripts\activate

## Install Packages

We will install a package called 'cowsay':

**`cowsay` is a fun, classic command-line program that generates an ASCII art image of a talking cow** with a message inside a speech bubble


## Using Package

Now that the 'cowsay' module is installed in your virtual environment, lets use it to display a talking cow.

Create a file called `test.py` on your computer. You can place it wherever you want, but I will place it in the same location as the `myfirstproject` folder -not* in* the folder, but in the same location.

Open the file and insert these three lines in it:


import cowsay

cowsay.cow("Good Mooooorning!")


## Deactivate Virtual Environment

(myfirstproject) C:\Users\ *Your Name* > deactivate


## Delete Virtual Environment

Another nice thing about working with a virtual environment is that when you, for some reason want to delete it, there are no other projects depend on it, and only the modules and files in the specified virtual environment are deleted.

To delete a virtual environment, you can simply delete its folder with all its content. Either directly in the file system, or use the command line interface like this:

C:\Users\ *Your Name* > rmdir /s /q myfirstproject
