letter = '''
Dead <|Name|>,
    Your are selected !
    <|Date|>
'''
 
name = input("enter your name :")
date = int(input("enter date:"))

print(f'''
Dead <|{name}|>,
    Your are selected !
    <|{date}|>
''',name,date)  

print(letter.replace("<|Name|>","Harry").replace("<|Date|>","24 September 2050"))