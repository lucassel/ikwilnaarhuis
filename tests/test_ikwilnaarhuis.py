import pytest,ikwilnaarhuis,datetime
from datetime import time
from datetime import date
from ikwilnaarhuis.cli import hello

@pytest.mark.cli
def test_time():
	uur = 9
	minuten = 0
	now = time(uur, minuten)
	enter = ikwilnaarhuis.cli.constructDate(uur, minuten)
	assert now == enter

def test_hour():
	uur = 9
	minuten = 0
	enter = ikwilnaarhuis.cli.constructDate(uur, minuten)
	assert enter.hour == 9

def test_minutes():
	uur = 9
	minuten = 59
	enter = ikwilnaarhuis.cli.constructDate(uur, minuten)
	assert enter.minute == 59

def test_leave():
	today = date.today()
	lunch = 60
	start = time(9,0)
	leave = (datetime.datetime.combine(today, start) + datetime.timedelta(minutes=lunch) + datetime.timedelta(hours=7, minutes=48)).time()
	leave_temp = ikwilnaarhuis.cli.calculateLeave(start, lunch)
	assert leave == leave_temp
	
