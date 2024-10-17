from typing import Generator
from usefulgen.modules.basic import *
import itertools

def Wordlist(charset:str ,length:int, *, strict:bool=False, show_amount_combinations:bool=False) -> Generator[str, None, None]:
    """
    Generates a huge amount of strings combinations of a given length using a given charset, will use only the chars from the charset (if strict=True) or their type (if strict=False)
    \n
    Examples of usage:
    \n
    Wordlist("H",3, strict=False) --> First combination: AAA | Last combination: ZZZ | Other combination: OAL
    \n
    Wordlist("Hello",4, strict=True) --> First combination: HHHH | Last combination: oooo | Other combination: ollH
    
    :param charset: String charset that will be used to generate words with the same pattern. **It is case sensitive**.
    :type charset: str, list of different types of chars when strict=False -> a, A, 1, !, é
    :param length: Integer that will be used to generate words of this length.
    :type length: int
    :param strict: If True, only the character present in the charset will be used. If False, it will use the same kind of chars as the charset. **False by default**
    :type strict: bool, optional, default=False
    :param show_amount_combinations: If True, will print out the amount of combinations that will be generated in the process. **False by default**
    :type show_amount_combinations: bool, optional, default=False
    :raises TypeError: If charset or length is empty
    :raises TypeError: If length is given but is not an integer
    :raises ValueError: If length is given but is not higher than 0
    :raises TypeError: If charset is given but is not a string
    :raises TypeError: If strict is not empty but is not a boolean
    :raises TypeError: If show_amount_combinations is not empty but is not a boolean
    :return: A generator yielding words depending on your parameters
    :rtype: Generator[str]
    """
    if charset is None or length is None:
        raise TypeError(f"Both parameters must be filled (charset and length)")
    elif not isinstance(length, int):
        raise TypeError(f"Expected integer, received {length}")
    elif length <= 0:
        raise ValueError(f"length ({length}) must be higher than 0")
    elif not isinstance(charset, str):
        raise TypeError(f"Expected string, received {charset}")
    elif strict is not None and not isinstance(strict, bool):
        raise TypeError(f"Expected boolean type as strict, received \'{strict}\'")
    elif show_amount_combinations is not None and not isinstance(show_amount_combinations, bool):
        raise TypeError(f"Expected boolean type as show_amount_combinations, received \'{show_amount_combinations}\'")

    def __DefineCharset(string:str) -> list:
        local_charset:list = []

        generators = list(lowerLatinAlphabet()), list(upperLatinAlphabet()), list(symbols()), list(symbolsCountrySpecific()), list(str(i) for i in numbers(0,9))
        for char in string:
            for gen in generators:
                if char in gen and char not in local_charset:
                    for sample in gen:
                        if sample not in local_charset:
                            local_charset.append(sample)
                    break
                elif gen == generators[-1] and char not in local_charset:
                    raise ValueError(f"\"{char}\" is not a valid character")
        return local_charset

    lcharset:list = []
    if not strict:
        lcharset = list(__DefineCharset(string=charset))
    elif strict:
        lcharset = list(charset)

    if show_amount_combinations:
            print(f"Generating {len(lcharset)**length} combinations...")
    
    already_yield = []

    for combination in itertools.product(lcharset, repeat=length):
        if combination not in already_yield:
            already_yield.append(combination)
            yield ''.join(combination)