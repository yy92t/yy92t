def fn1(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Writing detailed information about the error in log files")
        raise

try:
    a = fn1(1,0)
    b = a * 10
    print(b)
except Exception as ex:
    print("Error occured in calculation :",type(ex).__name__)

print("\n############\n")
   
class CalculationError(Exception):
    pass

def fn2(s):
    try:
        return float(s)
    except ValueError:
        print("Writing detailed information about the error in log files")
        raise CalculationError()

try:
    a = fn2("10")
    b = fn2("1a1")
    c = a + b
    print(c)
except CalculationError as ex:
    print("Calculation aborted. Please refer to log file for details")
