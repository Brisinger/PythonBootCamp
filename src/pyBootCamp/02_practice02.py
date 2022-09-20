from datetime import date


name = input("Enter your Name: ")
letter = ''' Dear <|Name|>,
                    You are Selected!
                    <|Date|>'''
letter = letter.replace("<|Name|>", name)\
    .replace("<|Date|>", date.strftime(date.today(), '%m-%d-%Y'))
print(letter)