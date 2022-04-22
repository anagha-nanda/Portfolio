'''
Created on Thu Apr 19

@author: Anaghananda Santhoshkumar

Model version: 1

"""
The following code presents the web scraping activity prescribed in the module 
GEO5003: Programming for Geographical Information Analysis to fulfil 
the requirements for Assignment 1: Online Portfolio.

'''
import requests
import bs4

#Using request library to get the webpage through a variable
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')

#To get the page
content = r.text

#Converts webpage into python object
soup = bs4.BeautifulSoup(content, 'html.parser')

##Getting elements of classes x and y
td_y = soup.find_all(attrs={"class" : "y"})
td_x = soup.find_all(attrs={"class" : "x"})


#Printing the x and y elements 
for i in td_y:
    print("y=", i.text.strip())
for j in td_x:
    print("x=", j.text.strip())
