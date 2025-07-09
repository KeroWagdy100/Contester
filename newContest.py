# newContest.py
from getContestDetails import *

def newContest(contestLink):
    contestDetails = getContestDetails(contestLink)
    if not contestDetails:
        return False
    