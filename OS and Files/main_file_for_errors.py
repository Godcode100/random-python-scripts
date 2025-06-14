from python_programs.multi_inheritor import Grand_child

import file_for_errors
def main():
    file_for_errors.PrintErrors(ArithmeticError)
    me=dir(file_for_errors)
    you = dir(file_for_errors.PrintErrors)
    for i,x in file_for_errors.__builtins__.items():
        print(f"key::{i}, value::{x}")
    print(me)
    print(you)
    
if __name__ =='__main__':
    main()