from typing import Generator
from usefulgen.modules.basic import *
import itertools

def Wordlist(*, charset:str=None ,length:int=None, show_amount_combinations:bool=False) -> Generator[str, None, None]:
    """
    Generates a huge amount of strings combinations depending on the given length or on the given charset
    \n
    **You can use only one parameter (charset or length) at the same time!**
    \n
    This function must be used with **named parameters** like : Wordlist(charset="hello")
    
    :param charset: String charset that will be used to generate words with the same pattern. **It is case sensitive and the order of your pattern matters**. Example of charset: "qWert1" will generate a list containing for example "hEllo5"
    :type charset: str, optional
    :param length: Integer that will be used to generate words of this length. This is **not the best way to generate words** (please consider using **charset**)
    :type length: int, optional
    :param show_amount_combinations: If True, will print out the amount of combinations that will be generated in the process. **False by default**
    :type show_amount_combinations: bool, optional, default=False
    :raises TypeError: If charset and length are both empty
    :raises TypeError: If both charset and length are given by the user
    :raises TypeError: If length is given but is not an integer
    :raises ValueError: If length is given but is not higher than 0
    :raises TypeError: If charset is given but is not a string
    :raises TypeError: If show_amount_combinations is not empty but is not a boolean
    :return: A generator yielding words depending on your parameters
    :rtype: Generator[str]
    """
    if charset is None and length is None:
        raise TypeError(f"Only one on two parameters must be filled (charset or length)")
    elif charset is not None and length is not None:
        raise TypeError(f"Only one on two parameters must be filled (both {charset} and {length} were provided)")
    elif length is not None:
        if not isinstance(length, int):
            raise TypeError(f"Expected integer, received {length}")
        elif length <= 0:
            raise ValueError(f"length ({length}) must be higher than 0")
    elif charset is not None:
        if not isinstance(charset, str):
            raise TypeError(f"Expected string, received {charset}")
    elif show_amount_combinations is not None and not isinstance(show_amount_combinations, bool):
        raise TypeError(f"Expected boolean type as show_amount_combinations, received \'{show_amount_combinations}\'")

    # Is used only if charset is not None-type
    def DefineCharset(string:str) -> list:
        local_charset:list = []

        generators = list(lowerLatinAlphabet()), list(upperLatinAlphabet()), list(symbols()), list(symbolsCountrySpecific()), list(str(i) for i in numbers(0,9))
        for char in string:
            for gen in generators:
                if char in gen:
                    local_charset.append(gen)
                    break
                elif gen == generators[-1]:
                    raise ValueError(f"\"{char}\" is not a valid character")
        return local_charset

    # Is used only if length is not None-type
    def AllCharset() -> list:
        local_charset:list = []
        for base_list in [list(lowerLatinAlphabet()), list(upperLatinAlphabet()), list(symbols()), list(symbolsCountrySpecific()), list(str(i) for i in numbers(0,9))]:
            for element in base_list:
                local_charset.append(element)
        return local_charset

    lcharset:list = list(AllCharset()) if charset is None else list(DefineCharset(string=charset))

    if show_amount_combinations:
        if length is None:
            print(f"Generating {len(lcharset)**len(charset)} combinations...")
        else:
            print(f"Generating {len(lcharset)**length} combinations...")
    
    if charset is None:
        for combination in itertools.product(lcharset, repeat=length):
            yield ''.join(combination)
    else:
        for combination in itertools.product(*lcharset):
            yield ''.join(combination)
