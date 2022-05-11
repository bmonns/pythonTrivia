
from textwrap import indent
import requests

print("Please enter the number of trivia questions you'd like to see: ", end='')
num = input()

r = requests.get(f'https://opentdb.com/api.php?amount={num}')
content = r.json()['results']

listContent = []
number = 1
for i in content:
    listContent.append('\n'+ str(number) + '.\n' + "Question: " + i['question'] + '\n' + "Answer: " + i['correct_answer'] + '\n')
    number+=1

for i in listContent:
    print(i)