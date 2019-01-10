import argparse, datetime
from datetime import time
from datetime import date

today = date.today()


due_minutes = 468


def constructDate(uur, minuten):
		enter = time(uur,minuten)
		return enter

def calculateLeave(enter):
		leave = (datetime.datetime.combine(today, enter) + datetime.timedelta(hours=9, minutes=48)).time()
		return leave

def main():
  now = datetime.datetime.now()
  parser = argparse.ArgumentParser(description="IK WIL NAAR HUIS")
  parser.add_argument('-t', '--time', nargs="+", metavar='T', type=int, help='the time you started working in hours, optional')
  parser.add_argument("-l", "--lunch", metavar='L', type=int, required=False,  dest="lunch", help="Enter your lunch break in minutes.")

  args = parser.parse_args()
  
  # if run with no integers then we use the script execution time as starting moment of the day
  if args.time == None:
    start_hour = now.hour
    start_minutes = now.minute
    print("ran script with no time input, using current time of {} : {} as your starting time".format(start_hour, start_minutes))
    

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

    # -l or --lunch is optional parameter for specifing your lunch break duration, 60 minutes default. 
  
  print("Your starting time is {} : {}".format(start_hour, str(start_minutes).zfill(2)))

  if args.lunch == None:
    print("default lunch break of 60 min")
    pass
  
  else:
    print("lunch break with user input {}".format(args.lunch))
    pass

  enter = constructDate(start_hour, start_minutes)
  
  leave = calculateLeave(enter)


  
  print("You are allowed to leave at " + leave.strftime("%H:%M" + " my nigga"))

  # if no break time specified, run with a standard break time of 60 minutes.
  # inform user when they don't enter a lunch break duration.



if __name__ == "__main__":
  main()