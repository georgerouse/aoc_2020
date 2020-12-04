import re

MANDATORY_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def passport_is_valid(passport):
    if not (int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002):
        return False, 'Failed byr'

    if not(int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020):
        return False, 'Failed iyr'

    if not(int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030):
        return False, 'Failed eyr'

    if passport['hgt'].endswith('cm'):
        hgt_int = int(passport['hgt'].replace('cm', ''))
        if not(hgt_int >= 150 and hgt_int <= 193):
            return False, 'Failed hgt (cm)'
    elif passport['hgt'].endswith('in'):
        hgt_int = int(passport['hgt'].replace('in', ''))
        if not(hgt_int >= 59 and hgt_int <= 76):
            return False, 'Failed hgt (in)'
    else:
        return False, 'Failed hgt'

    if not (bool(re.search(r'#[a-f0-9]{6}', passport['hcl'])) and len(passport['hcl']) == 7):
        return False, 'Failed hcl'

    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False, 'Failed ecl'

    if not (bool(re.search(r'[0-9]{9}', passport['pid'])) and len(passport['pid']) == 9):
        return False, 'Failed pid'

    return True, ''


if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_04.txt') as f:
        file_data = f.readlines()

    # Parse it into a list of dicts
    passport_list = []
    passport_details = {}
    for i, line in enumerate(file_data):
        if line == '\n':
            passport_list.append(passport_details)
            passport_details = {}
        else:
            line_sections = line.replace('\n', '').split(' ')
            for line_section in line_sections:
                identifier = line_section.split(':')[0]
                value = line_section.split(':')[1]
                passport_details[identifier] = value

        if i + 1 == len(file_data):
            passport_list.append(passport_details)
            passport_details = {}

    # Part 1
    valid_count = 0
    for passport in passport_list:
        if set(passport.keys()).issuperset(MANDATORY_FIELDS):
            valid_count += 1

    print(f"Answer to part 1: {valid_count}")
    passport_list = [passport for passport in passport_list if set(passport.keys()).issuperset(MANDATORY_FIELDS)]

    # Part 2
    valid_count = 0
    for passport in passport_list:
        passport_ok, message = passport_is_valid(passport)
        if passport_ok:
            valid_count += 1

    print(f"Answer to part 2: {valid_count}") # 104 too high
