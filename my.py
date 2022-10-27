import speech_recognition as sr
import pyttsx3
import time

ISTJ = 'You are responsible, sincere, analytical, reserved, realistic, systematic, Hardworking and trustworthy with sound practical judgment.'
ISFJ = 'You are Warm, considerate, gentle, responsible, pragmatic, thorough. Devoted caretaker, who enjoy being helpful to others.'
ISTP = 'You are Action-oriented, logical, analytical, spontaneous, reserved, independent.Enjoy adventure, skilled at understanding how machanical things work.'
ISFP = 'You are Gentle, sensitive, nurturing, helpful, flexible, realistic. Seek to create a personal environment that is both beautiful and practical.'
ESTP = 'You are Outgoing, realistic, action-oriented,curious,verstile,spontaneous.Pragmatic problem solvers and skillful negotiators.'
ESFP = 'You are Playful, enthusiastic, friendly, spontaneous, tactful, flexible. Have strong common sense, enjoy helping people in tangible ways.'
ESFJ = 'You are Friendly, outgoing, reliable, conscientious, organized, practical. Seek to be helpful and please others , enjoy being active and productive.'
ESTJ = 'You are Efficient,outgoing,analytical,syestematic,dependable,realistic.Like to run the show and get things done in an orderly fashion.'
INFJ = 'You are Idealistic, organized, insighful, dependable, compassionate, gentle. Seek harmony and cooperation, enjoy intellectual stimulation.'
INTJ = 'You are Innovative , independent, strategic, logical, reserved, insightful. Driven by their own orignal ideas to achieve improvements.'
INFP = 'You are Sensitive, creative, idealistic, perceptive, caring, loyal. Value inner  harmony and personal growth ,focus on dreams and possibilities.'
INTP = 'You are Intellectual,logical,precise,reserved,flexible,imaginative.Original thinkers who enjoy speculation and creative problem solving.'
ENFP = 'You are Enthusiastic, creative , spontaneous, optimistic, supportive playful. Values inspiration, enjoy starting new projects see potential in others.'
ENTP = 'You are Intentive, enthusiastic, strategic, enterprisng, inquisitive, versatile. Enjoy new ideas and challenges , value inspiration.'
ENFJ = 'You are Caring, enthusiastic, idealistic, organized, diplomatic, responsible. Skilled communicators who value connection with people.'
ENTJ = 'you are Strategical, logical, efficient, outgoing, ambitious, independent. Effective organizers of people and long-range planners.'



listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def Talk(text):
    engine.say(text) 
    engine.runAndWait()


def Take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = ' '
            command = listener.recognize_google(voice)
    except:
        pass
    return command


def run():
    Talk("Hi what is your name")
    com = input("Write your name here...! ")
    time.sleep(2)
    if com != ' ':
        Talk(f'''ok I am here to judge your personality 
        so i asked you only four questions and you have to answer these questions just only in one word 
        so lets go''')
        Talk('''My first question is that 
        are you extrovert or introvert 
        extrovert like you are a talkative person and enjoy with friends at weekend 
        and introvert is something like you are enjoy alone yourself like 
        reading book or netflix or seeing movie at weekend
        if you are extrovert type e and
        if you are introvert type i''')
    a = input("Write your answer here...! ")
    time.sleep(2)

    Talk('''sure 
    My second question is 
    You are sensing or intutive
    sensing people are practical and prefer routine and order 
    and they focus on details
    and intutives people are thinking differently and make new ideas
    and these people are not believe in reality so much 
    if you are sensing type s and
    if you are intutive type n''')
    b = input("Write your answer here...! ")
    time.sleep(2)

    Talk('''Ok
    Now my third question is that 
    Your are a person of thinking or feeling
    Thinking persons are those who make decisions which they think its logically right
    they do not care about that through this decision anyone can hurt
    on the other hand
    feeling type persons are those who make decisions to make other people happy even 
    this decision can hurt him
    they make persons happy with thier decisions 
    if you are thinking  type t and
    if you are feeling type f''')
    c = input("Write your answer here...! ")
    time.sleep(2)

    Talk(''' now my last question to you is 
    are you judging or perceiving 
    judging type persons are those 
    who prefer order and structure in their life 
    on the other hand 
    perceiving type persons are flexible they work at time 
    but they do not prefer order and structure in their life 
    if you are judging type j and
    if you are perceiving type p''')
    d = input("Write your answer here...! ")
    time.sleep(2)

    print(f'''\n\nOkkk
    {com}
         you are {a}{b}{c}{d}
         ''')

    print('\n\n')
    if a+b+c+d == 'istj':
        print(ISTJ)
        Talk(ISTJ)
    elif a+b+c+d == 'isfj':
        print(ISFJ)
        Talk(ISFJ)
    elif a+b+c+d == 'istp':
        print(ISTP)
        Talk(ISTP)
    elif a+b+c+d == 'isfp':
        print(ISFP)
        Talk(ISFP)
    elif a+b+c+d == 'estp':
        print(ESTP)
        Talk(ESTP)
    elif a+b+c+d == 'esfp':
        print(ESFP)
        Talk(ESFP)
    elif a+b+c+d == 'estj':
        print(ESTJ)
        Talk(ESTJ)
    elif a+b+c+d == 'esfj':
        print(ESFJ)
        Talk(ESFJ)
    elif a+b+c+d == 'infj':
        print(INFJ)
        Talk(INFJ)
    elif a+b+c+d == 'intj':
        print(INTJ)
        Talk(INTJ)
    elif a+b+c+d == 'infp':
        print(INFP)
        Talk(INFP)
    elif a+b+c+d == 'intp':
        print(INTP)
        Talk(INTP)
    elif a+b+c+d == 'enfp':
        print(ENFP)
        Talk(ENFP)
    elif a+b+c+d == 'entp':
        print(ENTP)
        Talk(ENTP)
    elif a+b+c+d == 'enfj':
        print(ENFJ)
        Talk(ENFJ)
    elif a+b+c+d == 'entj':
        print(ENTJ)
        Talk(ENTJ)
run()