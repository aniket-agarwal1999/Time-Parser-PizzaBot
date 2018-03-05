import date_time_parsers
from date_time_parsers import *

import 

movie = {'black':0, 'panther':1, 'hate':2, 'story':3, 'deadpool':4, 'baaghi':5, 'avengers':6, 'infinity':7, 'war':8}

answers = {'y':0, 'yes':1, 'correct':2, 'right':3, 'awesome':4, 'alright':5, 'sahi':6, 'gazab':7, 'haan':8, 'ya':9, 'yeah':10}

format_of_movie = {'3D':0, '2D':1}

halls = {'PVR':0, 'M2K':1, 'RR':2, 'DT':3}

def movie_decider:
    print("Welcome to the gaming portal")
    print("Please tell the name of the movie you want to see: ")
    print("Black Panther")
    print("Avengers: Infinity War")
    print("Hate Story 4")
    print("Deadpool 2")
    choice = input()
    choice = choice.lower()
    choice_list = choice.split()

    i= 0
    ans = 'n'
    while ans not in answers:
        while i<len(choice_list):
            if choice_list[i] in movie:
                if choice_list[i] == 'black' or choice_list[i] == 'panther':
                    print("You have chosen to watch the movie Black Panther.")
                    print("Is that right?")
                    ans = input()
                    ans = ans.lower()

    print("In which cinema hall do you want to see the movie: ")
    print("PVR cinemas")
    print("M2K cinemas")
    print("RR cinemas")
    print("DT cinemas")
    hall_answer = input()
    hall_list = hall_answer.split()
    k=0
    while k<len(hall_list):
        if hall_list[k] in halls:
            print("Okay, so you have selected the movie format as: ",hall_list[k])
    
    print("In which format do you want to see the movie(3D/2D): ")
    form = input()
    form_list = form.split()
    j=0
    while j<len(form_list):
        if form_list[j] in format_of_movie:
            print("Okay, So you have chosen the format of the movie as ",form_list[j])

    print("At what time and  do you want to see the movie")
    date_time_parse()
    print("So this is the time and date you have booked the ticket for...")
    print("Thank you for using our porta for booking the ticket")
    print("The full ticket details are as follows: ")
