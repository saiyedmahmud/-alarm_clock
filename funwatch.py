import datetime
import time
import winsound


def ct():
    current_time = datetime.datetime.now()
    global hour
    global minuts
    global ap
    global sec
    hour = int(current_time.strftime("%I"))
    minuts = int(current_time.strftime("%M"))
    ap = current_time.strftime("%p")
    sec = int(current_time.strftime("%S"))
    return print(f"{hour}:{minuts}:{sec} {ap}")


alarm_dic = {}


def c_alarm():

    h = int(input("Hour: "))
    while True:
        if h > 12:
            print("Given Houre must be in 12H Formet, Try again! ")
            h = int(input("Hour: "))
        else:
            break

    m = int(input("Minute: "))
    while True:
        if m > 60:
            print("minutse shuld be in between 60, try again! ")
            m = int(input("Minute: "))
        else:
            break
    dn = input("AM/PM: ").upper()
    while True:
        if dn != "AM" and dn != "PM":
            print("choose AM/PM, try again! ")
            dn = input("AM/PM:").upper()
            print(dn)
        else:
            break

    alarm_dic.update({"ahour": h, "aminuts": m, "adn": dn})
    return alarm_dic


def play_alarm(dic):
    check_hour = dic.get("ahour")
    check_minute = dic.get("aminuts")
    check_dn = dic.get("adn")
    alarm_hour = hour
    alarm_minute = minuts
    alarm_sec = sec
    alarm_dn = ap
    fq = 1000
    dur = 1000
    if check_hour == alarm_hour and check_minute == alarm_minute and check_dn == alarm_dn and alarm_sec < 14:
        
        return print(winsound.Beep(fq, dur), "its time to say Alhamdulillah!")


while True:
    i = 0
    user = input("do you want to creat a alarm? (y/n)").lower()
    if user == "y":
        c_alarm()

    while i < 60:
        ct()
        time.sleep(1)
        play_alarm(alarm_dic)
        i += 1
