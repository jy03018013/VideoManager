import numpy as np


# def matchTemplate_demo():
#     my_array = np.array(["123","5235",4124])
#     print("123456")
#     print(my_array)
# matchTemplate_demo()

def average(*args):
    if len(args) == 0:
        return 0
    nums = 0.0
    for arg in args:
        nums = nums + arg
    return nums / len(args)


d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.items()]
print ('<table border="1">')
print ('<tr><th>Name</th><th>Score</th><tr>')
print ('AA'.join(tds))

print ('</table>')
