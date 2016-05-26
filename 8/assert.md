## Assertions

An assertion is a sanity-check for testing of the program.

Assertions is like raise-if-not statement. 

An expression is tested, and if the result comes up false, an exception is raised.

Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output.

The syntax for assert is:

    assert Expression[, Arguments]

If the assertion fails, Python uses ArgumentExpression as the argument for the AssertionError. AssertionError exceptions can be caught and handled like any other exception using the try-except statement, but if not handled, they will terminate the program and produce a traceback.



    #!/usr/bin/python

    def KelvinToFahrenheit(Temperature):
       assert (Temperature >= 0),"Colder than absolute zero!"
       return ((Temperature-273)*1.8)+32

    print KelvinToFahrenheit(273)
    print int(KelvinToFahrenheit(505.78))
    print KelvinToFahrenheit(-5)


