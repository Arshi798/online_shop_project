import json
class student:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def __repr__(self):
        return f'Student(your name is {self.name} and your score is {self.score})'
s1=student('Ali', 19)
try:
    with open('class_s.json','w') as f:
        json.dump(s1.__dict__,f,indent=2)
except:
    print('Error')
