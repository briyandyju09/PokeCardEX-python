#Importing All packages
import pandas as pd#data manipulation
import requests#web scraping
from bs4 import BeautifulSoup#web scraping
from datetime import datetime#date and time
import time#sleep
import os#file management
import tkinter as tk#gui
from tkinter import filedialog#gui
from tqdm import tqdm #progress bar
import math#math
import openpyxl#excel
import pyfiglet#ascii art
from pyfiglet import Figlet
import re
from decimal import Decimal#decimal
from pokemontcgsdk import Card#pokemontcgsdk
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity
from pokemontcgsdk import RestClient

#Setting up the API

RestClient.configure('f1624ad8-1cf7-4ea2-b55c-b01122c54aaa')

#Defining the ASCII Art

def ascii():
    result = pyfiglet.figlet_format("PokeCardEX") 
    print(result) 

#Defining the input command

def input_com():
    x = input("Enter a command: ")
    if x == "help":
        print("Type 'help' to see this message again.")
        print("Type 'exit' to quit the program.")
        print("Type 'search' to search for a card.")
        print("Type 'set' to search for a set.")
        print("Type 'type' to search for a type.")
        print("Type 'supertype' to search for a supertype.")
        print("Type 'subtype' to search for a subtype.")
        print("Type 'rarity' to search for a rarity.")
        time.sleep(3)
        exit()

    elif "search" in x:
        card = input("Enter the name of the card you want to search for: ")
        card = Card.where(name=card)
        print(card)

    else:
        print("Invalid command. Type 'help' to see a list of commands.")
        time.sleep(3)
        exit()

#Running the functions
ascii()
input_com()