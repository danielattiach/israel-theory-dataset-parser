import re
import json
import requests
import xmltodict

response = requests.get('https://data.gov.il/dataset/618dd157-8df3-43e7-bf9a-00974b4919e9/'
                        'resource/8c0f314f-583d-48b6-9f5f-4483d95f6848/download/theoryexamhe_data_yellow.xml')
data = response.content.decode()
questions = [dict(q) for q in xmltodict.parse(data)['rss']['channel']['item']]

wrong_answer_regex = r'<span>([^<][\s\S]*?)<\/span>'
right_answer_regex = r'<span id=\"correctAnswer[0-9]{1,4}\">([\s\S]*?)<\/span>'
img_regex = r'<img[\w\W]+?/>'

parsed_questions = [
    {
        'question': re.sub(r'\d{1,4}\. ', '', question['title']),
        'answers': [{
            'answer': wrong_answer,
            'correct': False
        } for wrong_answer in re.findall(wrong_answer_regex, question['description'])] + [{
            'answer': re.search(right_answer_regex, question['description']).group(1),
            'correct': True
        }],
        'extra_content': re.findall(img_regex, question['description'])
    } for question in questions
]

with open('questions.json', 'w+') as f:
    f.write(json.dumps(parsed_questions, ensure_ascii=False))
