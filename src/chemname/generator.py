from chemname.constants import *

import re

def chemName(str):
    index = 0
    results = []

    if re.findall("[^A-Za-z]", str) != []:
        return None
    
    for symbol in ELEMENT_SYMBOLS:
        if re.findall(re.compile(f"^{symbol}", re.IGNORECASE), str):
            if len(symbol) == len(str):
                results.append([symbol])
            else:
                tempResults = []
                for tempResult in chemName(str[len(symbol):]):
                    tempResults.append([symbol] + tempResult)

                results.extend(tempResults)
    
    return None if results == [] else results