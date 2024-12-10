print('В команде %(team1)s участников: %(team1_num)s!' % {'team1':'Мастера кода', 'team1_num': 5})

team1_num = 5
team2_num = 6
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

#Использование format()
score_2 = 42
team2 = 'Волшебники данных'
print('Команда {} решила задач: {}!'.format(team2, score_2))
team1_time = 18015.2
print('{} решили задачи за {} c!'.format(team2, team1_time))

#Использование f-строк
score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач')


team2_time = 2153.31451

def sum_team():
    total = score_1 + score_2
    return total

def avg():
    sum_time = team1_time + team2_time
    total = sum_team()
    return round((sum_time / total), 1)

task_total = sum_team()
time_avg = avg()
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды на задачу!')

def win():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
        return result
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
        return result
    else:
        result = 'Ничья!'
        return result

challenge_result = win()
print(f'Результат битвы: {challenge_result}')