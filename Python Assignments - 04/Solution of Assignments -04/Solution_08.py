"""
8. Write a Python function called `temperature_converter` that takes a temperature value and a 
string representing the scale (‘C’ for Celsius or ‘F’ for Fahrenheit) as input. 
The function should convert the temperature from one scale to the other using nested functions and 
return the converted value.
"""


def temperature_converter(temp,scale):
      def c_to_f(c):
            return (c * 9/5) + 32
      def f_to_c(f):
            return (f - 32) * 5/9
      
      if scale == "C":
            return c_to_f(temp)
      elif scale == "F":
            return f_to_c(temp)
      else:
            return "Invalid"

temp = float(input("Enter temperature :"))
scale = input("Enter Scale (C for Celsius or F for Fahrenheit) : ").upper()

result = temperature_converter(temp, scale)
print("Temperature : ",result)