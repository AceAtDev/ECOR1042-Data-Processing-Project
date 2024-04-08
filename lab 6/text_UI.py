# ECOR 1042 Lab 6 - Template text UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Jett Miyasaki"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101309152"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-089"

#==========================================#
# Place your script for your text_UI after this line
import sort
import load_data
import curve_fit
import histogram

def text_UI():
    loop = True
    data = []
    while(loop == True):
        try:
            print("The available commands are:")
            print("\033[1mL)\033[0m oad Data")
            print("\033[1mS)\033[0m ort Data")
            print("\033[1mC)\033[0m urve Fit")
            print("\033[1mH)\033[0m istogram")
            print("\033[1mE)\033[0m xit")
            print("")
            user = input("Please type your command: ")
            user = user.capitalize()

            #check user input for option selected
            if(user == 'E'):
                loop = False
                break
            elif(user == 'L'):
                file = input("Please enter the name of your file: ")
                try:
                    attribute = input("Please enter the attribute to use as a filter: ")
                except KeyError:
                    print('Invalid Key...')

                if(attribute != 'All'):
                    value = input("Please enter the value of the attribute: ")
                    data = load_data.calculate_health(load_data.load_data(file, (attribute, value)))
                elif(attribute == 'All'):
                    data = load_data.calculate_health(load_data.load_data(file, (attribute, '')))

                if(data != []):
                    print('Data loaded')
                
                
            #check if file has been loaded first
            else:
                if(user not in ('S', 'C', 'H', 'E')):
                    print('Invalid Command.')
                elif data == []:
                    print('File not loaded. Please, load a file first.')
                elif(user == 'S'):
                    attribute = input("Please enter the attribute to sort: 'Agility', 'Armor', 'Intelligence', 'Health': ")
                    if(attribute in ('Agility','Armor','Intelligence','Health')):
                        order = input("Ascending (A) or Descending (D) order: ").capitalize()

                        data = sort.sort(data, order, attribute)
                        display = input("Data Sorted. Do you want to display the data?: ")
                    
                    if(display == 'Y'):
                        print(data)

                elif(user == 'C'):
                    attribute = input("Please enter the attribute you want to use to find the best fit for Health: ")
                    order = input("Please enter the order of the polynomial to be fitted: ")
                    poly = curve_fit.curve_fit(data, attribute, order)
                    print(poly)

                elif(user == 'H'):
                    attribute = input("Please enter the attribute you want to use for plotting: ")
                    histogram.histogram(data, attribute)


        except FileNotFoundError:
            print("File not found.")



text_UI()
