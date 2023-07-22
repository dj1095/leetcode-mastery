import requests
import json
import os

BASE_URL = "https://leetcode.com/problems"
API_ENDPOINT = 'https://leetcode.com/graphql'
question_name = input("Enter question name: ")
ext = input("Enter language used : ").lower()

mapper = {
  "java":".java",
  "python":".py"
}

# Define the GraphQL query with variables
query = '''
  query questionContent($titleSlug: String!){
    question(titleSlug: $titleSlug){
    questionId
    questionTitle
    difficulty
    content
    mysqlSchemas
    dataSchemas
    }
}
'''

# Define the variables for the query
variables = {
    "titleSlug": question_name
}

# Make a POST request to the GraphQL server
response = requests.post(API_ENDPOINT, json={'query': query, 'variables': variables})

# Parse the response
data = json.loads(response.text)                                 
question_id = data["data"]["question"]["questionId"]
question_title = data["data"]["question"]["questionTitle"]
difficulty = data["data"]["question"]["difficulty"]
content = data["data"]["question"]["content"]
resp_text = (content.replace("\\n"," ")
                    .replace("\\t","")
                    .replace('=\\', '='))

#Create new Directory
title = question_title.replace(" ", "")
dir_path = os.path.dirname(os.getcwd()) + "/" + difficulty + "/" + question_id+"."+title
if not os.path.isdir(dir_path):
  os.mkdir(dir_path)


#Creating ReadMe file

read_me = "README.md"
read_me_path = dir_path + "/" + read_me
link = BASE_URL + "/" + question_name + "/"  
html_content = f'''
<h2></h2>
<h2><a href="{link}" target="_blank">{question_id}.{question_title}</a></h2>
<h3>Difficulty - {difficulty}</h3>
'''
file_content = "".join([html_content,"\n",resp_text])
f = open(read_me_path,'w')
f.write(file_content)

#Creating Solution File
solution_file = ""
if ext in mapper:
  solution_file = "Solution" + mapper[ext]
else:
  solution_file = "Solution" + mapper['python']
sol_path = dir_path + "/" + solution_file
f2 = open(sol_path,'w')


