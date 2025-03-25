import requests
url ="https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json"

response = requests.get(url)
content = response.json()

user_input =int(input("enter the question_id: "))

# dictionary should be indexed with name of the key
list_of_questions = content['quizzes'] #list

for q in list_of_questions:  #q is each dictionary . list_of_questions is list of dictionaries
    for each_q in q["questions"]:  #each_q is dict.  q["questions"] is a list . questions is the key inside q dict.
        if each_q["id"] == user_input:
            for cities,correct_answer in each_q["choices"].items():
                print(f"Checking Choice: {cities} -> {correct_answer}")
                if correct_answer:
                    print(f"The correct answer is {cities}")





