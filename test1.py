import logging
logging.basicConfig(filename = 'string.log', level = logging.DEBUG, format = '%(asctime)s %(levelname)s %(name)s %(message)s')

class string_assignment:
    def extract_string(self,ext_string):
        """Extraction of a string"""
        logging.info("We are extracting a string from 1st index to 300th index with a jump of 3")
        self.ext_string = ext_string
        try:
            if len(ext_string) == 0:
                raise ValueError("Empty String")
                logging.error("Please provide a valid input")

            else:
                strng = ext_string[::3]
                logging.info("Extracted string is %s", strng)
                return strng

        except Exception as e:
            logging.exception(e)

    def rev_string(self, reverse_string):
        """Reversal of a string"""
        logging.info("This function will reverse the given string")
        self.reverse_string = reverse_string
        try:
            if len(reverse_string) == 0:
                raise ValueError("Empty String")
                logging.error("Please provide a valid input")

            else:
                rev_str = reverse_string[::-1]
                logging.info("Reversed string is: %s", rev_str)
                return rev_str

        except Exception as e:
            logging.exception(e)

    def capitalize_string(self,cap_string):
        """This function will convert the given string into upper case"""
        logging.info("Capitalize the string")
        self.cap_string = cap_string
        try:
            if len(cap_string) == 0:
                raise ValueError("Empty String")
                logging.error("Please enter a valid string")

            else:
                upper_string = cap_string.upper()
                logging.info("Upper string: %s", upper_string)
                return upper_string

        except Exception as e:
            logging.exception(e)

    def split_string(self,s_string):
        """This function will first capitalize the input string and then split it"""
        logging.info("Capitalize and then Split up the given string")
        self.s_string = s_string

        try:
            if len(s_string) == 0:
                raise ValueError("Empty String")
                logging.error("Please provide a valid string.")

            else:
                result = s_string.upper()
                logging.info("Upper case string is: %s", result)
                final_result = result.split(' ')
                logging.info("Final output is: %s", final_result)
                return final_result

        except Exception as e:
            logging.exception(e)

    def lower_string(self, l_string):
        """This function will convert the input string into lower case."""
        logging.info("Make String into Lower Case")
        self.l_string = l_string

        try:
            if len(l_string) == 0:
                raise ValueError("Empty String")
                logging.error("Please Enter a valid string")

            else:
                result = l_string.lower()
                logging.info("Converted string is %s", result)
                return result

        except Exception as e:
            logging.exception(e)


sp_string = string_assignment()
output_str = sp_string.split_string("this is My First Python programming class and i am learNING python string and its function")
print(output_str)
