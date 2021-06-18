def math(a,b):
          print("Addition of two numbers :",a+b)
          print("Subtraction of two numbers :",a-b)
          print("Multplication of two numbers :",a*b)
          print("Division of two numbers :",a/b)
a=float(input("Enter the first value : "))
b=float(input("Enter the second value : "))
math(a,b)


def covid(PatientName,BodyTemperature):
          if BodyTemperature < str(0) :
                default=str(98)
                print("Patient Name is ",PatientName," Body Temperature is ",default)
          else:
               print("Patient Name is ",PatientName," Body Temperature is ",BodyTemperature)
covid("Sneha","") 
covid("Sneha","98")