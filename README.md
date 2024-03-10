# BAC CALCULATOR
#### Video Demo:  <https://www.youtube.com/watch?v=iVBfazqebNI>
#### Description:

The Application, AZN Converter, written in Python, calculates exchange values of the currencies using the latest rates given by the Central Bank of Azerbaijan.

#### project.py
##### Data
Firstly, a get request is made to retrieve the html code of https://cbar.az/currency/rates page, which has the link to the latest xml file containing the data. The reason is, the link itself is not something like current.xml, but rather in dd.mm.yyyy format, and only is updated if it is a working day in Azerbaijan. So, instead of using something like `datetime`, the program rely on the CBAR to update the page that contains the link, and it uses a regular expression to extract it and with another request, it then retrieves the necessary data. The program will quit on both `request`s, if any `Exception` raises.


xml file is parsed with xml.etree.ElementTree, and stored in a list of dictionaries named `rates` with following keys: unit, code and value. Conversions have been made for unit to be 1 on currencies where it was 100.

##### ask_which_way
It is a function that asks for input in a while loop and returns if the input is one of "to", "from" or "exit"

If the return value is "to" or "from", the conversations to or from AZN will be made, respectively. If the return value is "exit", the program will quit.


###### convert
The convert function starts with asking the user for an input for the amount in a while loop. It returns if the input is a value that can be converted to a float or the program quits if the input is "exit".

Next is, input for the currency code, again in a while loop. If the input matches the value of the `code` of any currencies in the list, it assigns that currency's value to a new currency_value variable.

oz variable is generated with ounce_prepend function which will be covered in the next section.

The function then returns the resulting text to be printed on the terminal, formatted accordingly.

CBAR doesn't provide exchange rate for every possible currency. The function prints the list of supported currencies, if the input does not match any of the values of the `code` key in the `rates` list and it is not "exit". 

The program quits if the input is "exit".

###### ounce_prepend
Precious metals' code and only their code start with the letter X and they are measured in troy ounces. Using these, the the ounce_prepend function returns "troy ounce of " or "troy ounces of " using `inflect` library either before the inputted amount or the result of calculation depending on `mode`.


##### exit_app
This function quits the program. It exists, so, it can be managed from one place, if any change is required on exit calls across the program.


#### test_project.py
##### test_ask_which_way
This test tests ask_which_way function. MonkeyPatch is necessary because, the function has input in it.

##### test_ounces_prepend
This test tests ounce_prepend function.

##### test_convert
convert function relies on two inputs, one argument and one global variable. Because of this, test_convert has to implement mock values.
