#Nicholas Terrazas and Devin Heinemann
#02/23/2026
#Description:


class Contact:
    """
    Represents a contact with the information: first name, last name, phone number, address, city, and zip code.

    Attributes: _f_name, _l_name, _phone, _address, _city, _zip.
    """

    def __init__(self, fn, ln, ph, addr, city, zip):
        """
        Creates a contact object with the provided information. Assigns all parameters to their corresponding attributes.
        
        Parameters: first name, last name, phone number, address, city, and zip code.
        """
        
        #Assigns each parameter to its corresponding attribute.
        self._f_name = fn
        self._l_name = ln
        self._phone = ph
        self._address = addr
        self._city = city
        self._zip = zip


    def __lt__(self, other):
        """
        Compares a contact to another to determine if the current contact should be sorted before the other contact. 
        Will compare by last name, unless they are the same, then will compare by first name.
        
        Parameters: other - another contact object to compare to the current contact.

        Returns: True if the current contact should be sorted before the other contact, False otherwise.
        """

        #Checks if last names are the same.
        if self._l_name == other._l_name:
            #If the last names are the same, then compares by the first names.
            if self._f_name < other._f_name:
                return True
            else:
                return False
        #If the last names are not the same, then compares by the last names.
        else:
            if self._l_name < other._l_name:
                return True
            else:
                return False
    

    def __str__(self):
        """
        Creates a string for display purposes, representing the contact with all their information.
        
        Returns: A string representing the contact for display purposes.
        """

        #to be displayed, returns a string representing the contact with all their information.
        return f"{self._f_name} {self._l_name}\n{self._phone}\n{self._address}\n{self._city} {self._zip}\n"


    def __repr__(self):
        """
        Creates a string that is used to write the contact to the file in the format:
        "f_name,l_name,phone,address,city,zip"
        
        Returns: A string representing the contact for writing purposes.
        """

        #to be written to the file, returns a string representing the contact with all their information.
        return f"{self._f_name},{self._l_name},{self._phone},{self._address},{self._city},{self._zip}"