from sympy import *
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
import PySimpleGUI as sg

v0, x0 ,ω,φ, m1, m2, Fe  = symbols('v0 x0 ω φ m1 m2 Fe')
vars = [Fe, m1, m2, φ, ω, v0, x0, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
units = {"s": "m", "v": "m/s", "t": "s", "v0": "m/s", "a": "m/(s^2)", "x": "m", "x0": "m", "ω": "rad/s", "φ":"rad", "m1": "kg", "m2": "kg", "Fe" :"N", "T": "s", "R": "m", "F":"N", "k" :"N/m", "G": "N*m^2/kg^2"}
functions = {"1": v*t-s, "2": (v-v0)/t -a, "3": x0+v0*t - x+ a*t**2/2, "4": v**2-v0**2 - 2*a*s, "5": -ω+φ/t, "6": 1/T -v, "7": 2*pi*R/T - v, "8": ω*R - v, "9": -a + v**2/R, "10":-a + ω**2*R, "11":F/m - a, "12":G*m1*m2/r**2 - F, "13":m*g-F,"14":-k*x - Fe,}

layout1 = [[sg.Text("Choose the function that you want to use:")],
           [sg.Button('v=s/t', key = "1"), sg.Button('a = (v-v0)/t', key = "2"), sg.Button(' x = x0 + v0*t + a*t^2/2', key = "3")],
           [sg.Button('v^2-v0^2 = 2*a*s', key = "4"), sg.Button('ω = φ/t', key = "5"), sg.Button('v = 1/T', key = "6"), sg.Button('v = 2*π*R/T', key = "7"), sg.Button("v = ω*R", key = 8)],
           [sg.Button("a = v^2/R", key = 9), sg.Button("a = ω^2*R", key = 10), sg.Button("a = F/m", key = 11), sg.Button("F = G*m1*m2/r^2", key =12), sg.Button("F = m*g", key = 13), sg.Button("Fe = -k*x", key = 14)],
           [sg.Button("Cancel")]]
window1 = sg.Window('Formula', layout1, size = (800, 800)).Finalize()
window1.Maximize()
event1, values1 = window1.read()

if event1 == sg.WIN_CLOSED or event1 == "Cancel":
       window1.close()
       exit()

varsInFormula = []

if event1 in functions.keys():
    function = functions.get(event1)

    for index in vars:

        if str(index) in str(function):

            varsInFormula.append(index)
            index+=1

        window1.close()

layout2=[[sg.Text("Choose the variable that you need to get in result:")],
         [sg.Combo(varsInFormula, expand_x = True, readonly = True, key = "Combo")],
         [sg.Button("Ok"), sg.Button("Cancel")] ]
window2 = sg.Window("Variable", layout2, size = (800,800)).Finalize()
window2.Maximize()
event2, values2 = window2.read()

if event2 == sg.WIN_CLOSED or event2 == "Cancel":
    
    window2.close()
    exit()

result_var = values2["Combo"]

if event2 == "Ok":  
    
    formula = solve(functions.get(event1), result_var)
    window2.close()

layout3=[[sg.Text(f"{result_var} = {str(formula)[1:-1]}")],
         [sg.Text("Do you wish to solve the value of this equation?")],
         [sg.Button("Yes"), sg.Button("No")]]
window3 = sg.Window("Solving", layout3, size = (800,800)).Finalize()
window3.Maximize()
event3, values3 = window3.read()    

if event3 == sg.WIN_CLOSED or event3 == "No":
    
    window3.close()
    exit()

if event3 == "Yes":
    
    form = list(formula[0].atoms(Symbol, NumberSymbol))


layout4 = [[sg.Text("Please convert the values to SI units! If it is not a whole number, use a dot, not a comma!")]]
for index1 in form:
    
    layout4 += [[sg.Text(f"Enter the value of {index1}:"), sg.InputText(key = f"{index1}"), sg.Text(f"{units.get(str(index1))}")]]
    index1 += index1

layout4 += [[sg.Button("Solve"), sg.Button("Cancel")]]
window4=sg.Window("Substitution", layout4).Finalize()
window4.Maximize()
event4, values4 = window4.read()

if type(values4) != float:
    
    sg.Popup("The value is not a float or an integer!")
    exit()
           
if event4 ==sg.WIN_CLOSED or event4 =="Cancel":
    
    window4.close()
    exit()

values = []
values.append(values4)
res = function.subs(values4)
window4.close

if "sqrt" in str(solve(res, result_var)):
    result = str(solve(res, result_var)).replace(",", f" {units.get(str(result_var))} or {result_var} = ")
    layout5 = [[sg.Text(f"{result_var} =  {result[1:-1]} {units.get(str(result_var))}")],
               [sg.Button("Exit")]]

else:
    
    layout5 = [[sg.Text(f"{result_var} =  {round(float(nsolve(res, result_var, solve(res,result_var))), 4)} {units.get(str(result_var))}")], 
               [sg.Button("Exit")]]
    
window5 = sg.Window("Result",layout5).Finalize()
window5.Maximize()
event5,values5 = window5.read()

if event5 == sg.WIN_CLOSED or event5 == "Exit":
    
    window5.close()
    exit()
