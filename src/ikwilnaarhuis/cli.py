# -*- coding: utf-8 -*-
import argparse
import calendar
import datetime
import getpass
import sys
from datetime import date, time
from pyfiglet import Figlet

import colorama
import pkg_resources  # part of setuptools
from pyinsults import insults
from termcolor import colored

today = date.today()


def constructDate(uur, minuten):
    enter = time(uur, minuten)
    return enter


def calculateLeave(enter, lunch):
    leave = (datetime.datetime.combine(today, enter) + datetime.timedelta(hours=7,
                                                                          minutes=48) + datetime.timedelta(minutes=lunch)).time()
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

    print(colored("*** MILESTONES ***", 'magenta'))
    print(colored("It's been {} days since you've started working at In The Pocket, that's about {} months! 👏".format(
        delta.days, days2months(delta.days)), 'cyan'))
    print("You've got {} days left till your work anniversary. 🎉".format(
        anniversary.days))
    print("You've been banging that sweet ass for {} days, that's about {} months 🍑".format(
        gurl.days, days2months(gurl.days)))


def daycheck(weekday):
    if weekday > 4:
        print(colored(
            "Um, why the fuck are you running 'ikwilnaarhuis' in the weekend??? 🤷‍♂️🤷‍♀️ \n", 'yellow'))
    else:
        greeting = "Happy {}, {}! 👋".format(
            calendar.day_name[today.weekday()], getpass.getuser())
        print(colored(greeting, 'cyan'))


def process_input(args):

    # we got some --parameters allright
    parser = argparse.ArgumentParser(
        description="IK WIL NAAR HUIS, a CLI command line project for people that think IKWILNAARHUIS (a lot). This project is a testbed for cross platform Python software development and deployment, utilising practices as unit testing, code coverage, continous deployment.")

    parser.add_argument('integers', type=int, nargs='*',
                        help="Default behaviour, run 'ikwilnaarhuis 9 15' to start your day at 9:15. Optionally, just run 'ikwilnaarhuis' to start your day at the script's runtime.", default=[])
    parser.add_argument('-t', '--time', nargs="+", type=int,
                        help='Use -t or --time to strictly input time, completely optional.')
    parser.add_argument("-l", "--lunch", type=int, required=False,
                        help="Use -l or --lunch to enter a lunch break in minutes.")
    parser.add_argument(
        '-m', '--milestones', help="Use -m or --milestones to print out various milestones", action='store_true')
    parser.add_argument('-v', '--version',
                        help="Use -v or --version to print out 'ikwilnaarhuis' latest installed version", action='store_true')
    parser.add_argument('-r', '--reverse', type=int, required=False, nargs='+')
    return parser


def main():

    colorama.init()

    custom_fig = Figlet(font='standard')
    print(custom_fig.renderText('ikwilnaarhuis'))

    now = datetime.datetime.now()
    lunch = 60
    input = sys.argv[1:]
    parser = process_input(input)
    namespace = parser.parse_args(input)
    args = parser.parse_args()

    if namespace.version:
        version = pkg_resources.require("ikwilnaarhuis")[0].version
        print("ikwilnaarhuis --version: {}".format(version))
        return

    if namespace.milestones:
        milestones()
        return

    daycheck(today.weekday())

    if namespace.lunch:
        print(
            colored("🍽 Specified --lunch break of {} minutes".format(args.lunch), 'blue'))
        lunch = args.lunch

    else:
        print(colored(
            "🍽 No --lunch specified, using default of {} minutes!".format(lunch), 'yellow'))

    if namespace.reverse:
        leave_hour = args.reverse[0]
        try:
            leave_minutes = args.reverse[1]
        except:
            leave_minutes = 0
        print(f"you wanne leave at {leave_hour}:{leave_minutes}")
        dt = constructDate(leave_hour, leave_minutes)

        leave = (datetime.datetime.combine(today, dt) - datetime.timedelta(hours=7,
                                                                           minutes=48) - datetime.timedelta(minutes=lunch)).time()
        print(f"You betterr workkkk at {leave}")

    else:
        if namespace.integers:
            start_hour = args.integers[0]
            try:
                start_minutes = args.integers[1]
            except:
                start_minutes = 0

            print(colored("⏰ Specified starting time: {}:{}".format(
                start_hour, start_minutes), 'blue'))

        elif namespace.time:
            start_hour = args.time[0]
            try:
                start_minutes = args.time[1]
            except:
                start_minutes = 0

            print(colored(
                "⏰ Specified starting --time: {}:{}".format(start_hour, start_minutes), 'blue'))

        else:
            start_hour = now.hour
            start_minutes = now.minute
            print(colored(
                "⚠ You executed 'ikwilnaarhuis' without specifying a time, using current time!", 'yellow'))

        print("\n")
        print(colored("⏰ Your starting time is {} : {}.".format(
            start_hour, str(start_minutes).zfill(2)), 'cyan'))

        enter = constructDate(start_hour, start_minutes)
        leave = calculateLeave(enter, lunch)

        print(colored("You are allowed to leave at " + leave.strftime("%H:%M") +
                      ", you " + insults.long_insult() + ". 😍", 'green'))


if __name__ == "__main__":
    main()
