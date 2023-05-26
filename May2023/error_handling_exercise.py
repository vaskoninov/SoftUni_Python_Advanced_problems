###### Numbers Dictionary

# numbers_dictionary = {}
# line = input()
#
# while line != "Search":
#     number_as_string = line
#     try:
#         number = int(input())
#         numbers_dictionary[number_as_string] = number
#     except ValueError:
#         print("The variable number must be an integer")
#
#     line = input()
#
# line = input()
#
# while line != "Remove":
#     searched = line
#     try:
#         print(numbers_dictionary[searched])
#     except KeyError:
#         print("Number does not exist in dictionary")
#     line = input()
#
# line = input()
#
# while line != "End":
#     searched = line
#     try:
#         del numbers_dictionary[searched]
#     except KeyError:
#         print("Number does not exist in dictionary")
#     line = input()
#
# print(numbers_dictionary)

######## Email Validator

import re


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
