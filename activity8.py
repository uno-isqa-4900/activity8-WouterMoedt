import csv


class Customer:
    # Constructor with attributes of the csv file
    def __init__(self, cust_id, first_name, last_name, company_name, address, city, state, zip):
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

# Displays the title of the program
def display_title():
    print('Customer Viewer')
    print('---------------')


def csv_reader():
    # Create an empty list to store the customer data in
    customers = []
    # Open the csv file with the reader object
    with open('customers.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        # Append csv data to customers list and return
        for row in reader:
            customer =  Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            customers.append(customer)
    return customers


def find_customer():
    customers = csv_reader()
    # Try exception handler
    # If the user enters something other than a number, the user is prompted to enter a number again
    try:
        cust_id_input = int(input("Enter Customer ID: "))
    except:
        cust_id_input = int(input("Enter Customer ID as a number: "))

    # If the customer ID is larger than 0 (and thus valid), print results for that ID
    if cust_id_input >0:
        customer = customers[cust_id_input-100]
        # If the customer ID does not have company information, exclude the company row from the result
        if customer.company_name == "":
            print('Customer information: ' + '\n\n' +
                  customer.first_name + ' ' + customer.last_name + '\n' +
                  customer.address + '\n' +
                  customer.city + ' ' + customer.state + ' ' + customer.zip + '\n')
        # If the customer ID has company information, include the company row in the result
        if customer.company_name != "":
            print('Customer information: ' + '\n\n' +
                  customer.first_name + ' ' + customer.last_name + '\n' +
                  customer.company_name + '\n' +
                  customer.address + '\n' +
                  customer.city + ' ' + customer.state + ' ' + customer.zip + '\n')
    # Display an error message if a negative number is entered
    elif cust_id_input <=0:
        print('Customer ID should be larger than 0. Please try again.')
    # Display an error message for other invalid entries
    else:
        print('This customer ID could not be found. Please try again.')

def main():
    # Call the display_title() function to be displayed
    display_title()

    # Loop to ask user for new input
    choice = 'y'
    while choice.lower() == 'y':
        find_customer()
        choice = input("Continue(y/n)? ")

        if choice == 'n' or choice == 'N':
            print()
            print("Bye!")
            print()
            break

if __name__ == '__main__':
    main()