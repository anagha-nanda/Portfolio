# Assignment Portfolio

## Table of contents
* [Introduction](#Introduction)
* [About the Software](#About_the_Software)
* [Contents](#Contents)
* [Installation](#Installation)
* [Key Learnings and Known Issues](#Key_Learnings_and_Known_Issues)
* [Further Development](#Further_Development)
* [Copyright](#Copyright)

## Introduction
This Project presents the activities prescribed in the module GEO5003: Programming for Geographical Information Analysis to fulfil the requirements for Assignment 1: Online Portfolio.

## About the Software
Four Python files are included as part of this Portfolio.

1. Creation, manipulation, and display of Agents
2. Agent class framework
3. Web scraping using beautiful soup library
4. Creation of a Graphic User Interphase

The code in the first file has been split into different functions to capture each of the activities prescribed in the module. The program works by creating a list of objects of the class 'Agents' either using the random function or by reading from a .csv file containing environmental data.

The user is then allowed to manipulate the agents. A menu is displayed and the user is allowed to make a suitable selection. The functions available include display data, move agents, nibble environment, share with neighbours, animate agents, write agents to a .csv file, shuffle the order of the Agents in the list etc.

## Contents 
All files are saved on the 'Portfolio' repository. 

All activities related to the creation, manipulation, and display of Agents are included in a single module called final_module.py. The Agent class has been defined on a module titled agentframework.py. 

The gui.py file creates a basic Graphic User Interphase.

The web_scraping.py file scrapes a webpage using the beautiful soup library and displays 'x' and 'y' data from a table on the webpage.

The LICENSE and README file have also been included in the same repository. 

## Installation
1. Download this software as a zip file and extract it
2. Open it using a Python IDE such as Spyder. 
3. Run the software 

## Key Learnings and Known Issues

They key challenge in producing this software was to incorporate all the elements of the activities of the module in a clean and precise manner with a logical flow. 

The testing of the GUI was not possible due to the presence of a bug. The iPython console displayed 'Trying to connect to kernel' and then freeze when the backend was set to Tkinter. Subsequently, a GUI was not built to interact with the user. The software interacts with the user through the iPython console. 

The matplotlib functions was observed to only execute if the program has been terminated. It was not possible to display the data and then go back to the program. Resources such as [1], and [2] were consulted to mitigate this problem. However, no clear solution to the issue at hand was available.

[1]: https://stackoverflow.com/questions/458209/is-there-a-way-to-detach-matplotlib-plots-so-that-the-computation-can-continue
[2]: https://stackoverflow.com/questions/17149646/matplotlib-force-plot-display-and-then-return-to-main-code

## Further Development 
The software will be further developed to fix the known issues and incorporate more functionalities. The next version of the software will:

1. Allow the user to interact with the software using a GUI.
2. Add complexity to the environment by adding predator agents.
3. Change the dynamic of the agents based on how much they have in their store.

## Copyright
This project is licensed under the terms of the MIT license. 
