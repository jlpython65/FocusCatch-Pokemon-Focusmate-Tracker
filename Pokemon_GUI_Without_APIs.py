#Frame test
from glob import glob
from logging import root
import os, random
from re import X
import shutil
import tkinter as tk
import tkinter.ttk as ttk
import random
from typing import Counter
import subprocess
import pyperclip

from email import header
import imp
import json
from wsgiref import headers
import requests
import pprint
import time
from pyminder.pyminder import Pyminder
import tkinter as tk
from tkinter import EW, W, ttk

from PIL import ImageTk, Image  

from distutils.command.clean import clean
from email.mime import image
import imp
from lib2to3.pgen2.token import NAME
from multiprocessing.connection import Client
from telnetlib import EC
from unicodedata import name
import webbrowser
from xml.dom.minidom import Element
import selenium
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from imgurpython import ImgurClient
import configparser

from http import client
import configparser
from imgurpython import ImgurClient

from pathlib import Path



class windows(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("Test Application")
        container = tk.Frame(self, height=10, width=10)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Encounter,Caught):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Encounter)

    def show_frame(self, cont): 
        frame = self.frames[cont]
        frame.tkraise()

class Encounter(tk.Frame):
    def __init__(self, parent, controller):
        # build ui
        tk.Frame.__init__(self,parent)

        self.img_POKEMON = tk.PhotoImage(file=image_path_base /f"{image}")
        pokemon_label = tk.Label(self)
        
        pokemon_label.configure(
        image=self.img_POKEMON, height=196, width=196, relief="raised")

        pokemon_label.pack()

        self.button_frame = ttk.Frame(self)
        self.button_frame.configure(cursor="arrow", height=100, width=200)
        self.button_frame.pack()
        
        def open_CC_with_pokemon_image(image):
            pokemon_path = str(image_path_base / f"{image}")
            CC_path = GUI_path_base / "ClusterColor_v1.0_win64/ClusterColor.exe"
            launch_CC =subprocess.Popen(CC_path)
            pyperclip.copy(pokemon_path)

        def catch():
            global balls_thrown
            balls_thrown = balls_thrown + 1
            
            remaining_balls_label.configure(text=f"{10 - int(balls_thrown)}x")
            catch = random.randint(0,10)
            if catch != 1:
                print("The pokemon broke out of the ball!")
            if catch == 1:
                print(f"Gotcha! {pokemon_name} was caught!")
                controller.show_frame(Caught)
                open_CC_with_pokemon_image(image)
            elif balls_thrown == 10:
                print("It ran away!")
                sys.exit()
                

        self.catch_button = tk.Button(self.button_frame)
        self.catch_button.configure(
            borderwidth=10, default="normal", font="TkDefaultFont", justify="right",state="normal", text="CATCH"
            , command= catch
        )
        self.catch_button.pack(side="left")

        ball_label = ttk.Label(self.button_frame)
        self.img_pokeball1 = tk.PhotoImage(file=image_path_base / "pokeball_icon.png")
        ball_label.configure(
            compound="center",
            font="{Arial Narrow} 12 {bold}",
            foreground="#fb5846",
            image=self.img_pokeball1,
        )
        ball_label.pack(expand="true", padx=20, side="top")

        remaining_balls_label = ttk.Label(self.button_frame)
        remaining_balls_label.configure(text=f"{10 - int(balls_thrown)}x")
        remaining_balls_label.pack(side="top")
        controller.show_frame

class Caught(tk.Frame):
    def __init__(self,parent,controller):
        # build ui
        tk.Frame.__init__(self,parent)

        self.img_POKEMON = tk.PhotoImage(file=image_path_base / f"{image}")
        pokemon_label = tk.Label(self)
        
        pokemon_label.configure(
        image=self.img_POKEMON, height=196, width=196, relief="raised")

        pokemon_label.pack()

        catch_message_frame = ttk.Frame(self)
        catch_message = ttk.Label(catch_message_frame)
        catch_message.configure(
            takefocus=False,
            text=f"{pokemon_name} has been caught! Change their color pallete then type their nickname here",
        )
        catch_message.pack(side="top")
        self.nickname = ttk.Entry(catch_message_frame)
        self.nickname.pack(side="top")
        catch_message_frame.configure(cursor="arrow", height=100, width=200)
        catch_message_frame.pack()


        def rename():
            nickname = self.nickname.get()
            os.rename(image_path_base / f"recolors\{pokemon_name}_Recolored.png",image_path_base / f"recolors\{nickname}.png")
            print(f"Sending {nickname} to the PC BOX")
            nicknamelist.append(nickname)
            root.destroy()

        
        confirm_rename = ttk.Button(self, command= rename)
        confirm_rename.pack()

        
if __name__ == "__main__":
    GUI_path_base = Path(os.getcwd())
    image_path_base = Path(GUI_path_base / r"Pokemon_Images")

    image =random.choice(os.listdir(image_path_base))
    pokemon_name = image.replace(".png","" )
    
    balls_thrown = 0

    root = windows()
    nicknamelist = []
    root.mainloop()

