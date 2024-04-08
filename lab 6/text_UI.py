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
            #bolded visuals and general UI
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
            if(user == 'E'): #end code
                loop = False
                break
            elif(user == 'L'):
                file = input("Please enter the name of your file: ")
                try:
                    attribute = input("Please enter the attribute to use as a filter: ")
                
                    if(attribute != 'All'):
                        value = input("Please enter the value of the attribute: ")
                        data = load_data.calculate_health(load_data.load_data(file, (attribute, value)))
                    elif(attribute == 'All'):
                        data = load_data.calculate_health(load_data.load_data(file, (attribute, '')))

                    if(data != []):
                        print('Data loaded')
                except KeyError:
                    print('Invalid Key...')
                
                
            
            else:
                if(user not in ('S', 'C', 'H', 'E')): #if not selected options
                    print('Invalid Command.')
                elif data == []: #check if file has been loaded first
                    print('File not loaded. Please, load a file first.')
                elif(user == 'S'): #sort function
                    attribute = input("Please enter the attribute to sort: 'Agility', 'Armor', 'Intelligence', 'Health': ")
                    if(attribute in ('Agility','Armor','Intelligence','Health')):
                        order = input("Ascending (A) or Descending (D) order: ").capitalize()

                        data = sort.sort(data, order, attribute)
                        display = input("Data Sorted. Do you want to display the data?: ").capitalize()
                    
                    if(display == 'Y'): #display data
                        print(data)

                elif(user == 'C'): #curve fit function
                    attribute = input("Please enter the attribute you want to use to find the best fit for Health: ")
                    order = input("Please enter the order of the polynomial to be fitted: ")
                    poly = curve_fit.curve_fit(data, attribute, order)
                    print(poly)

                elif(user == 'H'): #histogram function
                    attribute = input("Please enter the attribute you want to use for plotting: ")
                    histogram.histogram(data, attribute)


        except FileNotFoundError:
            print("File not found.")


text_UI()
