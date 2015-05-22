concepts1 = [
    
    		   
    		   ['lesson-1-1', 'How the Web Works', 'SERVERS host massive amounts of information. The internet is the platform by which individuals can access this information from their <em>browsers.</em> When an inidividual types in a search into their browser, their computer sends an <em>HTTP request</em> to a server. The server then identifies the corresponding HTML document and relays it to the individuals web browser, which interprets the page and displays it on the users screen. <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/e-48329854/m-48480496"> Click here</a> for a video that explains this process in detail.'],
    		   ['lesson-1-2', 'HTML', 'HTML, or Hypertext Markeup Language, is the <b>glue</b> that holds everything together and is the <em>main protocol of the web.</em> An HTML document contains text content and markup (tags/attributes that modify how the text looks.) <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/m-48724340">This video</a> gives a good overview of HTML.'],
    		   ['lesson-1-3', 'HTML Tags, Elements and Attributes', 'An HTML document is made up of HTML elements. An element is defined as everything within a set of opening and closing tags. The tag tells the browser how to display content. <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/m-48723444">This video</a> goes into detail about the distinction between an element and a tag. An <b>ATTRIBUTE</b> is a property of an  HTML element. <em>HREF</em> is the <b>attribute</b> used to add a URL link in the anchor tag, for instance.'],
    		   ['lesson-1-4', 'INLINE VS. BLOCK', 'HTML elements are categorized as either inline or block. Block elements form an invisible box around the content. Some examples of inline elements are the p, em, b, h1, h2 (all the way up to h6,) and a tags. Some examples of block elements are the div and span tags.'],
    		   ['lesson-1-5', 'WHY COMPUTERS ARE STUPID','Computers are stupid because they interpret code literally, leaving little room for small mistakes and typos. Forgetting to add a closing bracket, for instance, can change the way an entire webpage looks.']
    
    		   ]
    		   
concepts2 = [
    		   
    
    		   ['lesson-2-1', 'HTML vs CSS', 'HTML and CSS are languages that the browser reads and then turns into a visual representation on the page. HTML controls <b>structure and content</b> and CSS controls <em>style</em>.'],
    		   ['lesson-2-2', 'HTML as a Tree Like Structure', 'HTML is defined as being a tree like structure because elements can have other elements inside of them..thus the concept of <em>inheritance</em>. Embedded elements will inherit the properties of the parent element. When programmers talk about "DOM" they\'re referring to the structure of a page.'],
               ['lesson-2-3', 'Indented HTML and Boxes', 'When you read an HTML document, you see a wave of indentations on the left side of the page. The more intended and HTML element is, the more deeply nested its corresponding box is.'],
               ['lesson-2-4', 'Text Editors', 'Programmers use text editors to write code. These are meant to make the process easier. They will, for instance add the closing tag automatically so that the programmer doesnt have to write it out.']
    
               ]

concepts3 = [
    
               ['lesson-3-1', 'The Importance of Avoiding Repetition', 'It is important for programmers to avoid repetition for a myriad of reasons. Repetition makes the task of fixing errors all the more tedious and time consuming, as the programmer will have to change the code over and over again. Less repetition means more efficiency. Also, avoiding repetition helps with code clarity and consistency. By grouping divs into common classes, for intance, the programmer can make <em>one</em> style change that will affect all the corresponding HTML elements as opposed to making the change many times.'],
               ['lesson-3-2', 'CSS', 'CSS stands for Cascading Style Sheets. CSS allows programmers to add to style to HTML. By assigning a class name to a group of similar HTML elements, style can be applied to all the members of that class.']
    		   
    		   ]
    
    
concepts4 = [
    
    			['lesson-4-1', 'Computer', 'Unlike machines that are built to perform one specific task, computers can be programmed to do an infinite number of things. A programmer can make a computer do anything as long as the computer is given a specific sequence of instructions.'],
    			['lesson-4-2', 'Computer Programs', 'A computer program is a specific sequence of instructions that tells the computer what to do. Some examples of a computer program are web browsers, apps, and games.'],
    			['lesson-4-3', 'Programming Language', 'A programming laguage is a code that programmers use to tell the computer what to do. Python is one example of a programming language.'],
    			['lesson-4-4', 'Python', 'Python is a programming language. When you "run" python code, this means that a python interpreter translates it into instructions that the computer understands and can then execute.'],
    			['lesson-4-5', 'Grammar', 'Python has a specific set of rules that must be followed in order for the interpreter to understand the meaning of the code and then communicate it to the computer. As humans, we have the ability to understand the meaning of a statement that may not be clearly articulated or technically correct. Computers aren\'t smart enough to do this- the instructions either will or will not be understood by the computer. In short, there is nothing subjective or ambiguous about a programming language; the rules of grammar and syntax are absolute.'],
    			['lesson-4-6', 'Python Expressions', 'A python "expression" is a correct statement that the interpreter can understand. (1+1) is a valid expression, while (1+ is not because there is no number after the + or closing parenthesis. <a href="https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3527838955/e-48704311/m-48736065" target="_blank">This video</a> does a good example of explaining what makes a valid python expression versus an invalid one.']
    
    			]
    
    
concepts5 = [
    
    			['lesson-5-1', 'A Variable in Python', 'A variable is value attached to a name. For instance, if we say variable_1 = 1 and then write print my_variable + my_variable, we will get the result 2.'],
    			['lesson-5-2', 'What = Means in Python', 'In Python, the equal sign means "takes the value of," as opposed to "is the same as." '],
    			['lesson-5-3', 'How are Variables Useful?', 'Variables are useful because: <br> 1) They allow programmers to assign names in English and thus improve code readability.<br> 2) They allow us to store value <br> 3) They allow us to change the value of a variable (i.e. days = days-1)'],
    			['lesson-5-4', 'String vs. Number', 'In Python, 1 is a number whereas "1" is a string. The code 1 + 1 would give 2, whereas "1" + "1" would give the concatenation of the two strings "11."'],
    			['lesson-5-5', 'Finding Strings in Strings', 'To find the location of a sub string within a string, we use the find operator- list.find(value).']
    
    			]
    		
concepts6 = [
    
    			['lesson-6-1', 'Function', 'A function is a something that receives an input, runs a procedure that does something to the input, and then produces an output.'],
    			['lesson-6-2', 'Making vs. Using a Function', 'To make a function, you write code that starts with def, followed by the function name and then the set of parameters that will be replaced by values when we eventually run the function. This is followed by the body of the code, which specifies what to do with the input parameters. For instance, the function square(a), where:</br> def square(a):</br> answer = a * a</br> return answer</br> will give whatever variable assigned to a, squared. To print the function, we write print square(a)</br> This will give the square of whatever value we have assigned to a.</br> It is important to remember to add a return statement, otherwise the function will not produce an output.'],
    			['lesson-6-3', 'The Importance of Functions', 'Functions are valuable in that they only have to be defined once. As such, they help programmers avoid repetition.'] 
    
    			]
    
    
concepts7 = [
    
    			['lesson-7-1', 'Boolean Values and Comparison Operators', 'In Python, a Boolean value is a statement that will either return True or False. For instance, "print 1>2" will return False, while "print 2==2" will return True. A Boolean value will always include a comparison operator. These are:</br> < smaller than, > larger than, == equal (because we have already used = to mean assignment,) != not equal, <= smaller than or equal to, >= larger than or equal to.'],
    			['lesson-7-2', 'If Statements', 'An If Statement is composed of a test expression and block, where the block is executed when the test expression is true. Example:</br> <p> </br> def bigger(a,b):</br>if a>b:</br>return a</br> else:</br> return b</br></p> </br> With the addition of the Or operator, we can have more than one test expression. For instance, in the procedure is_friend we have two test expressions: </br> <p> def is_friend(name):</br> if name[0] == \'D\' or name[0] == \'E\':</br> return True</br> else:</br> return False </br> </p> This can also be written as:</br> def is_friend(name):</br> return name[0] == \'D\' or name[0] == \'E\'</br> In either case, this function will return "True" where the string name has a first character of \'E\' or \'D\' and "False" when it does not.</br> </p>'],
    			['lesson-7-3', 'While Loops', 'A While Loop is similar to an If Statement in the sense that the block will be executed only if the test expression is true. However, while an If Statement will either execute 0 or 1 time, a While Loop will execute for as long as the test expression is true. This means that a While Loop has the potential to run infinitely. A "counting variable\" will change to mean something new each time the block is executed. <a href="https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3555769686/e-48686708/m-48480488\">This video</a> does a good job of explaining While Loops.'],
    			['lesson-7-4', 'Break Statements', 'If the break test evaluates to true, the while loop will stop and go on to the next statement. <a href="https://www.udacity.com/course/viewer#!/c-ud552-nd/l-3555769686/m-3644799435">This video</a> explains break statements.']
    
    			]
    
concepts8 = [
    
    			['lesson-8-1', 'Lists', 'Lists are sequences of data which contain an assignment statement and corresponding list of elements. Lists can contain numbers, strings or a combination of both.'],
    			['lesson-8-2', 'Nested Lists', 'Lists can can contain other lists. Like characters in strings, list elements are indexed starting from 0.'],
    			['lesson-8-3', 'Mutation and Aliasing', 'Lists can be mutated, while strings cannot.'],
    			['lesson-8-4', 'List Operations', 'The append operation adds a new element to the list. This operation is limited to one list element. The += operation appends any number of elements to the list. The + operation does not mutuate the list but will concatenate the two. The len operation, written as len(list), will give the number of elements in the list.'],
    			['lesson-8-5', 'Index Methods', 'list.index(value) will return the first occurence of the value in the list. If the value does not occur, the python interpreter will return error. "value in list" and "value not in list" are boolean values and will tell us whether or not the value is in the list by returning a value of True or False.'],
    			['lesson-8-6', 'For Loop', 'When we write "for name in list", "name" has the value of "each element in list". ']   
    
    			]
    
concepts9 = [
    
    			['lesson-9-1', 'Object Oriented Programming', 'The key advantage of OOP is that it allows programmers to reuse and recycle code. Also, in OOP, knowledge of how an object works is not necessary for a programmer to be able to use that object.'],
    			['lesson-9-2', 'Classes and Instances', 'A class can be likened to a blueprint. It contains information about the nature and behavior of a particular group of objects. An instance is a single manifestation of a class of objects and will behave according to the blueprint of that particular class. In the movie website project, each movie was an instance of the class movie. Classes can contain both data (ie the self.title instance variable defined within the init function) and intance methods (ie the showtrailer function.)'],
    			['lesson-9-3', '__init__ and Self', 'The init method is a constructor that creates space for a particular instance of an object within a class. The self variable represents the instance of that object. The init constructor can contain any number of variables that provide information about a class of objects.' ],
    			['lesson-9-4', 'Class Variables and Instance Variables', 'Instance variables belong to an instance of a class, where each instance has its own copy of the instance variable (ie the showtrailer method.) A class variable, on the other hand, only has one copy that is shared by all instances in that class (ie the VALID_RATINGS variable.)' ],
    			['lesson-9-5', 'Python Standard Library, Modules, Methods', 'The python standard library contains modules that can be imported and used. A module can define functions, classes and variables. For instance, when we import turtle, we import a module from the python standard library that contain methods and variables that define how objects in the class turtle behave.'],
    			['lesson-9-6', 'Inheritance', 'The concept of inheritance in python refers to the fact that a child element will inherit the same set of information and operate according to the same blueprint as its parent element. If a method that has been defined initially within the class parent is written again within the class child and changed, it is this new method that will be called for the class child and not the method defined within its parent class. This is known as method overriding and shows how OOP allows programmers to reuse the code that is useful to them and also adapt it to fit new instances.' ]
    
    
    			]
    
concepts10 = [
    
    			['lesson-10-1', 'Introduction to Networks', 'A network is a group of three or more entities that communicate indirectly. The internet is a network. </br> Latency: the time it takes for a message to get from source to destination; measured in milliseconds. </br> Bandwidth: the amount of info that can be transmitted per second; measured in mbps. </br> Protocol: set of rules that describe how entities communicate. HTTP stands for hypertext transfer protocol. </br> Client: web browser (ie safari, firefox, internet explorer) </br> Web browser sends message \'get object\' and server responds with the contents of that object.'],
    			['lesson-10-2', 'Make the Internet Work for You', 'URL stands for uniform resource locator; it consists of a protocol (http) host (www.whatever.com) and path (/...) A query parameter or get parameter is extra info that the server gets and changes the url. A cache stores data, can be used to make data requests faster. A fragment is separated by "#" and is used to reference a particular part of a page; not sent to server, purely exists in browser. A method refers to the type of request made- ie get or post. A relative path is the path relative to the host while the full path is the path including the host (absolute vs relative path.) A static file is a pre written file (i.e. image, text document) while a dynamic one is built on the fly by web applications. A web application is a program that generates content, lives on a web server, speaks HTTP.'],
    			['lesson-10-3', 'Forms', 'Forms allow users to enter text, select from dropdown menus, checkbox, radio, password etc..'],
    			['lesson-10-4', 'Modulus and Dictionaries', 'The modulus operator (%) works like a clock, returns the remainder. A dictionary contains a set of key/value pairs.'],
    			['lesson-10-5', 'Validation', 'Validating user input is one way to protect web applications from being hacked and improve security; string substitution and HTML escaping.'],
    			['lesson-10-6', 'Templates', 'Templates separate different types of code, allow for more readable and modifiable code, and help to create more secure websites. Also, since templates provide the structure of a webpage, they can be reused again and again with different content and thus help reduce unnecessary repetition.']
    
   
				]

          











