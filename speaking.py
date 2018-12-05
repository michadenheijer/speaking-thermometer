from playsound import playsound

def say_temp(temp):
    say = round(temp, 0)
    if temp > 45:
        playsound("speech/warm.mp3")
        return
    elif temp < 10:
        playsound("speech/cold.mp3")
        return
    else:
        for i in range(36):
            cal_temp = i + 10
            if cal_temp == round(temp):
                playsound("speech/" + str(cal_temp) + "-degrees.mp3")
                return
