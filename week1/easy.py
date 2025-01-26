name = input("enter your name: ")
sname = input("enter your surname: ")
crn =  input("enter the crn: ")
sj = input("enter the name of the subject: ")
mt1 = input("enter mt1 score: ")
mt2 = input("enter mt2: ")
final = input("enter final score: ")

avg = float(mt1)*0.3 + float(mt2)*0.3 + float(final)*0.4

print(f"""
      Name: {name}
      Surname: {sname}
      CRN: {crn}
      Subject: {sj}
      Midterm-1: {mt1}
      Midterm-2: {mt2}
      Final: {final}
      Weighted average of {name} {sname} is {avg}  
      """)