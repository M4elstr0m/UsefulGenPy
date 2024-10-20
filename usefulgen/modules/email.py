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
    for string_parameter in [firstname,lastname,nationality,domain,birthday_year,pseudonym,nickname,pet]:
        if not isinstance(string_parameter, str) and string_parameter is not None:
            raise TypeError(f"Expected string-type as argument: received \"{string_parameter}\"")
    
    # Convert all to lowercase
    firstname = str.lower(firstname) if firstname is not None else None
    lastname = str.lower(lastname) if lastname is not None else None
    nationality = str.lower(nationality) if nationality is not None else None
    domain = str.lower(domain) if domain is not None else None
    birthday_year = str.lower(birthday_year) if birthday_year is not None else None
    pseudonym = str.lower(pseudonym) if pseudonym is not None else None
    nickname = str.lower(nickname) if nickname is not None else None
    pet = str.lower(pet) if pet is not None else None

    def __DictDomainsByCountry() -> dict:
        """
        Stores the DomainsByCountry dictionnary, ready to be applied to a variable. Created to save memory when executing code
        """
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

    # Value checking
    if domain is not None and not domain.startswith("@"):
        raise ValueError(f"`domain` must start with a \"@\" to be functional")
    elif nationality is not None and nationality not in list(__DictDomainsByCountry().keys()):
         raise ValueError(f"`nationality` must be a country code (eg: US, UK...) known by this program")

    # Defines all the possible domains depending on the given parameters
    PossibleDomains:list = ([domain,]) if domain is not None else (__DictDomainsByCountry()[nationality]+__DictDomainsByCountry()["_all"]) if nationality is not None else (__DictDomainsByCountry()["_all"])
    AlreadyYield:list = []

    if firstname is not None and lastname is not None:
        for do in PossibleDomains:
            if firstname+lastname+do not in AlreadyYield:
                AlreadyYield.append(firstname+lastname+do)
                yield firstname+lastname+do
            if firstname+"."+lastname+do not in AlreadyYield:
                AlreadyYield.append(firstname+"."+lastname+do)
                yield firstname+"."+lastname+do
            if firstname+"_"+lastname+do not in AlreadyYield:
                AlreadyYield.append(firstname+"_"+lastname+do)
                yield firstname+"_"+lastname+do
            if firstname+do not in AlreadyYield:
                AlreadyYield.append(firstname+do)
                yield firstname+do
            if firstname+"-"+lastname+do not in AlreadyYield:
                AlreadyYield.append(firstname+"-"+lastname+do)
                yield firstname+"-"+lastname+do
            if lastname+firstname+do not in AlreadyYield:
                AlreadyYield.append(lastname+firstname+do)
                yield lastname+firstname+do

                ### can have whitespaces instead of \t 
                ### for loop to reverse lastname and firstname
                ### sort depending on if lastname is the first one or if it is firstname in first
                yield lastname+"."+firstname+do
                yield lastname+"_"+firstname+do
                yield lastname+do
                yield lastname+"-"+firstname+do
                
                

if __name__ == "__main__": #to delete
    for i in EmailGenerate(firstname="John",lastname="Doe"):
        print(i)
