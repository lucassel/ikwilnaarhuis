import argparse, datetime
from datetime import time
from datetime import date

today = date.today()
hour = 8
minutes = 0

due_minutes = 468


def constructDate(uur, minuten):
		enter = time(hour,minutes)
		return enter


def calculateLeave(enter):
		leave = (datetime.datetime.combine(today, enter) + datetime.timedelta(hours=9, minutes=46)).time()
		return leave
 

def main():

  parser = argparse.ArgumentParser(description="IK WIL NAAR HUIS")
  parser.add_argument('time', metavar='T', type=int, help='the time you started working in hours')
  parser.add_argument("-P", "--pauze", type=int, required=False,  dest="break", help="Enter your lunch break in minutes.")


  args = parser.parse_args()

  # first integer is always interpreted as an hour
  # second integer is always interpreted as minutes
  # if not second integer, we use minutes = 0
  # 
  # -P is optional parameter for specifing your lunch break duration, 60 minutes default. 
  
  hour = args.time
  #print("you entered {} : {} as your starting hour".format(hour, minutes))
  #print("you have to work {} minutes daily".format(due_minutes))
  enter = constructDate(hour, minutes)
  leave = calculateLeave(enter)
  print("You are allowed to leave at " + leave.strftime("%H:%M" + " my nigga"))

  # if no break time specified, run with a standard break time of 60 minutes.
  # inform user when they don't enter a lunch break duration.


  #print(os.getcwd())


if __name__ == "__main__":
  main()