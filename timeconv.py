#!/usr/bin/python



import datetime


HM_D = ':'


def mm_to_hhmm(mm):
    if mm == '':
        return ''
    hours = int(mm)/60
    mins =  int(mm)%60
    return str(hours) + HM_D + str(mins).zfill(2)


def hhmm_to_mm(hhmm):
    hoursmins = hhmm.split(HM_D)
    hours = int(hoursmins[0])
    mins = int(hoursmins[1])
    return str(hours*60 + mins)

