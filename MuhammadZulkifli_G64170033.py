from logic import *
disease_kb = FolKB([
    expr('(Mengalami(x,G01) & Mengalami(x,G02) & Mengalami(x,G03) & Mengalami(x,G04)) ==> Terjangkit(x,P01)')
])
for i in range(1, 23):
    if(i<10):
        disease_kb.tell(expr('Mengalami(Alex,G0' + str(i) + ')'))
    else:
        disease_kb.tell(expr('Mengalami(Alex,G' + str(i) + ')'))
print(disease_kb.ask(expr('Terjangkit(Alex, x)'))[x])
