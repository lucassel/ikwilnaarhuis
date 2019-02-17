import pytest
import ikwilnaarhuis
import datetime
from datetime import time
from datetime import date
from ikwilnaarhuis.cli import constructDate, calculateLeave, process_input


@pytest.mark.cli
def test_time():
    uur = 9
    minuten = 0
    now = time(uur, minuten)
    enter = constructDate(uur, minuten)
    assert now == enter


def test_hour():
    uur = 9
    minuten = 0
    enter = constructDate(uur, minuten)
    assert enter.hour == 9


def test_minutes():
    uur = 9
    minuten = 59
    enter = constructDate(uur, minuten)
    assert enter.minute == 59


def test_leave():
    today = date.today()
    lunch = 60
    start = time(9, 0)
    leave = (datetime.datetime.combine(today, start) + datetime.timedelta(
        minutes=lunch) + datetime.timedelta(hours=7, minutes=48)).time()
    leave_temp = calculateLeave(start, lunch)
    assert leave == leave_temp


def test_version_print():
    input = ['-v']
    parser = process_input(input)
    namespace = parser.parse_args(input)
    assert(namespace.version != False)


def test_milestone_print():
    input = ['-m']
    parser = process_input(input)
    namespace = parser.parse_args(input)
    assert(namespace.milestones != False)


def test_parse_time_hours():
    input = ['-t', '9']
    parser = process_input(input)
    namespace = parser.parse_args(input)
    assert(namespace.time != False)
    assert(namespace.time[0] == 9)


def test_parse_time_minutes():
    input = ['-t', '9', '15']
    parser = process_input(input)
    namespace = parser.parse_args(input)
    assert(namespace.time != False)
    assert(namespace.time[0] == 9)
    assert(namespace.time[1] == 15)


def test_parse_hours():
    input = ['9']
    parser = process_input(input)
    namespace = parser.parse_args(input)
    assert(namespace.integers != False)
    assert(namespace.integers[0] == 9)


def test_parse_minutes():
    input = ['9', '15']
    parser = process_input(input)
    namespace = parser.parse_args(input)
    assert(namespace.integers != False)
    assert(namespace.integers[0] == 9)
    assert(namespace.integers[1] == 15)
