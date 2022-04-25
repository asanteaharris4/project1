import sys
from student import Student

def main(args=None):
    """
        This program that parses the command line, creates a
        Student, and prints a description of the student to
        standard out by invoking its toString method.
    """
    if args is None:
        args = sys.argv[1:]
        # check number of args
    if len(sys.argv) < 3:
        print("Few or no command line arguments")
        exit(0)
    else:
        name, gpa, classes= parse_cli_argv(argv)
        student= Student(name, gpa, classes)
        print(f"{student.__str__()}")

def parse_cli_argv(argv):
        #extract each arg starting with name
        name = argv[0]
        gpa= argv[1] #extract GPA
        classes= argv[2:] #extract class names

        return name, gpa, classes


    
if __name__ == "__main__":
    main()