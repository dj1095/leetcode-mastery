import requests
import json
import os

BASE_URL = "https://leetcode.com/problems"
QUESTION_NAME = "redundant-connection"
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

# Define the GraphQL endpoint URL
graphql_endpoint = 'https://leetcode.com/graphql'

# Define the variables for the query
variables = {
    "titleSlug": QUESTION_NAME
}

# Make a POST request to the GraphQL server
response = requests.post(graphql_endpoint, json={'query': query, 'variables': variables})

# Parse the response
data = json.loads(response.text)


#File Handling
file_name = "README.md"
link = BASE_URL + "/" + QUESTION_NAME + "/"                                   
question_id = data["data"]["question"]["questionId"]
question_title = data["data"]["question"]["questionTitle"]
difficulty = data["data"]["question"]["difficulty"]
content = data["data"]["question"]["content"]
resp_text = (content.replace("\\n"," ")
                    .replace("\\t","")
                    .replace('=\\', '='))

#Create new Directory
title = question_title.replace(" ", "")
dir_path = os.path.dirname(os.getcwd()) + "/" + difficulty + "/" + title
file_path = dir_path + "/" + file_name

html_content = f'''
<h2></h2>
<h2><a href="{link}" target="_blank">{question_id}.{question_title}</a></h2><br/>
<h3>Difficulty - {difficulty}</h3>
'''

file_content = "".join([html_content,"\n",resp_text])
f = open(file_path,'w')
f.write(file_content)

