def pythonquizz():

    print("<!DOCTYPE html>")
    print("<html>")
    print("<head>")
    print("<title>Python Quiz</title>")
    print("<style>")
    print("body {")
    print("background-image: url('http://localhost/Mainproject/image9.jpg');")  
    print("background-size: cover;")
    print("background-attachment: fixed;")
    print("}")
    print("input[type=submit] {")
    print("background-color: #4CAF50;") 
    print("border: none;")  
    print("color: white;")  
    print("padding: 15px 32px;")  
    print("text-align: center;") 
    print("text-decoration: none;")  
    print("display: inline-block;")  
    print("font-size: 16px;")  
    print("margin: 4px 2px;")  
    print("cursor: pointer;") 
    print("border-radius: 10px;")  
    print("}")
    print("input[type=submit]:hover {")
    print("background-color: #45a049;")  
    print("}")
    print("</style>")
    print("</head>")
    print("<body>")
    print("<h1><center> Python Quizz</center></h1>")
    print("<form action='result.py'>")
    print("1. What is the data type of print(type(10))")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q1' > float  <br> "+
               " <input type='radio' value='ans2' name='q1'> int <br>"+ 
               "<input type='radio' value='ans3' name='q1'> str <br>")
    print("<br><br>")

    print("2. What is the output of the expression  print(-18 // 4)")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q2' > -4  <br> "+
               " <input type='radio' value='ans2' name='q2'> -5 <br>"+ 
               "<input type='radio' value='ans3' name='q2'> 4 <br>")

    print("3. What does the 'print' function do in Python?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q3' > Display output on the screen  <br> "+
               " <input type='radio' value='ans2' name='q3'> Read input from the user<br>"+ 
               "<input type='radio' value='ans3' name='q3'> Perform mathematical calculations<br>")
    print("<br><br>")

    print("4. Which of the following is a correct variable name in Python?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q4' > my_variable  <br> "+
               " <input type='radio' value='ans2' name='q4'> 2ndVariable <br>"+ 
               "<input type='radio' value='ans3' name='q4'> all of the above <br>")
    print("<br><br>") 

    print("5. Which of the following is not a valid data type in Python?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q5' > float  <br> "+
               " <input type='radio' value='ans2' name='q5'> int <br>"+ 
               "<input type='radio' value='ans3' name='q5'> double <br>")
    print("<br><br>")

    print("6. What does the 'range()' function in Python return?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q6' > List of integers  <br> "+
               " <input type='radio' value='ans2' name='q6'> Tuple of integers <br>"+ 
               "<input type='radio' value='ans3' name='q6'> Iterator of integers <br>")
    print("<br><br>")

    print("7. Which of the following is a correct way to comment out a line in Python?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q7' >  // Comment <br> "+
               " <input type='radio' value='ans2' name='q7'> # Comment <br>"+ 
               "<input type='radio' value='ans3' name='q7'> /* Comment */ <br>")
    print("<br><br>")

    print("8. Which of the following is the correct syntax for a lambda function in Python?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q8' >   lambda(x): x * 2<br> "+
               " <input type='radio' value='ans2' name='q8'> lambda x: x * 2 <br>"+ 
               "<input type='radio' value='ans3' name='q8'>  def x: return x * 2<br>")
    print("<br><br>")

    print("9. Which of the following statements is used to exit a loop in Python?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q9' > stop<br> "+
               " <input type='radio' value='ans2' name='q9'> break<br>"+ 
               "<input type='radio' value='ans3' name='q9'> exit<br>")
    print("<br><br>")

    print("10. Which of the following statements is true about Python?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q10' > It is a compiled language<br> "+
               " <input type='radio' value='ans2' name='q10'> It supports automatic memory management<br>"+ 
               "<input type='radio' value='ans3' name='q10'>  It is mainly used for low-level programming<br>")
    print("<br><br>")

    print("11. Which of the following is not a valid way to comment in Python?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q11' >  // This is a comment<br> "+
               " <input type='radio' value='ans2' name='q11'>  # This is a comment<br>"+ 
               "<input type='radio' value='ans3' name='q11'> ''' This is a comment '''<br>")
    print("<br><br>")

    print("12.  Which keyword is used to define a function in Python?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q12' >  define <br> "+
               " <input type='radio' value='ans2' name='q12'> def<br>"+ 
               "<input type='radio' value='ans3' name='q12'> function <br>")
    print("<br><br>")

    print("13. What is Python?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q13' >    High-level programming language<br> "+
               " <input type='radio' value='ans2' name='q13'> Low-level programming language <br>"+ 
               "<input type='radio' value='ans3' name='q13'>  Assembly language<br>")
    print("<br><br>")

    print("14. Which of the following is the correct way to define a tuple in Python?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q14' > {1, 2, 3} <br> "+
               " <input type='radio' value='ans2' name='q14'> [1, 2, 3]<br>"+ 
               "<input type='radio' value='ans3' name='q14'> (1, 2, 3) <br>")
    print("<br><br>")

    print("15.What is the correct syntax to open a file in Python? ")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q15' >  open_file('file.txt')<br> "+
               " <input type='radio' value='ans2' name='q15'>open('file.txt') <br>"+ 
               "<input type='radio' value='ans3' name='q15'>  open_file('file.txt', 'r')<br>")
    print("<br><br>")

    print("16.Which method is used to remove an item from a list in Python? ")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q16' >  remove() <br> "+
               " <input type='radio' value='ans2' name='q16'>  pop()<br>"+ 
               "<input type='radio' value='ans3' name='q16'>  delete() <br>")
    print("<br><br>")

    print("17.Which of the following is not a valid comparison operator in Python? ")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q17' >  == <br> "+
               " <input type='radio' value='ans2' name='q17'> <=<br>"+ 
               "<input type='radio' value='ans3' name='q17'>   ><<br>")
    print("<br><br>")

    print("18.What does the 'in' keyword do in Python? ")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q18'>  Checks if a string is empty <br> "+
               " <input type='radio' value='ans2' name='q18'> Checks if an item exists in a list<br>"+ 
               "<input type='radio' value='ans3' name='q18'>  Converts a string to lowercase<br>")
    print("<br><br>")

    print("19.What is the purpose of the del statement in Python? ")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q19' > To delete a file <br> "+
               " <input type='radio' value='ans2' name='q19'>  To delete a variable<br>"+ 
               "<input type='radio' value='ans3' name='q19'>  To delete a function<br>")
    print("<br><br>")

    print("20. Which of the following is used to execute a block of code only if a certain condition is true in Python?")
    print("<br><br>")
    print("<input type='radio' value='ans1' name='q20' >  then<br> "+
               " <input type='radio' value='ans2' name='q20'> next<br>"+ 
               "<input type='radio' value='ans3' name='q20'>  if<br>")

    print("<br><input type='submit' value='Submit'>")
    print("</form>")
    print("</body>")
    print("</html>")
    
