import re


def part_one(passports):
    """Count all the valid passports."""

    validPassports = 0

    for passport in passports:
        if len(passport) == 8:
            validPassports += 1
        elif len(passport) == 7:
            if 'cid' not in list(passport.keys()):
                validPassports += 1

    return validPassports


def part_two(passports):
    """Count all the valid passports and check their fields."""

    validPassports = 0

    for passport in passports:
        lengthCorrect = False

        # Check if all passport fields are present.
        if len(passport) == 8:
            lengthCorrect = True
        elif (len(passport)) == 7:
            if 'cid' not in passport.keys():
                lengthCorrect = True

        # Check if the fields are valid.
        fieldsValid = True
        for key, val in passport.items():
            if key == 'byr':
                if not (len(val) == 4 and
                        int(val) >= 1920 and int(val) <= 2002):
                    fieldsValid = False
            elif key == 'iyr':
                if not (len(val) == 4 and
                        int(val) >= 2010 and int(val) <= 2020):
                    fieldsValid = False
            elif key == 'eyr':
                if not (len(val) == 4 and
                        int(val) >= 2020 and int(val) <= 2030):
                    fieldsValid = False
            elif key == 'hgt':
                if 'cm' in val:
                    if not (int(val[:-2]) >= 150 and int(val[:-2]) <= 193):
                        fieldsValid = False
                elif 'in' in val:
                    if not (int(val[:-2]) >= 59 and int(val[:-2]) <= 76):
                        fieldsValid = False
                else:
                    fieldsValid = False
            elif key == 'hcl':
                if not (val[0] == '#' and
                        re.match('^([0-9]|[a-f]){6}$', val[1:])):
                    fieldsValid = False
            elif key == 'ecl':
                colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                if val not in colors:
                    fieldsValid = False
            elif key == 'pid':
                if not (re.match('^[0-9]{9}$', val)):
                    fieldsValid = False

        if lengthCorrect and fieldsValid:
            validPassports += 1

    return validPassports


def main():

    with open("input.txt") as f:
        content = f.readlines()
    content = [item.strip() for item in content]

    passports = []

    passport = []
    for line in content:
        if line == '':
            passports.append(passport)
            passport = []
        else:
            attributes = line.split(' ')
            for attribute in attributes:
                passport.append(attribute)
    passports.append(passport)

    for i, passport in enumerate(passports):
        passportDict = {}

        for attribute in passport:
            key = attribute.split(':')[0]
            value = attribute.split(':')[1]
            passportDict[key] = value

        passports[i] = passportDict

    res1 = part_one(passports)
    print(f'Part One: {res1}')

    res2 = part_two(passports)
    print(f'Part Two: {res2}')


if __name__ == '__main__':
    main()
