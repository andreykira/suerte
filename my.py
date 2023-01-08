https://colab.research.google.com/drive/1vkc9lJhFHspzY2tAMHIANr6eNzsreb6D

# Введите данные:
cd /content/drive/MyDrive/Colab Notebooks

import pandas as pd
import cred
info = pd.read_csv('info.csv', index_col='currency')

# Получите Данные по акциям от alphavantage:
def get_data(token):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={token}&interval={time}&apikey={cred.API_KEY}&datatype=csv'
    return pd.read_csv(url)

from numpy.core.fromnumeric import mean
# Сравниваем FastSMA и SlowSMA
def get_useful_data(df):
  fast_7 = mean(df['close'][0:7])
  slow_25 = mean(df['close'][0:25])
  if fast_7 > slow_25:
    num = 1
  else:
    num = 0
  return num 

# Конечная функция принятия решения о покупке или продаже
def trader(curr):
  df = get_data(curr)
  num = get_useful_data(df)
  if info['position'][curr] != num:
    if num == 1:
      print(f'Для {curr}. Быстрая скользящая пересекла среднюю снизу вверх, КУПИТЬ!')
    else:
      print(f'Для {curr}. Быстрая скользящая пересекла среднюю сверху вниз, ПРОДАВАТЬ!')
    info['position'][curr] = num
  elif num == 1:
    print(f'Пока не продавать {curr}')
  elif num == 0:
    print(f'Пока не покупать {curr}')
  return info

# Проверка
for curr in info.index:
  trader(curr)
print (info)





