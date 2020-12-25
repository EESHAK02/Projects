# This is a sample Python script.
from tkinter import *          # tkinter library for GUI
import requests                # requests library to access the api content
from tkinter import messagebox   # messagebox to show city not available



key = '4a507357d087d54ac1b244b1f3eafd40'                                   # apikey to be formatted in appid={} to access website
website = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'   # api website to access required data

def weather_report(city_name):
    suggestion_di_icon={}
    suggestion_di_temp={}
    # created dictionary for suggestions where key is temp condition/condition icon & value is suggestion

    finaldetails=requests.get(website.format(city_name, key))   # add city name and api key in brackets in website
    if finaldetails:
        json = finaldetails.json()
        # city,country,current temperature,max temperature,min temperature,weather,icon
        city_name=json['name']
        country_name=json['sys']['country']
        current_temp=json['main']['temp']
        current_temp_cel=(current_temp - 273.15)
        weather_condition=json['weather'][0]['description']
        status_icon=json['weather'][0]['icon']
        # adding suggestions for for temperature conditions or weather condition icons
        if (current_temp_cel)<11 and (current_temp_cel)>0:
            suggestion_di_temp['current_temp_cel']='Carry a sweater !'
        if (((current_temp_cel)>11) and ((current_temp_cel)<30)):
            suggestion_di_temp['current_temp_cel']='Good temperature !'
        if (current_temp_cel)<0:
            suggestion_di_temp['current_temp_cel']='Carry your snow guards !'
        if (current_temp_cel)>30 :
            suggestion_di_temp['current_temp_cel']='Carry a cap or a hat !'
        if ((status_icon=='09d') or (status_icon=='09n') or (status_icon=='10d') or (status_icon=='10n')) :
            suggestion_di_icon['status_icon']='Carrying an umbrella is a must !'
        if ((status_icon=='04d') or (status_icon=='04n')):
            suggestion_di_icon['status_icon']='You may carry an umbrella !'
        if ((status_icon=='11d') or (status_icon=='11n')):
            suggestion_di_icon['status_icon']='PLease stay indoors !'
        if ((status_icon=='01d') or (status_icon=='01n')):
            suggestion_di_icon['status_icon']='Off you go!'
        if ((status_icon=='02d') or (status_icon=='02n')) :
            suggestion_di_icon['status_icon']='Enjoy the weather !'
        if ((status_icon=='13d') or (status_icon=='13n')) :
            suggestion_di_icon['status_icon']='Carry your snow guards !'
        if ((status_icon=='50d') or (status_icon=='50n')) :
            suggestion_di_icon['status_icon']='Cover nose and mouth !'
        report=(city_name, country_name, current_temp_cel, weather_condition, suggestion_di_icon, suggestion_di_temp,status_icon)
        return report

    else:
        return None


def search():
    city_name = enter_city.get()
    weather = weather_report(city_name)
    if weather:
        place['text']='{}, {}'.format(weather[0], weather[1])                    # format city in desired form
        condition['text'] = (weather[3])                                         # format weather condition
        temp['text'] = '{:.2f}°C'.format(weather[2])                             # format current temperature upto 2 decimals (:.2f)
        suggestioni['text']='{}'.format(weather[4]['status_icon'])              # format suggestion for particular weather condition
        suggestiont['text']='{}'.format(weather[5]['current_temp_cel'])         # format suggestion for particular temperature
        # icon_image['image']='weather_icon_images/{}.png'.format(weather[5])     # adding icon of weather condition

    else:
        messagebox.askretrycancel('Not available', 'Sorry! Try once more ?')


# main_screen
window=Tk()
window.geometry('600x500')                               # size of app window
window.title('Weather API Project')                      # title of app window
window['bg']='light green'                                     # set background color

# title_label
Label(window,text='WEATHER TODAY ?',bg='light green',fg='red',font='ComicSansMS 24 bold').pack()   # first major title

# adding image
img=PhotoImage(file="weatherimg.png")             # introductory image in png format
Label(window,image=img , bg='light green').pack()


# enter_city_name
enter_city=StringVar()
city_entry=Entry(window, textvariable=enter_city,width=18, bg='white', fg='black', font='Arial 13 bold').pack()      # user input

# search button
search_weather = Button(window, text='Search', width=10, bg='white', fg='black',font='Arial 12 bold', command=search).pack()       # add search button

# place label
place=Label(window, text='', fg='brown', bg='light green' , font='Helvetica 24 bold')            # city and country formatted
place.pack()

# condition label
condition=Label(window, text='', fg='red', bg='light green', font='Helvetica 18 bold')            # weather condition got from api
condition.pack()

# temp label
temp=Label(window, text='', fg='black', bg='light green', font='Arial 20 bold')                   # current temperature got from api
temp.pack()

# suggestioni label
suggestioni=Label(window, text='',fg='dark blue',bg='light green' , font='Helvetica 18 bold')            # suggestion given
suggestioni.pack()

# suggestiont label
suggestiont=Label(window, text='',fg='blue',bg='light green' , font='Helvetica 18 bold')            # suggestion given
suggestiont.pack()




window.mainloop()                                   # run the program
