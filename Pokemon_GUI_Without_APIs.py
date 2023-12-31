#Frame test
import configparser
import imp
import json
import os
import pprint
import random
import shutil
import subprocess
import sys
import time
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser
from distutils.command.clean import clean
from email import header
from email.mime import image
from glob import glob
from http import client
from lib2to3.pgen2.token import NAME
from logging import root
from multiprocessing.connection import Client
from pathlib import Path
from re import X
from telnetlib import EC
from tkinter import EW, W, ttk
from typing import Counter
from unicodedata import name
from wsgiref import headers
from xml.dom.minidom import Element

import pyperclip
import requests
import selenium
from imgurpython import ImgurClient
from PIL import Image, ImageTk
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#what do I call this? root_window 
class root_window(tk.Tk): #Too vague of a noun
    def __init__(self):
        tk.Tk.__init__(self)

        self.wm_title("Test Application")
        self.frames = {}
        parent_frame = self.setup_parent_frame() #how come there isn't a self. prefix for parent_frame?
        self.setup_child_frames(parent_frame)
        self.raise_selected_child_frame(CaptureAttemptFrame)
        
    def setup_parent_frame(self):
        parent_frame = tk.Frame(self, height=10, width=10)
        parent_frame.pack(side="top", fill="both", expand=True)
        parent_frame.grid_rowconfigure(0, weight=1)
        parent_frame.grid_columnconfigure(0, weight=1)
        return parent_frame

    def setup_child_frames(self,parent_frame):
        for F in (CaptureAttemptFrame,CapturedPokemonFrame): #Capture_window? Is that too redundant?
            child_frame = F(parent_frame, self) #Creates an instance with the container being the parent
            self.frames[F] = child_frame
            child_frame.grid(row=0, column=0, sticky="nsew")

    def raise_selected_child_frame(self,child_frame): #Ideally, I would delete the older frame and replace with a newer one. But having them stacked together is part of my design.
        selected_frame = self.frames[child_frame]
        selected_frame.tkraise()
        


class CaptureAttemptFrame(tk.Frame):
    def __init__(self, parent, controller):
        # build ui
        tk.Frame.__init__(self,parent)

        self.controller = controller
        self.click_count = 0

        self.setup_pokemon_display_label()
        
        action_frame = self.setup_action_frame()

        self.setup_catch_button(action_frame)
        self.setup_pokeball_icon(action_frame)
        self.pokeball_counter_label = self.setup_pokeball_counter(action_frame)

    

    #todo pokemon_label
    def setup_pokemon_display_label(self):
        self.pokemon_image_path = tk.PhotoImage(file=image_directory /f"{chosen_pokemon_image_path}")
        pokemon_image_label = tk.Label(self)
        pokemon_image_label.configure(
        image=self.pokemon_image_path, height=196, width=196, relief="raised")
        pokemon_image_label.pack()


    def setup_action_frame(self):
        action_frame = ttk.Frame(self)
        action_frame.configure(cursor="arrow", height=100, width=200)
        action_frame.pack()
        return action_frame


    def setup_catch_button(self,action_frame):
        catch_button = tk.Button(action_frame)
        catch_button.configure(
            borderwidth=10, default="normal", font="TkDefaultFont", justify="right",state="normal", text="CATCH"
            , command= self.catch_pokemon
        )
        catch_button.pack(side="left")


    def setup_pokeball_icon(self,action_frame):
        pokeball_icon_label = ttk.Label(action_frame) #why is the label attached to the button_frame?
        self.pokeball_icon_path = tk.PhotoImage(file=image_directory / "pokeball_icon.png")
        pokeball_icon_label.configure(
            compound="center",
            font="{Arial Narrow} 12 {bold}",
            foreground="#fb5846",
            image=self.pokeball_icon_path,
        )
        pokeball_icon_label.pack(expand="true", padx=20, side="top")
    

    def setup_pokeball_counter(self,action_frame):
        pokeball_counter_label = ttk.Label(action_frame)
        pokeball_counter_label.configure(text=f"{10 - int(self.click_count)}x")
        pokeball_counter_label.pack(side="top")
        return pokeball_counter_label

    def open_ClusterColor_with_pokemon_image(self,image):
        pokemon_image_path = str(image_directory / f"{image}")
        ClusterColor_path = main_directory / "ClusterColor_v1.0_win64/ClusterColor.exe"
        launch_ClusterColor =subprocess.Popen(ClusterColor_path)
        pyperclip.copy(pokemon_image_path)

    def catch_pokemon(self):
        # click_count = click_count + 1

        catch_chance_int = random.randint(0,1)

        if catch_chance_int != 1:
            self.click_count +=1
            self.pokeball_counter_label.configure(text=f"{10 - int(self.click_count)}x")
            print("The pokemon broke out of the ball!")
        elif catch_chance_int == 1:
            print(f"Gotcha! {pokemon_name} was caught!")
            self.controller.raise_selected_child_frame(CapturedPokemonFrame)
            self.open_ClusterColor_with_pokemon_image(chosen_pokemon_image_path)

        elif click_count == 10:
            print("It ran away!")
            sys.exit()


class CapturedPokemonFrame(tk.Frame):
    def __init__(self,parent,controller):
        # build ui
        tk.Frame.__init__(self,parent)


    
        self.setup_pokemon_display_label

        nickname_frame = self.setup_nickname_frame()
        self.setup_capture_message(nickname_frame)
        self.setup_nickname_entry(nickname_frame)

    
    def setup_pokemon_display_label(self):
        self.pokemon_image_path = tk.PhotoImage(file=image_directory /f"{chosen_pokemon_image_path}")
        pokemon_image_label = tk.Label(self)
        pokemon_image_label.configure(
        image=self.pokemon_image_path, height=196, width=196, relief="raised")
        pokemon_image_label.pack()

    def setup_nickname_frame(self):
        nickname_frame = ttk.Frame(self)
        nickname_frame.configure(cursor="arrow", height=100, width=200)
        nickname_frame.pack()
        return nickname_frame

    def setup_capture_message(self,nickname_frame):
        capture_message = ttk.Label(nickname_frame)
        capture_message.configure(
            takefocus=False,
            text=f"{pokemon_name} has been caught! Change their color pallete then type their nickname here",
        )
        capture_message.pack(side="top")

    def setup_nickname_entry(self,nickname_frame):
        self.nickname = ttk.Entry(nickname_frame)
        self.nickname.pack(side="top")

    def rename(self):
        nickname = self.nickname.get()
        os.rename(image_directory / f"recolors\{pokemon_name}_Recolored.png",image_directory / f"recolors\{nickname}.png")
        print(f"Sending {nickname} to the PC BOX")
        nickname_list.append(nickname)
        root.destroy()

    def setup_rename_button(self,nickname_frame):
        confirm_rename = ttk.Button(self, command= self.rename)
        confirm_rename.pack()


        
if __name__ == "__main__":
    main_directory = Path(os.getcwd()) #this path is constant so I'm not calling it "current"
    image_directory = Path(main_directory / r"Pokemon_Images")

    chosen_pokemon_image_path =random.choice(os.listdir(image_directory)) # Distinguishes what kind of pokemon for discussion. Displayed_wild_pokemon_image is redundant.
    pokemon_name = chosen_pokemon_image_path.replace(".png","" )

    root = root_window()
    #todo what does look at imports, what does logging do and why import it as "root"?
    nickname_list = []
    #todo it's just one name. Array is a waste.
    root.mainloop()

