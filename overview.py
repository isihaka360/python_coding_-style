# Python Programming Style
# A goal of CS 1110 is for you to learn to write programs that are not only correct
# but also understandable. 
# These guidelines should help you toward that goal. 
# We ask that you follow these guidelines when writing programs in this course.
# They will give you a good basis for developing a style of your own as you become a more experienced programmer.

# This guide includes rules for Python constructs that will be covered later in the semester.
# Skim these sections now and read them more carefully later when the topics are discussed.

# Table of Contents
# @Purpose of Good Style
# @Code Layout
# @Naming Conventions
# @Comment Conventions
# @Statement Comments
# @Specifications
# @Attribution Comments

# @Purpose of Good Style
# Your program should be readable, because if it is not readable, the chances of it being correct are slim. Moreover, if your program is unreadable, it will be difficult and time-consuming to find and correct the errors in it. Therefore,

# Using a disciplined style of programming will save you time whenever you have to read your program or debug it.

# Your program should be readable by others, not just you. In this course, a grader who has trouble understanding it is not likely to give you good a grade. But this is important even outside of the course. Most programs live a long time and require maintenance – changes to adapt to new and different requirements, upgrades in other software, and new hardware. The author of the program is quite likely not going to be around when the maintenance is required, so someone else must read the program and understand it enough to update it successfully.
# Even the programs you write for yourself should be readable. We have found that even as short a time as four weeks after you finish an assignment is long enough for you to forget what you did in your own code.
# So for your own sake and for the sake of others, it makes sense to develop programming habits that support readable, understandable, and correct programs.
# Part of these habits concern simple, syntactical measures like using proper spacing, or using naming conventions. The more important part concerns recording enough information in comments for the reader to understand how a program is designed and why.
# Unlike Java, Python does not have a standardized format for writing function comments. 
# The style taught in class and outlined in this guide is modeled on the Java style, but adheres to Python guidelines for docstring comments. In particular, our style contains much more useful information than most Python documentation that you will see online.
# As you develop as a programmer, you may develop a style of your own. And different workplaces have different styles. But by practicing the programming style of this course you will develop the discipline to write clean and maintainable code.

# @Code Layout
# Many people do not think that Python requires a rules on code layout because Python must be properly formatted and indented in order to run.
# However, there are still some cases where a Python program will run, but not be well formatted.
# Tabs versus Spaces
# Python will allow you to indent with either tabs or spaces. 
# However, beginning programmers should always indent with spaces.
# This is what your editor Atom Editor does, and is standard practice in most code editors. 
# And whatever you do, you should absolutely *never mix tabs and spaces(. 
# Doing so will cause your program to crash.
# In this course you should always use 4 spaces for each indentation level.

# @Line Length
# In this course you should strive for a maximum of 79 characters per line.

# This convention is a historical artifact of the fact that older computers could only show 80 characters per line on the command prompt. This convention has persisted as people have become accustomed to this length, and it is now considered a “natural length” for a single line of code.

# While most code editors will wrap the text for you if you exceed this character limit, text wrapping occurs in inconvenient places and can be difficult to read. To make the code easier to read, it would be better for you to break up the lines yourself.

# In order to break up a line of code you need to put expressions in parentheses. You can then break up the code by putting line breaks inside of the parentheses. The following is acceptable Python code:

    # if (width ==0 and height == 0 and
    #     color == 'red' and emphasis == 'strong' or
    #     highlight > 100):      
# When using parentheses to break up code across multiple lines, it is standard practice to indent the lines so that they start just after the position of the initial parenthesis. 
# This is shown in the example above.

# @Blank Lines
# Because Python is whitespace significant, blanks lines should be used sparingly and to give the most emphasis to code divisions. 
# The following two important guidelines should be observed:
# -->Functions (and class definitions) should be separated by two blank lines.
# -->Methods (within a class definition) should be separated by a single blank line.
# In addition, you may use blank lines to separate logical sections of code within a function or method, but this should be done sparingly.

# In programming and writing code, a "--@blank line--" typically refers to a line that contains no visible characters.
# Blank lines are used to separate different sections of code or to provide visual clarity and improve readability.
# They do not contribute to the functionality of the code but serve as a means to structure and organize the code visually.

# Here are a few common uses of blank lines in code:
# 1.Separating Blocks of Code:
# Blank lines are often used to separate distinct blocks of code within a function, method, or program.
# This can make it easier to understand the logical structure of the code.
def example_function():
    pass
    # Block 1
    # statement_1
    # statement_2

    # Blank line for separation

    # Block 2
    # statement_3
    # statement_4
    
# 2.Improving Readability:
# Adding blank lines can enhance the overall readability of the code by creating visual breaks between different sections.
# This is particularly useful for long and complex code files.
 
    # Code for one feature
    ...

    # Blank line for separation

    # Code for another feature
    ...
      
# 3.Compliance with Style Guides:
# Many coding style guides, including PEP 8 for Python, recommend the use of blank lines to improve code readability.
# Following such style guides helps maintain consistency across projects and makes the code more accessible to other developers.  
# While blank lines are not executed or interpreted by the programming language, they play a crucial role in enhancing the human-readable aspect of code. 
# They help programmers organize their code in a clear and structured manner, making it easier to understand and maintain. 

# @Import Statements
# Imports should usually be on separate lines.
# The following code
import os
import sys
# is preferable to
import sys, os
# However, it is okay to use commas when importing multiple items from a single module.
# The following is acceptable:
from subprocess import Popen, PIPE
# The from keyword should be limited to imports that are used heavily within the current module, and which are guaranteed to not collide with any existing functions or variables.

# @Naming Conventions
# Good naming conventions can help you and any reader of a program understand the program easily, as they help indicate what the program should be doing. 
# Some people advocate using very long names that define what a named entity (variable, function, etc.) represents.
# However, this is not feasible since a good definition may require many lines of explanation.
# Thus, any style guideline must be a compromise.

# Unlike other programming languages, the naming conventions for Python are not standardized. 
# In any Python module, you might see the following mix of conventions:
# Lowercase: example
# Lowercase with underscores: example_in_python
# Uppercase: EXAMPLE
# Uppercase with underscores: EXAMPLE_IN_PYTHON
# CamelCase (each word in phrase is capitalized): ExampleInPython
# Lower CamelCase (CamelCase with first letter lower case): exampleInPython

# In order to maintain maximum clarity, we obey the following rules (which are standardized in Java, but accepted in Python too).

# Non-object oriented features (functions and global variables): use underscores.
# Object oriented features (classes and methods): use CamelCase.
# Class names: start with an uppercase letter
# All other names: are start with a lowercase letter.

# @Functions
# A function should be be named a verb phrase that gives some indication of what it does.
# However, this name should never be used as an excuse to omit a specification.
# This primarily includes procedures, though it could be true for fruitful functions as well.
# On the other hand, a function that simply returns a value (e.g. a fruitful function with no side effects) may use a noun phrase that describes the value.
# Determining which case applies can be a matter of taste.
# Functions should use either lowercase or lowercase with underscores (when the function name is a compound word)

# Examples: draw_oval, show_window, length, interest

#---> @Function Parameters
# The precise meaning of a parameter – and any restrictions on it – must be given in the function specification. 
# This is why long parameter names are unnecessary.
# short, it is wise to give parameters short names, and avoid compound words.
# All names should be lower case.
# For a more detailed example, consider the two method headings given below.
# The first is preferable because it is shorter and easier to understand.
# Notice how the change in variable names effects the length of the specification
def draw_oval(x, y, w, h):
        """
        Draws an ellipse that fits within the rectangle given.
      
        The upper left corner of the rectange is at position (x,y), 
        its width is w, and its height is h. The object uses the 
        current color to draw the ellipse.
        """
        
def draw_oval(x_coordinate, y_coordinate, width, height):
        """
        Draws an ellipse that fits within the rectangle given.
      
        The upper left corner of the rectange is at position 
        (x_coordinate,y_coordinate), its width is width, and 
        its height is height. The object uses the current color 
        to draw the ellipse.
        """       
        
# A parameter used as a flag should be named for what the flag represents, like selected, rather than simply flag.
# In addition, you should avoid generic names like value except in the case of a setter.       

# @Local Variables
# A local variable should be a noun phrase that describes the variable contents. Local variables should start with a lower case letter.
# You may either use underscores or CamelCase (depending on whether this is a class or a function), but you must be consistent throughout the function or method.
# For loop variables, or variables that are used only briefly, a short, one-or-two letter name can be used instead.
# A name like the_loop_counter or first_number instead of kk or x causes clutter. As long as the context of the variable is clear, use a short name.
# A variable used as a flag should be named for what the flag represents, like selected, rather than simply flag.
# In addition, you should avoid generic names like count or value Instead, describe the items being counted or the value stored in the variable.
# Examples: size, x_coordinate, no_lines

# @Global Variables
# Global variables should be reserved for constants (e.g. variables that do not change after their initial assignment). Standard practice for constants is to write them in upper case with underscores as needed.
# Unlike other languages, Python does not enforce constants.
# It is possible (but a bad idea) to change a constant variable. 
# This is an instance where the use of a naming convention is incredibly important.
# The user of uppercase indicates that it is a bad idea to change this variable.
# Examples: PI, Y, E, WINDOW_SIZE

# @Classes
# Since a class represents a set of possible objects, a class name should be a noun phrase that identifies the possible objects.
# The first letter is uppercase and compound names are written using CamelCase.
# Example: FilterInputStream, LivingMammals

# @-->Methods
# The guidelines for method names are similar to those for function names except that we use CamelCase (with first letter lowercase) rather than underscores.
# Methods that are hidden (e.g. should only be used as a helper method) should begin with an underscore.
# Examples: drawOval, fillOval, length, toString, _hiddenMethod

# @-->Method Parameters
# Methods follow the same rules for parameters that as functions.
# But in addition, the first parameter for an instance method should always be self.
# The first parameter for a class method should always be cls.

# @-->Attributes
# Attributes contain information that determine the state of their object.
# Therefore, an attribute name should be a noun phrase that describes what the attribute contains. 
# However, the attribute will still need to be described in the class specification.
# An attribute name should be CamelCase with with the first letter lowercase.
# Atributes that are hidden (e.g. are not accessed outside of the methods) should begin with an underscore.

# Examples: size, xCoordinate, noLines, _hiddenAttrib

#@--> Properties
# A property looks like an attribute, but it is really a collection of accessor methods (getters and setters) for manipulating an attribute. 
# A property typically corresponds to another hidden attribute. 
# Hence, the property name should be the same as the attribute name, but without the leading underscore.

# Examples: size, xCoordinate, noLines, hiddenAttrib

# @Comment Conventions
# Python has two types of comments: single line comments (which start with a # sign) and docstrings (which are enclosed in triple quotes).
# The following is a general rule regarding commenting:
        """ 
        Specifications are docstrings; all other comments are single line comments.
        
        """
#   You will see a lot of Python code that ignores this guideline. 
#   Do not emulate that code.

# @Statement Comments
# Single-line comments are never required.
# While they help make make code more maintainable, they do not serve the same software engineering role that specifications do.
# With that said, they do serve a useful role as statement comments.

# Just as essays are grouped in paragraphs, code should be grouped into logical units.
# A good unit should be one that can be described in a single sentence, and that sentence should be written as a single-line comment at the start of the unit.
# If a unit of code requires more than a sentence to describe, that means it is complicated enough to pull out as a separate function (with specification).      

# Here is an example of a code unit with a statement-comment:
  # Ensure that x >= y
  
  # Ensure that x >= y
#  here x and y are two Empty variables
x =None
y = None
if (x < y):
    tmp = x
    x = y
    y = tmp
    
""" Note that a statement comment should explain what the group of statements does, not how it does it.
     """
     
    #  NOTE:Each time you start a new unit or block of code, you should add a new statement comment.
    #  Here is an extended example with several a statement comments.
    
      # Eliminate whitespace from the beginning and end of t
      
    # while (len(t) != 0 and t[0].isspace()):
    #     t= t[1:]

    # # If t is empty, print an error message and return
    # if (len(t) == 0):
    #     ...
    #     return False;
    
    # # If t is a proper name, print a greeting.
    # if (contains_capitals(t)):
    #     ...

    # # Store the French translation of t in t_french
    
            # Sometimes people will add a comment to indicate the end of a code unit, like this
   # Ensure that x >= y
   #  here x and y are two Empty variables
x =None
y = None
if (x < y):
    tmp = x
    x = y
    y = tmp
    # End of ensure x >= y
    
            # However, as long as you are consistent about the use of statement comments, this can always be inferred from the next statement comment or the end of the function or method.
            
#  @Specifications
# Unlike statement comments, specifications are required. In Python, specifications are part of the help system and direct others how to use your module, function, or class.
# That is why it is important to format them properly.

# All specification comments, be they for a function, module, or class, follow the same format.
# They are a docstring enclosed in triple-quotes on either side. 
# They should start with a simple description that can fit on exactly one line.
# This should be followed by a blank line, and then a more detailed description of the specification.    
      
    #   For example, here is the beginning of the specification for the function draw_oval:
def draw_oval(x, y, w, h):
     """"
        Draws an ellipse that fits within the rectangle given.
      
        The upper left corner of the rectange is at position (x,y), 
        its width is w, and its height is h. The object uses the 
        current color to draw the ellipse. """  
        
#  Note that we do not go into detail about the parameters until after the blank line.
#  The goal is to make a first line that is as descriptive, but short, as possible.

# Sometimes the first line of the specification is enough information. 
# In that case, there is no need for the blank line, as shown in the example below:   
def clear():
        """
        Clears all shapes drawn on the screen.
        """  
        
# @Module Specifications
# Module specifications are extremely important for this course, particularly as they are typically the first thing that we read when we grade your assignments. 
# As they are a specification, they should use docstrings and must be the first thing in the file.
# In particular, this is the documentation that will display when you use the help() command on this module.

# Module specifications should obey the basic rules for specifications.
# That is, they should have a short single line, followed by a blank line and then a more detailed explantion.
# However, the difference is what to do at the end of the specification. 
# The last two lines of a module comment are special.
# The second to last line should be the name of the author (please include your netid).
# The last line should be the date that the file was last modified.

# Putting all of this together, here is an example of a module comment in full:

"""
Module to demonstrate basics of Python style

This module does not do anything interesting when it is loaded or run 
as an application.  The primary purpose of this module is to demonstrate 
good programming style in Python.

Authors: Walker White (wmw2), Lillian Lee (ljl2)
Version: August 24, 2019
"""           

# @Function Specifications
# Every function header should be followed by a docstring giving its specification.
# The specification comment should be a docstring, following the basic rules for specifications.
# It should be indented, just like the rest of the function body.
# For a fruitful function (i.e. one that returns a value other than None), the one-line summary should indicate what the function returns, as follows:
def dist(x1, y1, x2, y2):
    """
        Returns the distance between points (x1,y1) and (x2,y2)
        The end of a function specification should always describe the parameters of the function
        
        """
# Each parameter should be listed separately, with its own precondition. Here is an example: 

def find_common(t, c):
        """
        Prints the most frequently occurring temperature in t[0:c]. 
        
        If there is more than one possibility for the most frequently 
        occuring temperature, this function prints the least such.
        
        Parameter t: a sequence of temperature values in centigrade.  
        Precondition: t is a sequence of floats
        
        Parameter c: How far to search in the sequence t.
        Precondition: c is an int, 0 <= c < len(t)
        """
        
    # Sometimes preconditions are about a relationship between one or values. 
    # In that case the precondition should be mentioned with every parameter it applies to. For example: 
    
def rangelist(a, b):
     """
     Returns the list [a, ..., b]
        
     Parameter a: the first integer in the list
     Precondition: a is an int, a <= b
        
     Parameter b: the last integer in the list
     Precondition: b is an int, a <= b
     
     """    
     
# @Class Specifications
# Class specifications are docstrings that immediately follow the class header, shown as follows: 
class RGB(object):  
    """"
        A class representing a RGB color value.
        
        """    
        
# The specification is indented to the same level as attributes and methods in the class.
# It follows the basic rules for specifications.
# The first line should be a description of the type that the class represents.         
        
        # Attributes are documented as part of the class specification.
        # Attributes are documented like function parameters except that they have invariants instead of preconditions.
        # Here is an example of a class shown in lecture:
        
class Worker(object):
        """
        A class representing a worker in a certain organization
        
        Attribute lname: The worker last name
        Invariant: lname is a string

        Attribute ssn: The Social Security number
        Invariant: ssn is an int in the range 0..999999999
        
        Attribute boss: The worker's boss
        Invariant: boss is an instace of Worker, or None if no boss
        
        """   
        
#  Hidden attributes should not be part of the class specification. 
#  They are hidden. If those attributes have getters or setters, then their specification should be contained in those method specifications.
#  A purely internal attribute, with no getters and setters should be documented with single-line comments immediately after the specification. 
#  The format should be the same as in the specification comment.
#  Consider the following example:           
        
class Worker(object):
    """
    A class representing a worker in a certain organization
        
    Attribute lname: The worker last name
    Invariant: lname is a string

    Attribute boss: The worker's boss
    Invariant: boss is an instace of Worker, or None if no boss
     """
    ### HIDDEN ATTRIBUTES
    # Attribute _ssn: The Social Security number
    # Invariant: _ssn is an int in the range 0..999999999
    
# @Method Specifications
# Method specifications behave a lot like function specifications with one minor change.
# The parameter self should not be mentioned in the parameter list and it does not need a precondition.
# The precondition is implied by the fact that it is an instance method. 
# The same applies for cls and class methods.

# The only exception is for getters.
# Because a getter is accessing an invariant, the getter should always include the attribute invariant.
# The following is an example of a getter for a color object.

def getRed(self): 
    """
        Returns the red channel            
        Invariant: the value is an int between 0 and 255, inclusive.
        
        """
        
# @Properties
# Even though they act like attributes, properties do not go in the class specification. 
# Instead, the have their own separate specfications, written as a docstring.
# This docstring goes in the property getter (which should always appear in the property setter) and follows the same rules as a getter specification.
# However, it should not say Returns, but instead should word the summary line as a noun phrase, like any attribute.

# The following is an example of the documentation for the RGB class.   
# class RGB(object):    
#         @property
#     def red(self):
        
#         """
#         The red channel
            
#         Invariant: the value is an int between 0 and 255, inclusive.
#         """
#         return self._red
       
#     @red.setter
#     def red(self, v):
#         assert (v >= 0 and v <= 255), '%s is outside [0,255]' % repr(v)
#         assert (type(v) == int), '%s is not an int' % repr(v)
#         self._red = v      """
#      A class representing a RGB color value.
#      """


        
    
# Note that property setters do not require specifications. 
# The behavior is fully specified by the getter, and the decorator indicates which getter to use.    

# Attribution Comments
# In order to avoid plagiarism, you should always credit a co-author or source.
# Co-authors should be credited in the module specification. 
# If someone is not a co-author (e.g. they did not write code), but they influenced the code through other means, you should acknowledge this in the module specification.
# For example:

"""
Module to demonstrate basics of Python style

This module does not do anything interesting when it is loaded or run 
as an application.  The primary purpose of this module is to demonstrate 
good programming style in Python.

This module was written after a discussion with Steve Marschner (srm2), 
though he did not contribute any code.

Authors: Walker White (wmw2), Lillian Lee (ljl2)
Version: August 24, 2012
"""
# For specific algorithms or code fragments, the acknowledgement should be in the should be in the function specification.
# For example:

def collides(shape1, shape2):
        """
        Returns: True if shape1 and shape2 intersect
        
        This function implements the Gilbert-Johnson-Keerthi distance 
        algorithm, as described in the article:
        
            "A fast procedure for computing the distance between complex 
            objects in three-dimensional space", IEEE Journal of Robotics 
            and Automation, Vol 4. Issue 2, 1988.
        
        Parameter shape1: The first shape to test
        Precondition: shape1 is an object of class Shape
        
        Parameter shape2: The second shape to test
        Precondition: shape2 is an object of class Shape
        
        """
        
#  @Acknowledgments
# The ideas in this document originated in the structured-programming movement of the 1970’s.
# They are every bit as applicable today. Some of the examples and ideas were taken from old Cornell CS100 and and CS211 handouts, originating in the work of Richard Conway and David Gries (see their 1973 text on An Introduction to Programming, using PL/C). 
# Hal Perkins also had a hand in writing an earlier version of this document.

# The current version of this document was written by Walker White, several years after converting CS1110 to Python. 
# This transition required a significant change in specification comments, particularly regarding class specifications.
# In developing these style guidlines, he incorporated many of the official style conventions outlined in PEP 257. 
# Some of the examples here come from that article.
# In addition, the style for formatting preconditions and invariants was inspired by the Sphinx documentation tool.       
        