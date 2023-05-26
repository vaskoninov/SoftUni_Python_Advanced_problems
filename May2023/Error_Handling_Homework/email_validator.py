importimport re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class TooManyAtSymbols(Exception):
    pass


MIN_USER_NAME_LENGTH = 4
VALID_DOMAINS = [".com", ".bg", ".org", ".net"]

regex = re.compile(r'(?P<user>\w+)@\w+(?P<domain>\.\w+)')

email = input("Please enter your email address")

while email != "End":
    matches = regex.finditer(email)
    for match in matches:
        user = match.group("user")
        domain = match.group("domain")

        if len(user) < 4:
            raise NameTooShortError("Name must be more than 4 characters")
        if domain not in VALID_DOMAINS:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if email.count("@") > 1:
        raise TooManyAtSymbols("There should be one @ symbol")
    email = input("Please enter your email address")
