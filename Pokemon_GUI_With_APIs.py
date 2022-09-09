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
from tkinter import ttk

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


def pokeballs_given():
    def get_beeminder_focusmate_goal():
        pyminder = Pyminder(user=config.get("beeminder_credentials","first_name"), token=config.get("beeminder_credentials","token"))
        goals = pyminder.get_goals()
        goal = goals[0]
        return goal
    
    def get_sessions_done_today(goal):
        today = time.time()
        yesterday= time.time() - 70000
        total_sessions_as_of_today = goal.get_data_sum(today)
        total_sessions_as_of_yesterday = goal.get_data_sum(yesterday)
        sessions_done_today = total_sessions_as_of_today - total_sessions_as_of_yesterday 
        #What would be more simple is just getting the data session done today instead
        #of calculating the totals
        print(f"{sessions_done_today} sessions done today!")
        return sessions_done_today

    goal = get_beeminder_focusmate_goal()
    sessions_done_today = get_sessions_done_today(goal)
    
    balls_list = [10,10] #I'll add more balls later
    global balls
    if sessions_done_today > 0:
        balls = balls_list[0]

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
            CC_path = r"C:\Users\username_here\Downloads\ClusterColor_win64\ClusterColor_v1.0_win64\ClusterColor.exe"
            launch_CC =subprocess.Popen(CC_path)
            pyperclip.copy(pokemon_path)

        def catch():
            global balls_thrown
            balls_thrown = balls_thrown + 1
            
            remaining_balls_label.configure(text=f"{balls - int(balls_thrown)}x")
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
        self.img_pokeball1 = tk.PhotoImage(file=GUI_path_base / "pokeball (1).png")
        ball_label.configure(
            compound="center",
            font="{Arial Narrow} 12 {bold}",
            foreground="#fb5846",
            image=self.img_pokeball1,
        )
        ball_label.pack(expand="true", padx=20, side="top")

        remaining_balls_label = ttk.Label(self.button_frame)
        remaining_balls_label.configure(text=f"{balls - int(balls_thrown)}x")
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

class upload_imgur():
    def __init__(self):
        print("Uploading to Imgur...")
        client_id = config.get("imgur_credentials","client_id")
        client_secret = config.get("imgur_credentials", "client_secret")

        imgur_username = config.get("imgur_credentials","imgur_username")
        imgur_password = config.get("imgur_credentials","imgur_password")

        self.client = ImgurClient(client_id,client_secret)
        authorization_url = self.client.get_auth_url('pin')
        print("Authenticating...")
        def get_authorization_pin():
            driver = webdriver.Chrome(GUI_path_base / "chromedriver.exe")
            driver.get(authorization_url)
            username = driver.find_element("name","username")
            password = driver.find_element("name", "password" )
            allow = driver.find_element("name", "allow")
            username.send_keys(imgur_username)
            password.send_keys(imgur_password)
            time.sleep(1)
            allow.click()
            time.sleep(1)

            timeout = 5 
            try:
                element_present = EC.presence_of_element_located((By.ID,"pin"))
                WebDriverWait(driver,timeout).until(element_present)
                pin_element = driver.find_element("id",'pin')
                pin = pin_element.get_attribute("value")

            except TimeoutException:
                print("waited to long")
                driver.close
            return pin

        pin = get_authorization_pin()

        credentials = self.client.authorize(pin, 'pin')
        self.client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
        print("Authentication Successful!")

    def upload_image(self,nickname):

        album_id = self.client.get_account_album_ids("hightierhuman")
        image_path = image_path_base / f"recolors\{nickname}.png"

        album_id = self.client.get_account_album_ids("hightierhuman")

        pc_box = album_id[0]
        config = {
            "album": pc_box,
            "name" : f"{pokemon_name}",#pokemon_name
            "title" : f"{nickname}",#nickname
            "description": "uploaded"
        }
        upload = self.client.upload_from_path(image_path,config = config, anon=False)
        link_for_uploaded_image = upload["link"]
        print("Image uploaded to Imgur!")
        return link_for_uploaded_image 


    def PCBOX(self,link_for_uploaded_image):
        token = config.get("notion_credentials","token")

        payload = {
            'parent': {'database_id': config.get("notion_credentials","database_id")},       
            'properties': {
                        'Name': {
                                'title': [{"text":{"content":f"{nicknamelist[0]}"}}],
                                },
                        'Pokemon': {
                                    'rich_text': [{"text":{"content":f"{pokemon_name}"}}]},
                        "Date Caught":{
                            "date": {
                                "start":"2021-05-11T11:00:00.000-04:00"}}
                            },
            'cover':{
                    "type": "external",
                    "external":{"url": f"{link_for_uploaded_image}"}
                    
        }
        }

        data = json.dumps(payload)

        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer "+ token,
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"}
        readurl = f"https://api.notion.com/v1/pages"
        response1 = requests.post(readurl, headers=headers,data=data)
        print(f"{nicknamelist[0]} has been sent to the PC BOX in Notion!")
        
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")
    
    image_path_base = Path(r"C:\Users\username_here\Documents\1Python\Pokemon_Game\Pokemon_Images\gen5")
    GUI_path_base = Path(r"C:\Users\username_here\Documents\1Python\Pokemon_Game\GUI_others")
    image =random.choice(os.listdir(image_path_base))
    pokemon_name = image.replace(".png","" )
    
    balls_thrown = 0

    pokeballs_given()
    root = windows()
    nicknamelist = []
    root.mainloop()

    imgur = upload_imgur()
    link_for_uploaded_image = imgur.upload_image(nicknamelist[0])
    imgur.PCBOX(link_for_uploaded_image)


