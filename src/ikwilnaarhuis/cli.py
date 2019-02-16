# -*- coding: utf-8 -*-
import argparse
import datetime
import calendar
import getpass
import sys
from datetime import time
from datetime import date
from pyinsults import insults
import colorama
from termcolor import colored



today = date.today()

def constructDate(uur, minuten):
    enter = time(uur, minuten)
    return enter

def calculateLeave(enter, lunch):
    leave = (datetime.datetime.combine(today, enter) + datetime.timedelta(hours=7, minutes=48) + datetime.timedelta(minutes=lunch)).time()
    return leave

def days2months(days):
    return days/30

def milestones():
    first_day = datetime.date(2018, 6, 11)
    amelie = datetime.date(2018, 8, 25)
    one_year = datetime.date(2019, 6, 11)

    delta = today - first_day
    anniversary = one_year - today
    gurl = today - amelie
    print("\n")
    print(colored("*** MILESTONES ***", 'green'))
    print(colored("You've worked at In The Pocket for {} days ({} months)! 👏".format(delta.days, days2months(delta.days)), 'cyan'))
    print(colored("You've got {} days left till your work anniversary. 🎉".format(anniversary.days), 'cyan'))
    print("\n")
    print(colored("You've been banging that sweet 🍑 for {} days! 💞".format(gurl.days), 'magenta'))
    print(colored("That's about {} months already. 🐎".format(days2months(gurl.days)), 'magenta'))
    print("\n")

def daycheck(weekday):
    if weekday > 4:
        print(colored("Um, why the fuck are you running 'ikwilnaarhuis' in the weekend??? 🤷‍♂️🤷‍♀️ \n", 'yellow'))
    else:
        greeting = "Happy {}, {}! 👋".format(calendar.day_name[today.weekday()], getpass.getuser())
        print(colored(greeting, 'cyan'))


def main():

    colorama.init()
    now = datetime.datetime.now()
    lunch = 60    
    daycheck(today.weekday())

    # we got some --parameters allright
    parser = argparse.ArgumentParser(description="IK WIL NAAR HUIS, a CLI command line project for people that think IKWILNAARHUIS (a lot).")

    parser.add_argument('integers', metavar='N', type=int, nargs='*', help='Time input without --time flag.', default = [])
    parser.add_argument('-t', '--time', nargs="+", metavar='T', type=int, help='The time you started working in hours, optional')
    parser.add_argument("-l", "--lunch", metavar='L', type=int, required=False, dest="lunch", help="Enter your lunch break in minutes.")
    parser.add_argument('-m', '--milestones', help="print milestones", action='store_true')
    
    namespace = parser.parse_args(sys.argv[1:])
    args = parser.parse_args()

    if namespace.integers:
      start_hour = args.integers[0]
      try:
          start_minutes = args.integers[1]
      except:
          start_minutes = 0

      print(colored("⏰ Specified starting time: {}:{}".format(start_hour, start_minutes), 'blue'))


    elif namespace.time:
      start_hour = args.time[0]
      try:
          start_minutes = args.time[1]
      except:
          start_minutes = 0

      print(colored("⏰ Specified starting --time: {}:{}".format(start_hour, start_minutes), 'blue'))

    else: 
      start_hour = now.hour
      start_minutes = now.minute
      print(colored("⚠ You executed 'ikwilnaarhuis' without specifying a time, using current time!", 'yellow'))

    if namespace.lunch:
        print(colored("🍽 Specified --lunch break of {} minutes".format(args.lunch), 'blue'))
        lunch = args.lunch

    else:
        print(colored("🍽 No --lunch specified, using default of {} minutes!".format(lunch), 'yellow'))

    print("\n")
    print(colored("⏰ Your starting time is {} : {}.".format(start_hour, str(start_minutes).zfill(2)), 'cyan'))

    enter = constructDate(start_hour, start_minutes)
    leave = calculateLeave(enter, lunch)

    print(colored("You are allowed to leave at " + leave.strftime("%H:%M") + ", you " + insults.long_insult() + ". 😍", 'green'))

    if namespace.milestones:
        milestones()


if __name__ == "__main__":
    main()
