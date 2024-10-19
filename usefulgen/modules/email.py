from typing import Generator
#from usefulgen.modules.basic import *

def EmailGenerate(
        *,
        firstname:str=None,
        lastname:str=None,
        nationality:str=None,
        domain:str=None,
        birthday_year:str=None,
        pseudonym:str=None,
        nickname:str=None,
        pet:str=None
        ) -> Generator[str, None, None]:
    """
    Generates all possible emails using the given informations
    """
    # Type checking
    for parameter in [firstname,lastname,nationality,domain,birthday_year,pseudonym,nickname,pet]:
        if not isinstance(parameter, str) and parameter is not None:
            raise TypeError(f"Expected string-type as argument received \"{parameter}\"")
    
    def __DictDomainsByCountry() -> dict:
        """Created to save memory when executing code"""
        DomainsByCountry:dict = { # Domain only OR all + nationality if there is no Domain
            "_all":["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com", "@icloud.com", "@live.com", "@proton.me", "@protonmail.com"],
            "at":["@gmx.at", "@aon.at", "@live.at", "@outlook.at"],
            "be":["@live.be", "@outlook.be", "@hotmail.be"],
            "ca":["@live.ca", "@hotmail.ca"],
            "ch":["@gmx.ch", "@hotmail.ch"],
            "cl":["@live.cl", "@outlook.cl"],
            "cn":["@live.cn", "@123.com", "@126.com", "@163.com"],
            "cz":["@yahoo.cz", "@outlook.cz"],
            "de":["@yahoo.de", "@gmx.de", "@aol.de", "@live.de", "@outlook.de", "@hotmail.de"],
            "dk":["@yahoo.dk", "@live.dk", "@outlook.dk"],
            "es":["@yahoo.es", "@wanadoo.es", "@outlook.es", "@hotmail.es"],
            "fi":["@yahoo.fi", "@hotmail.fi"],
            "fr":['@gmail.com', '@laposte.net', '@free.fr', '@hotmail.fr', '@outlook.fr', '@sfr.fr', '@orange.fr', "@yahoo.fr", "@yopmail.fr", "@yopmail.com", "@gmx.fr", "@aliceadsl.fr", "@aol.fr", "@live.fr", "@wanadoo.fr"],
            "gr":["@yahoo.gr"],
            "hk":["@live.hk"],
            "hu":["@yahoo.hu", "@outlook.hu"],
            "ie":["@yahoo.ie", "@live.ie", "@outlook.ie"],
            "in":["@yahoo.in", "@live.in", "@outlook.in"],
            "it":["@yahoo.it", "@aol.it", "@live.it", "@outlook.it", "@hotmail.it"],
            "jp":["@yahoo.it", "@aol.jp", "@live.jp", "@outlook.jp", "@hotmail.co.jp"],
            "kg":["@hotmail.kg"],
            "kr":["@outlook.kr"],
            "kz":["@hotmail.kz"],
            "li":["@gmx.li"],
            "lv":["@outlook.lv"],
            "nl":["@yahoo.nl", "@live.nl", "@outlook.nl", "@hotmail.nl"],
            "no":["@yahoo.no", "@live.no"],
            "ph":["@outlook.ph"],
            "pl":["@yahoo.pl", "@yandex.pl"],
            "pt":["@yahoo.pt", "@outlook.pt"],
            "ro":["@yahoo.ro", "@hotmail.ro"],
            "ru":['@mail.ru', "@yandex.mail", "@yahoo.ru", "@yandex.com", "@yandex.ru", "@live.ru", "@hotmail.ru"],
            "sa":["@outlook.sa"],
            "se":["@yahoo.se", "@live.se"],
            "sg":["@outlook.sg"],
            "sk":["@outlook.sk"],
            "ua":["@yandex.ua"],
            "uk":["@gmx.co.uk", "@aol.co.uk", "@wanadoo.co.uk", "@live.co.uk", "@hotmail.co.uk"],
            "us": ["@mail.com", "@mail.aol.com", "@zoho.com", "@yahoo.net", "@gmx.us", "@hushmail.com", "@verizon.com"],
            "vn": ["@outlook.com.vn"],
        }
        return DomainsByCountry


if __name__ == "__main__":
    EmailGenerate("John","Doe")