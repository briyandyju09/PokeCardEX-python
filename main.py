import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import os
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm #progress bar
import math
import openpyxl
import pyfiglet
from pyfiglet import Figlet
import re
from decimal import Decimal
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity
from pokemontcgsdk import RestClient

RestClient.configure('f1624ad8-1cf7-4ea2-b55c-b01122c54aaa')

def ascii():
    result = pyfiglet.figlet_format("PokeCardEX") 
    print(result) 

def input():
    input = input("Enter a command: ")

def print():
    if input == "help":
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

    elif input == "search":
        card = input("Enter the name of the card you want to search for: ")
        card = Card.where(name=card)
        print(card)

    else:
        print("Invalid command. Type 'help' to see a list of commands.")
        time.sleep(3)
        exit()

ascii()
input()
print()