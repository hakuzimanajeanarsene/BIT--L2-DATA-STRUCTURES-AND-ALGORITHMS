from array import array
#we are going to create array of scores for Tournament Scoreboard

#Task 1 Intergers
scores = [78, 92, 85, 60, 99]  # Example scores for 5 players
score_sum = sum(scores) 
score_avg = score_sum / len(scores) 
score_min = min(scores) 
score_max = max(scores) 

print("sum:", score_sum)
print("average:", score_avg)
print("minimum:", score_min)
print("maximum:", score_max)

#Task 2 Strings

print(f"Tournament Scoreboard Total scores are {score_sum} and average is {score_avg}")

#Task 3 Booleans

threshold = 80
if score_avg >= threshold and score_max >= 90:
    print('Above Standard')
else:
    print('Below Standard')

#Task 4 Lists
players = ['arsen','patrick','shalom','sam-g','paterne']
print('players list before modification:', players)
players.append('john')
scores.append(98)
i = 0
for player in players:
    if scores[i] < threshold:
        del players[i]
        del scores[i]
    i = i + 1
print('players list after modification', players)
players.sort()
print('players after sort', players)

#Task 5 Array
# This array will store the ages of players
ages = array('i', [20,25,19,30])
total_age = sum(ages)
print('Total ages:', total_age)
# compare data 
total_scores_now = sum(scores)
print('compare total of array to list version: total_scores_now == total_age will be ', total_scores_now == total_age)

#Task 6 Dictionaries
#We are going to create dictional for players I'm thinking about football player

players_dictional = [
        {'id': 1, 'name' : 'patricke', 'score' : 92, 'age' : 20},
        {'id': 2, 'name' : 'shalom', 'score' : 85, 'age' : 25},
        {'id': 3, 'name' : 'paterne', 'score' : 99, 'age' : 19},
        {'id': 4, 'name' : 'john', 'score' : 98, 'age' : 3}
    ]
print('list of dictionals', players_dictional)
players_dictional[0]['name'] = 'patrick'
print('list of dictionals after update record on index 0', players_dictional)
del players_dictional[2]
print('list of dictionals after delete record on index 2', players_dictional)
sum_of_scores_in_list_of_dictionals = i = 0 
for player in players_dictional:
    sum_of_scores_in_list_of_dictionals = sum_of_scores_in_list_of_dictionals + player['score']
print('Sum of score in list of dictionals is :', sum_of_scores_in_list_of_dictionals)