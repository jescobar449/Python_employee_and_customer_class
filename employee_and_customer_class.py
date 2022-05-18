#Name: Jose Melquiades Escobar

#Employee class
class Employee:

    #__init__ to initializes the attributes.
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    #Define all accessor methods
    def get_name (self):
        return self.__name
    def get_id_number (self):
        return self.__id_number
    def get_department (self):
        return self.__department
    def get_job_title (self):
        return self.__job_title


#Define main()
def main ():

    #Creates three Employee objects 
    susan = Employee ('Susan Meyers', 47899, 'Accounting', 'Vice President')
    mark = Employee ('Mark Jones', 39119, 'IT', 'Programmer')
    joy = Employee ('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

    #Display the data for each employee
    print ('---Employee.py---')
    print ('Employee 1:')
    print ('Name: ', susan.get_name())
    print ('ID number: ', susan.get_id_number())
    print ('Department: ', susan.get_department())
    print ('Title: ', susan.get_job_title())
    print ('')
    print ('Employee 2:')
    print ('Name: ', mark.get_name())
    print ('ID number: ', mark.get_id_number())
    print ('Department: ', mark.get_department())
    print ('Title: ', mark.get_job_title())
    print ('')
    print ('Employee 3:')
    print ('Name: ', joy.get_name())
    print ('ID number: ', joy.get_id_number())
    print ('Department: ', joy.get_department())
    print ('Title: ', joy.get_job_title())
    print ('')
    print ('')


main()


#########################################################################

#Person class
class Person:

    #__init__ to initializes the attributes.
    def __init__ (self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    #Define all accessor methods
    def get_name (self):
        return self.__name
    def get_address (self):
        return self.__address
    def get_phone_number (self):
        return self.__phone_number

    #Define all mutator methods
    def set_name (self, name):
        self.__name = name
    def set_address (self, address):
        self.__address = address
    def set_phone_number (self, phone_number):
        self.__phone_number = phone_number

#Customer Class
class Customer(Person):
    def __init__ (self, name, address, phone_number, customer_number, mailing_list):
        Person.__init__ (self, name, address, phone_number)
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    #Defina all accessor methods
    def get_customer_number (self):
        return self.__customer_number
    def get_mailing_list (self):
        return self.__mailing_list

    #Define all mutator methods
    def set_customer_number (self, customer_number):
        self.__customer_number = customer_number
    def set_mailing_list (self, mailing_list):
        self.__mailing_list = mailing_list


#Define main()
def main ():

    #Declare local variables
    user_mailing_list = 'none'

    #Ask user for customer's information
    print ('')
    print ('')
    print ('---Customer.py---')
    user_name = input ('Enter the name: ')
    user_address = input ('Enter the address: ')
    user_phone_number = input ('Enter the phone_number: ')
    user_customer_number = input ('Enter the customer_number: ')
    #Boolean for mailing list 
    while user_mailing_list == 'none':
        user_mailing_list = input ('Does the customer wish to be on the maililng list? (Yes/No): ')
        if user_mailing_list == 'Yes': 
            user_mailing_list = True
        elif user_mailing_list == 'No':
            user_mailing_list = False
        else:
            print ('Yes or No are the only options accepted')
            user_mailing_list = 'none'
            
    #Assign the user's input to the customer
    new_customer = Customer (user_name, user_address, user_phone_number, user_customer_number, user_mailing_list)
    

    #Display the customer's information
    print ('')
    print ('Customer Information:')
    print ('Name:', new_customer.get_name())
    print ('Address:', new_customer.get_address())
    print ('Phone number:', new_customer.get_phone_number())
    print ('Customer Number:', new_customer.get_customer_number())
    print ('On Mailing List:', new_customer.get_mailing_list())


main ()





