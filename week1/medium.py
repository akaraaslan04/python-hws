x = float(input("enter x value: "))
y = float(input("enter y value: "))

sum = x+y
sub = x-y
mult = x*y
if(y==0):
    div = "cannot divide by zero"
else:
    div = x/y
if(y==0 or x%y!=0 ):
    remain = "y does not divide x"
else:
    remain = "y divides x"
    
print(f"""
      x+y: {sum}
      x-y: {sub}
      x*y: {mult}
      x/y: {div}
      {remain}
      """)