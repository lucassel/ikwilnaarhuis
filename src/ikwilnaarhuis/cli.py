# -*- coding: utf-8 -*-
import argparse, datetime
import calendar
import getpass
import sys
from datetime import time
from datetime import date
from pyinsults import insults
import colorama
from termcolor import colored

colorama.init()

today = date.today()

def hello():
    return "he"

def constructDate(uur, minuten):
		enter = time(uur,minuten)
		return enter

def calculateLeave(enter, lunch):
		leave = (datetime.datetime.combine(today, enter) + datetime.timedelta(hours=7, minutes=48) + datetime.timedelta(minutes = lunch)).time()
		return leave

def days2months(days):
    return days/30

def milestones():
  first_day = datetime.date(2018, 6, 11)
  amelie = datetime.date(2018,8,25)
  one_year = datetime.date(2019,6,11)
  
  delta = today - first_day
  anniversary = one_year - today
  gurl = today - amelie

  print("It's been {} days since you've started working at In The Pocket, that's about {} months! 👏".format(delta.days, days2months(delta.days)))
  print("You've got {} days left till your work anniversary. 🎉".format(anniversary.days))
  print("You've been banging that sweet ass for {} days, that's about {} months 🍑".format(gurl.days, days2months(gurl.days)))
  print("\n")



def main():
  now = datetime.datetime.now()
  lunch = 60
  # TODO implement weekdays
  greeting = "Happy {}, {}! 👋".format(calendar.day_name[today.weekday()], getpass.getuser())
  print(colored(greeting, 'green'))

  parser = argparse.ArgumentParser(description="IK WIL NAAR HUIS, a CLI command line project for people that think IKWILNAARHUIS a lot")
  parser.add_argument('-t', '--time', nargs="+", metavar='T', type=int, help='the time you started working in hours, optional')
  parser.add_argument("-l", "--lunch", metavar='L', type=int, required=False,  dest="lunch", help="Enter your lunch break in minutes.")
  parser.add_argument('-m', '--milestones', help="print milestones", action='store_true')

  namespace = parser.parse_args(sys.argv[1:])
  if namespace.milestones:
    milestones()

  args = parser.parse_args()
  #  Switch to namespace
  #  if statements suck.
  # if run with no integers then we use the script execution time as starting moment of the day
  if args.time == None:
    start_hour = now.hour
    start_minutes = now.minute
    print("⚠ Script executed without specified time, using ==> {}:{}.".format(now.hour, now.minute))

  else:
    start_hour = args.time[0]
    try: 
      start_minutes = args.time[1]
    except:
      start_minutes = 0
    # try to parse an hour out of two integers
    # first integer is always interpreted as an hour
    # second integer is always interpreted as minutes
    # if not second integer, we use minutes = 0


    # TODO testing issues

    # -l or --lunch is optional parameter for specifing your lunch break duration, 60 minutes default. 
  
  print("⏰ Your starting time is {} : {}.".format(start_hour, str(start_minutes).zfill(2)))

  if args.lunch == None:
    print("🍽 No --lunch specified, using default of {} minutes!".format(lunch))  
  
  else:
    print("🍽 Specified --lunch break of {} minutes".format(args.lunch))
    lunch = args.lunch
    

  enter = constructDate(start_hour, start_minutes)
  leave = calculateLeave(enter, lunch)
  
  print("You are allowed to leave at " + leave.strftime("%H:%M") + ", you " + insults.long_insult() + ". 😍")

if __name__ == "__main__":
  main()