time = int(input('Введите время в секундах:'))
hours = time // 3600
minutes = (time // 60) % 60
seconds = time % 60
print(f'чч: {hours} мм: {minutes} сс: {seconds}')
