print("What is the quadratic term's co-efficient:")
a = float(input())
print("What is the linear term's co-efficient:")
b = float(input())
print("What is the constant:")
c = float(input())
try:
    firstValue,secondValue (-b+((b**2)-(4*a*c))**(0.5))/(2*a),(-b-((b**2)-(4*a*c))**0.5)/(2*a)
    print(f"The answers are {firstValue} and {secondValue}")
except:
    print("The quadratic equation has an imaginary solution")