import re
def arithmetic_arranger(problems, show = False):  
    if len(problems) > 5: #Checks if the list is greater than 5
      return "Error: Too many problems."
      
    firstLine = ""
    secondLine = ""
    lines = ""
    thirdLine = ""
    final = ""
    for problem in problems:
      temp = problem.split()
      #Checks if the are / or * operators
      if "*" in problem or "/" in problem:
        return "Error: Operator must be '+' or '-'."
      
      #Checks if the numbers have digits
      fNumber = temp[0]
      op = temp[1] #operator
      sNumber = temp[2]
      if fNumber.isdigit() == False or sNumber.isdigit() == False:
        return "Error: Numbers must only contain digits."

      #Checks if the digits are in right length
      if len(fNumber) > 4 or len(sNumber) > 4:
        return "Error: Numbers cannot be more than four digits."

      #Calculates the value of a problem
      if op == "+":
        value = str(int(fNumber) + int(sNumber))
      elif op == "-":
        value = str(int(fNumber) - int(sNumber))
      
      #The hardest part
      temp2 = max(len(fNumber), len(sNumber)) + 2
      up = fNumber.rjust(temp2) + "    "
      down = op + " " + sNumber.rjust(temp2 - 2) + "    "
      ddown = value.rjust(temp2) + "    "
      firstLine += up
      secondLine += down
      thirdLine += ddown
      for i in range(temp2):
        lines += '-'
      lines += "    "

      
    
    #Checks the "show" boolean value
    if show == False:
      final += firstLine + "\n" + secondLine + "\n" + lines + "\n"
    else:
      final += firstLine + "\n" + secondLine + "\n" + lines + "\n" + thirdLine
    return final