# behave-amazon
An automated script using Python and Behave to automate a guest shopper's journey on amazon.com

## Tools and Framework Used.
* Language: Python
* Language version: 3.7.5
* Selenium
* brew
* Webdriver: Chrome
* Framework: Behave
* Framework version: 1.2.6
* IDE: Pycharm (Professional Edition)
* OS: macOS (Catalina 10.15.4)
## Installation and usage.
Installation and usage can be done via the terminal or used through the Pycharm IDE.
## Using the Terminal
* open terminal
* Install python by running _**"brew install python3"**_
* Install behave and selenium by running _**"pip3 install behave selenium"**_
* Install chromedriver by running _**"brew cask install chromedriver"**_
* Navigate to the folder cloned from git.
* run >behave ./Features/guest_shopper.feature
## Using the IDE
## Create a Python Virtual environment.
So you can have an isolated working directory of the Python environment so
as to keep the global Python free of installed dependencies. This ensures 
that the environment created only affects the project. This means the 
environment forms our project working directory.
> **STEPS:**
> * Open terminal
> * Check if **virtualenv** is installed on the system: virtualenv --version.
> * If it is not installed, install using _"pip3 install virtualenv"_.
> * If it is installed, go ahead and create a directory where the virtual
> environment will be located.
> * Navigate to the directory and create the new virtual environment. 
>by using the command _"virtualenv <name_of_environment>"_
> * Install selenium with _"pip install selenium"_
> * Install behave with _"pip install behave"_
> * Copy this project into the environment
> * Activate the virtual environment by using 
>_source <name_of_environment>/bin/activate_
**NB:** To deactivate, just type _**deactivate**_ and hit enter
## Pycharm IDE
* Install Pycharm (Professional Edition).
* Open and navigate to the folder where this project has been copied 
and open it.
* Click the **Run** Tab and click add/edit configuration.
* Click the **+** and select **Behave**
* Name the config
* On the **Feature files or folders**, navigate to the Features folder of 
this project.
* Ensure the virtualenv is being used as the interpreter.
* Click **Apply** and **OK**.
## Project Execution
>Navigate into the Features folder and run _**"behave"**_

## What does this script do?

Normally, we get on any e-commerce site to search for an item to buy 
online without bothering to sign in or register because we are excited. 
So we search for the item, add it to cart, the proceed to checkout. 
It is at this point that the system reminds us that we have to register 
or sign in before we can make a purchase on the site.

This simple script designed with Selenium, Python and behave framework
helps to capture that journey and verify that a user is redirected to 
the sign in or sign up page when the user gets to the point of checkout.