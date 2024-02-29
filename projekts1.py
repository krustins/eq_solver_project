from sympy import *
from sympy.abc import s, v,t, a
v0 = symbols('v0')

function = input("Choose the function that you want to use:\n 1) s = v*t\n 2) v0^2 - v^2 = 2*a*s\n Choose the number of the formula:")
functions = {"1": v*t-s, "2": v0**2-v**2-2*a*s  }
result_var = input("Enter the variable that you need in the result:")
formula = solve(functions.get(function), result_var)
print(f'{result_var} = {formula}')
'''
form = formula[0].atoms(Symbol, NumberSymbol)
vertibas = {}
for i in form:
    vertibas[i] = input(f"{i} vertiba: ")
print(vertibas)
atbilde = solve(float(vertibas[vertibas.values([0])])*t-float(vertibas[vertibas.values([1])]), t)
print(atbilde)'''
solveOrNot = input('Do you want to solve the equation using the values? :')
if solveOrNot == 'Yes':
    if function == '1':
        if result_var == "s":
             vValue = input("Input the value of v (velocity) : ")
             tValue = input ('Input the value of t(time):')
             print (f"s =  {solve(float(vValue)*float(tValue) - s, s)}")
        elif result_var == 't':
             vValue = input("Input the value of v (velocity) : ")
             sValue = input ('Input the value of s(displacement):')
             print (f"t =  {solve(float(vValue)*t - float(sValue),t )}") 
        elif result_var == 'v':
             tValue = input("Input the value of t (time) : ")
             sValue = input ('Input the value of s(displacement):')
             print (f"v =  {solve(v*float(tValue) - float(sValue), v)}") 
    elif function =='2':
        if result_var == "v0":
             vValue = input("Input the value of v (velocity) : ")
             aValue = input ('Input the value of a(acceleration):')
             sValue = input('Input the value of s(displacement)')
             print (f"v0 =  {solve(v0**2-float(vValue)**2-2*float(aValue)*float(sValue), v0)}")
        elif result_var == 'a':
             vValue = input("Input the value of v (velocity) : ")
             sValue = input ('Input the value of s(displacement):')
             v0Value = input ('Input the value of v0(velocity at the start):')
             print (f"a =  {solve(float(v0Value)**2-float(vValue)**2-2*a*float(sValue), a )}") 
        elif result_var == 'v':
             v0Value = input ('Input the value of v0(velocity at the start):')
             sValue = input ('Input the value of s(displacement):')
             aValue = input ('Input the value of a(acceleration):')
             print (f"v =  {solve(float(v0Value)**2-v**2-2*float(aValue)*float(sValue), v)}")
        elif result_var == 's':
             v0Value = input ('Input the value of v0(velocity at the start):')
             aValue = input ('Input the value of s(displacement):')
             vValue = input("Input the value of v (velocity) : ")
             print (f"s =  {solve(float(v0Value)**2-float(vValue)**2-2*float(aValue)*s, s)}")       

    
