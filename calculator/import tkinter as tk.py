import tkinter as tk


# Write a way to replace the values in the string after we do the calculation
class calculate:   
    def calculate(string):
        while '(' in string:
            pos = string.rfind('(')
            endPos = string.find(')')

            equation = string[pos+1:endPos]
            parts = equation.split()
            a, operator, b = parts
            a = int(a)
            b = int(b)
            print(parts)
            print(a)
            print(operator)
            print(b)

            if operator == "+":
                return a + b
            elif operator == "-":
                return a - b
            elif operator == "*":
                return a * b
            elif operator == "÷":
                return a / b
            elif operator == "%":
                return a % b
            else:
                return "Error"
            
# def solve():

# string = "1 + (3+5)"
# while "(" in string loop
#   result = calculate(string)
#   for i range string.length() loop
#     if string[i] = "("
#       start = i 
#     if string = ")" 
#       end = i
#       break
#     //replace between these indexes 
            
root = tk.Tk()
root.title("Calculator")
root.geometry("400x300")


def solve():
    equation = str(getText())
    clear()
    if equation == "Error":
        clear()
        insertText("ERROR")
    else:
        result = calculate.calculate(equation)
        start = equation.rfind('(')
        end = equation.find(')')
        insertText(result)
        equation = equation[:start ]+ str(result)+ equation[end:] 




button_frame = tk.Frame(root)
button_frame.pack(expand=True)

# Buttons
button1 = tk.Button(button_frame, text=" 1 ", command = lambda: insertText("1"))
button2 = tk.Button(button_frame, text=" 2 ", command = lambda: insertText("2"))
button3 = tk.Button(button_frame, text=" 3 ", command = lambda: insertText("3"))
button4 = tk.Button(button_frame, text=" 4 ", command = lambda: insertText("4"))
button5 = tk.Button(button_frame, text=" 5 ", command = lambda: insertText("5"))
button6 = tk.Button(button_frame, text=" 6 ", command = lambda: insertText("6"))
button7 = tk.Button(button_frame, text=" 7 ", command = lambda: insertText("7"))
button8 = tk.Button(button_frame, text=" 8 ", command = lambda: insertText("8"))
button9 = tk.Button(button_frame, text=" 9 ", command = lambda: insertText("9"))
button0 = tk.Button(button_frame, text=" 0 ", command = lambda: insertText("0"))
buttonAdd = tk.Button(button_frame, text=" + ", command = lambda: insertText(" + "))
buttonSubtract = tk.Button(button_frame, text=" - ", command = lambda: insertText(" - "))
buttonMultiply = tk.Button(button_frame, text=" * ", command = lambda: insertText(" * "))
buttonDivide = tk.Button(button_frame, text=" / ", command = lambda: insertText(" / "))
buttonMod = tk.Button(button_frame, text=" % ", command = lambda: insertText(" % "))
buttonPar1 = tk.Button(button_frame, text=" ( ", command = lambda: insertText("( "))
buttonPar2 = tk.Button(button_frame, text=" ) ", command = lambda: insertText(" )"))
solveButton = tk.Button(button_frame, text=" = ", command = lambda: solve())
textBox = tk.Text(button_frame, height=2, width=16)
backspaceButton = tk.Button(button_frame, text=" ⌫ ", command = lambda: backspace())
clearButton = tk.Button(button_frame, text=" CE ", command = lambda: clear())
button1.grid(row=2, column=0, columnspan=1)
button2.grid(row=2, column=1, columnspan=1)
button3.grid(row=2, column=2, columnspan=1)
button4.grid(row=3, column=0, columnspan=1)
button5.grid(row=3, column=1, columnspan=1)
button6.grid(row=3, column=2, columnspan=1)
button7.grid(row=4, column=0, columnspan=1)
button8.grid(row=4, column=1, columnspan=1)
button9.grid(row=4, column=2, columnspan=1)
button0.grid(row=5, column=1, columnspan=1)
buttonMod.grid(row=1, column=2, columnspan=1)
buttonAdd.grid(row=1, column=3, columnspan=1)
buttonSubtract.grid(row=2, column=3, columnspan=1)
buttonMultiply.grid(row=3, column=3, columnspan=1)
buttonDivide.grid(row=4, column=3, columnspan=1)
buttonPar1.grid(row=1, column=0, columnspan=1)
buttonPar2.grid(row=1, column=1, columnspan=1)
solveButton.grid(row=5, column=3, columnspan=1)
textBox.grid(row=0, column=0, columnspan=5)
backspaceButton.grid(row=1, column=4, columnspan=1)
clearButton.grid(row=2, column=4, columnspan=1)

def getText():
    # Gets the info from the textbox
    current_text = "( " + textBox.get("1.0", "end-1c") + " )"
    validOptions = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", "+", "-", "*", "/", "%", "(", ")"}
    current_index = "1"
    assert current_index in validOptions
    try:
        for i in range (len(current_text)):
            current_index = current_text[i]
    except AssertionError:
        return "Error"
    # print(current_text)
    return current_text

def insertText(text):
    textBox.insert(tk.END, text)

def backspace():
    textBox.delete("end-3c", "end-1c")

def clear():
    textBox.delete(1.0, tk.END)



if __name__ == "__main__":
    root.mainloop()
    while True:
        expression = input()
        if expression.lower() == "q":
            break
        # result = calculate(expression)
    