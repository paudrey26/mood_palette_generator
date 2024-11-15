import seaborn as sns
import matplotlib.pyplot as plt
moods = {
    '1': ['#960505','#BB72FF','#ACB7C3','#2FFF00','#2F4B26'], 
    '2': ['#702E0D','#6610F2','#93A29B','#DCBF85','#DDD78D'], 
    '3': ['#634810', '#6610F2','#93A29B','#DCBF85','#DDD78D'],
    '4': ['#70680D'],
    '5': ['#0B5726'],
    '6': ['#0D6D70'],
    '7': ['#2B68A1'],
    '8': ['#8371DE'],
    '9': ['#8D6AE6'],
    '10':['#FCC0E6']
    }


try:
    user_mood = input('What is your mood currently on a scale from 1-10?: ')
except:
    print("Bruh that's not a number")

if user_mood in moods:
    colors=moods[user_mood]
else:
    print("Error not an option. Faulty input")
    colors=moods["1"]
    
sns.palplot(colors)
plt.title(f'{user_mood} Palette')
plt.show()
