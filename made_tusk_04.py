my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
time = 0
x = 0
while x < 3:
  import random
  k = random.randint(0,len(my_favorite_songs) - 1)
  time += my_favorite_songs[k][1]
  my_favorite_songs.remove(my_favorite_songs[k])
  x += 1
print(f"Три песни звучат {time} минут")
