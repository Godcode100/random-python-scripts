import logging
from operator import add,sub,mul,truediv
import sys

logging.basicConfig(filename='log.txt',level=logging.INFO)


def Calculator(a,b,op):
    a = float(a)
    b = float(b)

    if op == "+":
        return add(a,b)
    elif op == "-":
        return sub(a,b)
    elif op == "*":
        return mul(a,b)
    elif op == "/":
        return truediv(a,b)
    else:
        raise NotImplementedError(f"{op} operation not supported")

print("""Calculator Use POSTFIX NOTATION CTRL C OR CTRL D TO QUIT""")

while True:
    try:
        equation = input("").split()
        result = Calculator(*equation)
        print(result)
    except NotImplementedError as e:
        print("<!> INVALID OPERATOR")
        logging.debug(e)
    except ValueError as e:
        print("<!> expected format: <A>,<B>,<OP>")
        logging.exception(e)
        raise 
    except TypeError as e:
        print("<!> Wron number of arguments: <A>,<B>,<OP>")
        logging.debug(e)
    except ZeroDivisionError as e:
        print("Cannot Divide by Zero")
        logging.debug(e)
    except(KeyboardInterrupt,EOFError):
        print("n\Goodbye")
        sys.exit(0)
    except Exception as e:
        logging.exception(e)
        raise
