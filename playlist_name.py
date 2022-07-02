from datetime import datetime
import random

playlist_name = 'Test ' + datetime.today().strftime('%Y-%m-%d-%H-%M')
print(playlist_name)

upper_eng = "TEST"
number = "0123456789"
all_eng = upper_eng + number
lenght = 10
random_name = 'TEST' + "".join(random.sample(all_eng, lenght))
print(random_name)

fixture_playlist_name = 'FixtureTest' + datetime.today().strftime('%Y-%m-%d-%H-%M')