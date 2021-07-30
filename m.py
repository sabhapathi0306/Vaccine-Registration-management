import re
 
# Function to validate Aadhar
# number.
s = "148346873265"
s1 = s[:4]+" "+s[4:8]+" "+s[-4:]

def isValidAadharNumber(str):
    
        # Regex to check valid
        # Aadhar number.
        regex = ("^[2-9]{1}[0-9]{3}\\" +
                "s[0-9]{4}\\s[0-9]{4}$")
        
        # Compile the ReGex
        p = re.compile(regex)
    
        # If the string is empty
        # return false
        if (str == None):
            return False
    
        # Return if the string
        # matched the ReGex
        if(re.search(p, str)):
            return True
        else:
            return False
aa = isValidAadharNumber(s1)
if(len(s) != 12 or aa != True):
    print("enetr correct numebr")
    



