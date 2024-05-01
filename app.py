from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary containing quiz questions, options, and correct answers
quiz_questions = {
    1: {
        'question': '1. Who is the author of the famous book titled "The Chibok Girls"?',
        'options': ['Teju Cole', 'Buchi Emecheta', 'Helon Habila', 'Sofia Atta'],
        'correct_answer': 'Helon Habila'
    },
    2: {
        'question': '2. "Women of Owu" was written by?',
        'options': ['Femi Osofisan', 'Femi Adebayo', 'Femi Oyeniran', 'Femi Kayode'],
        'correct_answer': 'Femi Osofisan'
    },    
    3: {
        'question': '3. "There was a Country" was written by?',
        'options': ['Wole Soyinka', 'Chinua Achebe', 'Patience Ozokwor', 'Ben Okri'],
        'correct_answer': 'Chinua Achebe'
    },    
    4: {
        'question': '4. He was titled the Abese of Egbaland',
        'options': ['Sani Abacha', 'Tafawa Balewa', 'Ernest Shonekan', 'Babatunde Fashola'],
        'correct_answer': 'Ernest Shonekan'
    },    
    5: {
        'question': '5. How did Tafawa Balewa die?',
        'options': ['He died of old age', 'He hung himself', 'He drowned in river Niger', 'He was murdered'],
        'correct_answer': 'He was murdered'
    },
    6: {
        'question': '6. Nigeria gained independence on...',
        'options': ['October 1, 1958', 'October 1, 1960', 'October 1, 1962', 'October 1, 1964'],
        'correct_answer': 'October 1, 1960'
    },
    7: {
        'question': "7. When was the Aba Women's riot?",
        'options': ['1920', '1929', '1937', '1945'],
        'correct_answer': '1929'
    },    
    8: {
        'question': "8. Not a Nigerian geopolitical zone",
        'options': ['North Central', 'North East', 'North North', 'North West'],
        'correct_answer': 'North North'
    },     
    9: {
        'question': "9. Number of geopolitical zones in Nigeria",
        'options': ['5', '6', '7', '8'],
        'correct_answer': '6'
    },     
    10: {
        'question': "10. When was the amalgamation of Nigeria?",
        'options': ['1914', '1924', '1934', '1944'],
        'correct_answer': '1914'
    },     
    11: {
        'question': "11. Nigeria is currently in its ________ republic",
        'options': ['First', 'Second', 'Third', 'Fourth'],
        'correct_answer': 'Fourth'
    },     
    12: {
        'question': "12. NNPC stands for...",
        'options': ['Nigerian Nuclear Power Commission', 'Nigerian National Petroleum Corporation', 'Northern Nigeria Petrochemical Corporation', 'National Network of Petroleum Consultants'],
        'correct_answer': 'Nigerian National Petroleum Corporation'
    },     
    13: {
        'question': "13. Sani Abacha was a well known...",
        'options': ['Dictator', 'Neuro Surgeon', 'District Attorney', 'Prophet'],
        'correct_answer': 'Dictator'
    },     
    14: {
        'question': "14. He was the Chief Security Officer to General Sani Abacha",
        'options': ['Chukwuma Nzeogwu', 'Hamza Al-Mustapha', 'Johnson Aguiyi-Ironsi', 'Alex Ibru'],
        'correct_answer': 'Hamza Al-Mustapha'
    },     
    15: {
        'question': "15. The first Nigerian Minister of Foreign Affairs",
        'options': ['Utahhman Dan Fodio', 'Nuhu Bamalli', 'Jaja Wachuku', 'Funmi Ransome-Kuti'],
        'correct_answer': 'Funmi Ransome-Kuti'
    },     
    16: {
        'question': "16. The man on the 5 naira note",
        'options': ['Nnamdi Azikiwe', 'Ahmadu Bello', 'Obafemi Awolowo', 'Tafawa Balewa'],
        'correct_answer': 'Tafawa Balewa'
    },     
    17: {
        'question': "17. The Aburi Accord was not honored by the _______",
        'options': ['The Gowon Administration', 'The Abacha Administration', 'The Obasanjo Administration', 'The Shagari Administration'],
        'correct_answer': 'The Gowon Administration'
    },     
    18: {
        'question': "18. The second president of Biafra",
        'options': ['Johnson Aguiyi-Ironsi', 'Chukwuma Nzeogwu', 'Odumegwu Ojukwu', 'Philip Effiong'],
        'correct_answer': 'Philip Effiong'
    },     
    19: {
        'question': "19. Not a Nigerian Language",
        'options': ['Ikwerre', 'Tiv', 'Shona', 'Igala'],
        'correct_answer': 'Shona'
    },     
    20: {
        'question': "20. Not a Nigerian ethnic group",
        'options': ['Anaang', 'Gbagyi', 'Ngoni', 'Jukun'],
        'correct_answer': 'Ngoni'
    },     
    21: {
        'question': "21. Hebert Macaulay was considered by many as the ...",
        'options': ['The creator of the Nigerian flag', 'The founder of Nigerian nationalism', 'The founder of Nigerian white garment church', 'The creator of Nigerian constitution'],
        'correct_answer': 'The founder of Nigerian nationalism'
    },     
    22: {
        'question': "22. NCNC was orginally called",
        'options': ['National Council of Nigerian and the Church', 'National Convention of Nigerian Citizens', 'National Convention of Nigerian Chiefs', 'National Council of Nigeria and the Cameroons'],
        'correct_answer': 'National Council of Nigeria and the Cameroons'
    },     
    23: {
        'question': "23. ________ was the Sardauna of Sokoto",
        'options': ['Frederick John Lugard', 'Sir Ahmadu Bello', 'Kashim Shettima', 'Muhammadu Sanusi I'],
        'correct_answer': 'Sir Ahmadu Bello'
    },     
    24: {
        'question': "24. Rabi'u Musa Kwankwaso served as the governor of ___________",
        'options': ['Borno State', 'Taraba State', 'Kano State', 'Nasarawa State'],
        'correct_answer': 'Kano State'
    },     
    25: {
        'question': "25. Children's Day in Nigeria in on?",
        'options': ['1st June', '27th May', '10th February', '3rd November'],
        'correct_answer': '27th May'
    },     
    26: {
        'question': "26. Patrick Chukwuma Nzeogwu was born in",
        'options': ['Aba', 'Nsukka', 'Kaduna', 'Benin City'],
        'correct_answer': 'Kaduna'
    },     
    27: {
        'question': "27. Festus Okotie-Eboh was the _________ till 1966?",
        'options': ['Minister of Foreign Affairs', 'Minister of Finance', 'Minister of Education', 'Minister of Petroleum'],
        'correct_answer': 'Minister of Finance'
    },     
    28: {
        'question': "28. The 1966 Nigerian counter-coup was also known as the...",
        'options': ['The May Rematch', 'The June Rematch', 'The July Rematch', 'The August Rematch'],
        'correct_answer': 'The July Rematch'
    },     
    29: {
        'question': "29. Nigeria's first military Head of State General",
        'options': ['Murtala Muhammed', 'Adekunle Fajuyi', 'Theophilus Danjuma', 'Johnson Aguiyi-Ironsi'],
        'correct_answer': 'Johnson Aguiyi-Ironsi'
    },     
    30: {
        'question': "30. Bukar Suwa Dimka's cause of death? ",
        'options': ['Public Execution', 'Leukemia', 'Cardiac Arrest', 'Lethal Injection'],
        'correct_answer': 'Public Execution'
    },     
    31: {
        'question': "31. Who served as the governor of the Central Bank of Nigeria from 1967 to 1975? ",
        'options': ['Donald Etiebet', 'Chief Stephen Osadebe', 'Clement Isong', 'Joseph Achuzie'],
        'correct_answer': 'Clement Isong'
    },     
    32: {
        'question': "32. Who was nicknamed the Black Scorpion during the Biafran War? ",
        'options': ['Emmanuel Ifeajuna', 'Victor Banjo', 'Benjamin Adekunle', 'Adewale Ademoyega'],
        'correct_answer': 'Benjamin Adekunle'
    },     
    33: {
        'question': "33. Shehu Shagari was the ____ President/ Head of State of Nigeria ",
        'options': ['2nd', '4th', '6th', '8th'],
        'correct_answer': '6th'
    },
    # Add more questions here
}

# Home route
@app.route('/')
def home():
    # Rendering the home page template with quiz questions
    return render_template('index.html', questions=quiz_questions)

# Quiz route
@app.route('/quiz', methods=['POST'])
def quiz():
    score = 0
    # Iterating through each question in the quiz
    for qid, data in quiz_questions.items():
        # Retrieving the selected option for each question from the form data
        selected_option = request.form.get(str(qid))
        # Checking if the selected option matches the correct answer
        if selected_option == data['correct_answer']:
            # Incrementing the score if the answer is correct
            score += 1
    # Rendering the result page template with the score and total number of questions
    return render_template('result.html', score=score, total=len(quiz_questions))

if __name__ == '__main__':
    app.run(debug=True)
