from tkinter import *
import tkinter as tk
from datetime import datetime
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
import requests
from timezonefinder import TimezoneFinder
import pytz
from PIL import Image,ImageTk

root = Tk()
root.title("Weather App")
root.geometry("900x500")
root.configure(bg='#1E41D0')
root.resizable(False,False)

#search
def getweather():
    city=e1.get()
    geolocator = Nominatim(user_agent="geoapiExcercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%p")
    clock.config(text= current_time)
    name.config(text="Current Weather")

    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"
    json_data = requests.get(api).json()
    condition= json_data['weather'][0]['main']
    desciption= json_data['weather'][0]['description']
    temp= int(json_data['main']['temp']-273.15)
    pressure= json_data['main']['pressure']
    humidity= json_data['main']['humidity']
    wind= json_data['wind']['speed']

    label2.config(text=(temp,"'"))
    label21.config(text=(condition,"|","FEELS","LIKE",temp,"'"))
    w.config(text=(wind,"km/h"))
    h.config(text=(humidity,"%"))
    d.config(text=desciption)
    p.config(text=(pressure," mbar"))

Search_image = PhotoImage(file='Copy of search.png')
myimage = Label(image=Search_image,bg='#1E41D0')
myimage.place(x=20,y=20)

e1 = Entry(root,justify='center',width=17,font=('poppins',25,'bold'),fg="white",bg="#343836")
e1.place(x=50,y=40)
e1.focus()

search_icon = PhotoImage(file="Copy of search_icon.png")
myicon = Button(image=search_icon,cursor='hand2',bg='#404040',height=40,command=getweather)
myicon.place(x=390,y=37)


logo = PhotoImage(file="Copy of logo.png")
mylogo = Label(image=logo,bg="#1E41D0")
mylogo.place(x=300,y=90)


label2 = Label(root,font="times 70 bold ",fg="#ee666d",bg="#1E41D0")
label2.place(x=600,y=120)

label21 = Label(root,font="times 15 ",fg="white",bg="#1E41D0")
label21.place(x=600,y=230)

name = Label(root,font=("arial",15,'bold'),bg='#1E41D0',fg="white")
name.place(x=30,y=100)

clock = Label(root,font=("arial",13,'bold'),bg="#1E41D0",fg="white")
clock.place(x=30,y=130)

label1 = Label(bg="black",height=100,width=200)
label1.place(x=0,y=330)


label3 = Label(text = 'Wind',font="times 15 bold underline",fg="white",bg='black')
label3.place(x=80,y=350)
w = Label(text="....",font="times 12 bold ",justify='center',fg='light blue',bg='black')
w.place(x=80,y=380)

label3 = Label(text = 'Humidity',font="times 15 bold underline",fg="white",bg='black')
label3.place(x=240,y=350)
h = Label(text="....",font="times 12 bold ",justify='center',fg='light blue',bg='black')
h.place(x=240,y=380)

label3 = Label(text = 'Description',font="times 15 bold underline",fg="white",bg='black')
label3.place(x=480,y=350)
d = Label(text="....",justify='center',font="times 12 bold ",fg='light blue',bg='black')
d.place(x=480,y=380)

label3 = Label(text = 'Pressure',font="times 15 bold underline",fg="white",bg='black')
label3.place(x=720,y=350)
p = Label(text="....",justify='center',font="times 12 bold ",fg='light blue',bg='black')
p.place(x=720,y=380)




root.mainloop()