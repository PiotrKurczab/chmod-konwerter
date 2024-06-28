import sys
import chmodconverter_functions as chmodconverter

def main():
    if len(sys.argv) != 3:
        print("Użycie: chmodconverter -s SYMBOLICZNY | -n NUMERYCZNY")
        sys.exit(1)
    
    option = sys.argv[1]
    value = sys.argv[2]
    
    if option == '-s':
        print(chmodconverter.symbolic_to_numeric(value))
    elif option == '-n':
        print(chmodconverter.numeric_to_symbolic(value))
    else:
        print("Nieznana opcja. Użycie: chmodconverter -s SYMBOLICZNY | -n NUMERYCZNY")
        sys.exit(1)

if __name__ == "__main__":
    main()