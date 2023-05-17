def getString(message):
    while True:
        text = input(message).strip()
        
        if len(text) != 0: 
            return text
        else:
            print("Please input a valid string!!!")
        
def getNumber(message, minValue, maxValue):
    while True:
        try:
            number = int(input(message))
        except ValueError:
            print("You have to input a number!!!")
        else:
            if isinstance(number, int) and number >= minValue and number <= maxValue:
                return number
            else:
                print(f"Invalid value! Please select value from {minValue} to {maxValue}")

def getByOption(message, options):
    while True:
        text = input(message).strip()
        
        if text in options: 
            return text
        else:
            optionsText = ", ".join(options)
            print(f"Please just input one of these options: {optionsText} !!!")