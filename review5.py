songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key, value in zip(songs,playcounts)}
print(plays,'\n')
plays["Purple Haze"] = 1
print(plays,'\n')
plays["Respect"] = 94
print(plays,'\n')

library = {"The Best Songs": plays}
library["Sunday Feelings"] = {}
print(library,'\n')
