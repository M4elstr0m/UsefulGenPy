from typing import Generator

def upperLatinAlphabet() -> Generator[str, None, None]:
    """Generates a list of all the uppercase letters of the latin alphabet

    :return: A generator yielding each letters of the latin alphabet
    :rtype: Generator[str]
    """
    for i in range(65,91):
        yield chr(i)

def lowerLatinAlphabet() -> Generator[str, None, None]:
    """Generates a list of all the lowercase letters of the latin alphabet

    :return: A generator yielding each letters of the latin alphabet
    :rtype: Generator[str]
    """
    for i in range(97,123):
        yield chr(i)

def numbers(start:int, end:int) -> Generator[int, None, None]:
    """Generates a list of integers from 'start' to 'end' included without any leading zeros

    :param start: First integer of the list (inclusive)
    :type start: int
    :param end: Last integer of the list (inclusive)
    :type end: int
    :return: A generator yielding integers from 'start' to 'end' (inclusive)
    :rtype: Generator[int]
    :raises TypeError: If 'start' or 'end' is not an integer
    :raises ValueError: If 'start' is bigger than 'end'
    :raises ValueError: If 'start' or 'end' is not positive
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError(f"Both start ({start}) and end ({end}) must be integers")
    elif start >= end:
        raise ValueError(f"start ({start}) must be lower than end ({end})")
    elif start < 0 or end < 0:
        raise ValueError(f"Both start ({start}) and end ({end}) must be positive integers")
    
    for i in range(start,end+1):
        yield i

def numbersLeadingZeros(start:int, end:int, leading_zeros:int) -> Generator[str, None, None]:
    """Generates a list of strings of the integers from 'start' to 'end' included with the leading zeros
    
    :param start: First number of the list (inclusive)
    :type start: int
    :param end: Last integer of the list (inclusive)
    :type end: int
    :param leading_zeros: The number of leading zeros to add to a numerical sequence from right to left. For example, if leading_zeros=1, the sequence would be 1, 2, 3, ... If leading_zeros=2, the sequence would be 01, 02, 03, ...
    :type leading_zeros: int
    :return: A generator yielding strings of integers from 'start' to 'end' (inclusive)
    :rtype: Generator[str]
    :raises TypeError: If 'start', 'end' or 'leading_zeros' is not an integer
    :raises ValueError: If 'start' is bigger than 'end'
    :raises ValueError: If 'start', 'end' or 'leading_zeros' is not positive
    """
    if not isinstance(start, int) or not isinstance(end, int) or not isinstance(leading_zeros, int):
        raise TypeError(f"Both start ({start}), end ({end}) and leading_zeros ({leading_zeros}) must be integers")
    elif start >= end:
        raise ValueError(f"start ({start}) must be lower than end ({end})")
    elif start < 0 or end < 0 or leading_zeros < 0:
        raise ValueError(f"start ({start}), end ({end}) and leading_zeros ({leading_zeros}) must be positive integers")

    for i in range(start,end+1):
        i = str(i)
        while len(i) < leading_zeros:
            i = "0"+i
        yield i

def symbols(space:bool=True) -> Generator[str, None, None]:
    """Generates a list of all the most common symbols

    :param space: Determines if the space character (ASCII:32) will be yield or not
    :type space: bool, optional
    :return: A generator yielding each common symbols
    :rtype: Generator[str]
    :raises TypeError: If 'space' is not a boolean type
    """
    if not isinstance(space, bool):
        raise TypeError(f"space parameter ({space}) must be a bool-type (True/False)")

    if space:
        yield chr(32)
    for i in range(33,48):
        yield chr(i)
    for i in range(58,65):
        yield chr(i)
    for i in range(91,97):
        yield chr(i)
    for i in range(123,126):
        yield chr(i)

def symbolsCountrySpecific(country:str=None) -> Generator[str, None, None]:
    """Generates a list of all the letters considered as special characters from every country

    :param country: Determines the language from where the accents will be taken
    :type country: str, optional
    :return: A generator yielding each letters containing a special accents
    :rtype: Generator[str]
    :raises TypeError: If 'country' is not a string
    :raises ValueError: If 'country' is not supported (not in the countries list)
    """
    if country is not None:
        countries:dict = {
                "france":[192,194,196,198,199,200,201,202,203,206,207,212,217,219,220,224,226,228,230,231,232,233,234,235,238,239,244,249,251,252,338,339],
                "germany":[196,214,220,223,228,246,252],
                "italy":[192,200,201,204,210,217,224,232,233,236,242,249],
                "spain":[161,191,193,201,205,209,211,218,220,225,233,237,241,243,250,252]
                }

        if not isinstance(country, str):
            raise TypeError(f"country ({country}) is not a string type")
        elif str.lower(country) not in list(countries.keys()):
            raise ValueError(f"The country you entered ({country}) is not supported")
        
        for i in countries[str.lower(country)]:
            yield chr(i)

    else:
        yield chr(161)
        for i in range(191,215):
            yield chr(i)
        for i in range(216,222):
            yield chr(i)
        for i in range(223,247):
            yield chr(i)
        for i in range(248,253):
            yield chr(i)
        for i in range(338,340):
            yield chr(i)

def PiDecimals(start:int, end:int) -> Generator[int, None, None]:
    """Generates a list of a determined quantity of numbers after Pi's decimal
    
    :param start: Determines the start of the list after Pi's decimal (inclusive)
    :type start: int
    :param end: Determines the amount of numbers after Pi's decimal (inclusive)
    :type end: int
    :raises TypeError: If 'end' or 'start' is not int-type
    :raises ValueError: If 'end' or 'start' is < 1
    :raises ValueError: If 'start' is bigger than 'end'
    :return: A generator yielding numbers after Pi's decimal
    :rtype: Generator[int]
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError(f"Both start ({start}) and end ({end}) must be integers")
    elif start > end:
        raise ValueError(f"start ({start}) must be lower or equal than end ({end})")
    elif start < 1 or end < 1:
        raise ValueError(f"Both start ({start}) and end ({end}) must be >= 1")
    
    try:
        from decimal import Decimal, getcontext
    except ModuleNotFoundError or ImportError:
        raise ImportError("'decimal' module could not be imported. Since it is a built-in module, check your Python version!")

    validity = 5 # precalculates after x terms to insure the validity of the result
    
    def calc_pi(n:int) -> float:
        getcontext().prec = n+1  # Set the decimal precision to n+1
        pi = Decimal(0)
        for k in range(n):
            pi += (Decimal(1)/(16**k)) * (
                (Decimal(4)/(8*k+1)) -
                (Decimal(2)/(8*k+4)) -
                (Decimal(1)/(8*k+5)) -
                (Decimal(1)/(8*k+6))
            )
        return pi
    
    pi = str(calc_pi(end+validity))[2+start-1:-validity]
    for number in list(pi):
        yield int(number)