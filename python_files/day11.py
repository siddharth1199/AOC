import itertools
import functools
import sys
import string


def skip_bad_letters(prop, letter_group, bad_letters):
    maybe_bad_letter = [a[0] for a in enumerate(prop) if a[1] in bad_letters]
    if maybe_bad_letter:
        first_bad_idx = maybe_bad_letter[0]
        first_bad_letter = prop[first_bad_idx]
        next_good_letter = letter_group[letter_group.index(first_bad_letter) + 1]
        return prop[0:first_bad_idx] + next_good_letter + 'a' * (7 - first_bad_idx)
    else:
        return prop


def increment_letter(letter, letter_group):
    # 26 for all letters, 23 for allowable
    letter_group_length = len(letter_group)
    idx = letter_group.index(letter) + 1
    new_letter_idx = (idx) % letter_group_length
    return letter_group[new_letter_idx]


def ip(password, allowable_letters):
    """
    Increment Password.
    Increment the last letter in the string, then "carry the one" if necessary
    """
    new_letter = increment_letter(password[-1], allowable_letters)
    if new_letter == 'a':
        return ip(password[:-1], allowable_letters) + new_letter
    else:
        return password[:-1] + new_letter


def next_valid_password(start, bad_letters):

    # Consts. Could let these be global or args but meh.
    letters = string.ascii_lowercase
    allowable_letters = functools.reduce(lambda x, y: x.replace(y, ''),
                                         bad_letters,
                                         letters)
    allowable_pairs = [a + a for a in allowable_letters]

    # This line isn't necessary so it's commented out,
    # but it speeds things up for 2nd example
    updated_start = skip_bad_letters(start, letters, bad_letters)

    # No point in checking the input, because we want the *next* valid one.
    if updated_start == start:
        prop = ip(start, allowable_letters)
    else:
        prop = updated_start

    while True:
        enough_pairs = len([a for a in allowable_pairs if a in prop]) >= 2
        indices = [letters.index(x) for x in prop]
        ords = list(map(lambda x: x[1] - x[0],
                        list(zip(indices, indices[1:]))))
        has_straight = ', 1, 1' in str(ords)
        if enough_pairs and has_straight:
            return prop
        else:
            prop = ip(prop, allowable_letters)


def main():

    start = 'cqjxjnds'
    
    bad_letters = 'iol'
    part1 = next_valid_password(start, bad_letters)
    print(part1)

    part2 = next_valid_password(part1, bad_letters)
    print(part2)

if __name__ == '__main__':
    main()