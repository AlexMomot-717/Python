time_in_sek = int(input('Ведите количество секунд: '))
hour = time_in_sek // 3600
if hour < 10:
    hour = '0' + str(hour)
minutes = (time_in_sek % 3600) // 60
if minutes < 10:
    minutes = '0' + str(minutes)
sek = time_in_sek % 60
if sek  < 10:
    sek  = '0' + str(sek)
print(str(hour) + ':' + str(minutes) + ':' + str(sek))