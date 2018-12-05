from playsound import playsound

def say_temp(temp):
    say = round(temp, 0)
    for i in range(36):
        cal_temp = i + 10
        if cal_temp == round(temp):
            playsound("speech/" + str(cal_temp) + "-degrees.mp3")
    

say_temp(34.378924)
