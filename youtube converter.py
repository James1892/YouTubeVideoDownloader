#!/usr/bin/env python3

from rich.progress import track
from pytube import YouTube
from rich import print
import os.path
import time
import sys
import os


def videoProgreesBar():
    for i in track(range(10), description="Downloading"):
        time.sleep(.4) 

def audioprogressbar():
    for i in track(range(5), description="Downloading"):
        time.sleep(.2)


def mainMenu():
    os.system("cls")
    while True:
        print("""[red]
     __   __         _____      _             ____                          _            
     \ \ / /__  _   |_   _|   _| |__   ___   / ___|___  _ ____   _____ _ __| |_ ___ _ __ 
      \ V / _ \| | | || || | | | '_ \ / _ \ | |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
       | | (_) | |_| || || |_| | |_) |  __/ | |__| (_) | | | \ V /  __/ |  | ||  __/ |   
       |_|\___/ \__,_||_| \__,_|_.__/ \___|  \____\___/|_| |_|\_/ \___|_|   \__\___|_|v1 [/red]""",
       "By James Perry" )

        print("=======================================")
        print("option:")
        print("   1) MP3")
        print("   2) MP4")
        print("   99) Exit")
        print("========================================")

        option = input("option: ")
        
        if option == "1":
            mpThree()
        elif option == "2":
            mpFour()
        elif option == "99":
            sys.exit()
        try:
            option
        except KeyError:
            break


def mpThree():
    os.system("cls")
    print(""" [magenta]
 __  __ ____ _____ 
|  \/  |  _ |___ / 
| |\/| | |_) ||_ \ 
| |  | |  __/___) |
|_|  |_|_|  |____/ 
                  [/magenta] """)
    while True:
        try:
            url = input("Enter url of the mp3 file you want to download \n>> ")  # Youtube url input
            video = YouTube(url)
            print(video.title)  # Displays the video title
            audio = video.streams.filter(only_audio=True).first()  # Grabs only the audio
        except:
            print(f"[bold red]{url} invalid url[/bold red]")
            url
        else:
            while True:
                location = input("Save to directory \n>> ")
                if os.path.exists(location) == False:
                    print(f"[bold red]{location} does not exist[/bold red]\n")
                    location


                elif os.path.exists(location) == True:
                    saveFile = audio.download(output_path = location)  # Gets the location the downloads the audio
                    base, ext = os.path.splitext(saveFile)
                    newFile = base + ".mp3"  # Changes the extentionof the file
                    os.rename(saveFile, newFile)  # Renames the file

                    audioprogressbar()  # rogress bar
                    print(f"[bold green]{video.title} has successfully downloaded.[/bold green]")
                    while True:
                        print("=======================================")
                        print("option:")
                        print("   1) mp3")
                        print("   2) Main Menu")
                        print("   99) Exit")
                        print("========================================")
                        option = input(">> ")
                        if option == "1":
                            mpThree()
                        elif option == "2":
                            mainMenu()
                        elif option == "99":
                            sys.exit()
                        try:
                            option
                        except KeyError:
                            break
            
     
def mpFour():
    os.system("cls")
    print(""" [yellow]
 ____    ____  _______   _    _    
|_   \  /   _||_   __ \ | |  | |   
  |   \/   |    | |__) || |__| |_  
  | |\  /| |    |  ___/ |____   _| 
 _| |_\/_| |_  _| |_        _| |_  
|_____||_____||_____|      |_____| [/yellow]""")
    
    while True:
        try:
            url = input("Enter url for the mp4 file you want to download \n>> ")
            video = YouTube(url)
            print(video.title)
            download = video.streams.get_highest_resolution()
        except:
            print(f"[bold red]{url} does not exist[/bold red]\n")
            url
        else:
            while True:
                location = input("Save to directory \n>> ")
                if os.path.exists(location) == False:
                    print(f"[bold red]{location} does not exist[/bold red]\n")
                    location


                elif os.path.exists(location) == True:
                    saveFile = download.download(output_path = location)  # Gets the location the downloads the audio
                    base, ext = os.path.splitext(saveFile)
                    newFile = base + ".mp4"  # Changes the extentionof the file
                    os.rename(saveFile, newFile)  # Renames the file

                    videoProgreesBar()  # rogress bar
                    print(f"[bold green]{video.title} has successfully downloaded.[/bold green]")
                    while True:
                        print("=======================================")
                        print("option:")
                        print("   1) mp4")
                        print("   2) Main Menu")
                        print("   99) Exit")
                        print("========================================")
                        option = input(">> ")
                        if option == "1":
                            mpFour()
                        elif option == "2":
                            mainMenu()
                        elif option == "99":
                            sys.exit()
                        try:
                            option
                        except KeyError:
                            break
            

mainMenu()