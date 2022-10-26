import random
import string
import sys
import identities_data as d
from identity import Identity


def gen_rand_firstname():
    return random.choice(d.firstnames)


def gen_rand_lastname():
    return random.choice(d.lastnames)


def gen_rand_email(firstname):
    return gen_email_user_name(firstname) + gen_email_provider_name()


def gen_rand_city():
    return random.choice(d.cities)


def gen_rand_country():
    return random.choice(d.countries)


def gen_rand_id():
    return int(''.join(str(random.randint(0, 9)) for i in range(9)))


def gen_email_provider_name():
    return '@' + random.choice(d.domains) + random.choice(d.extensions)


def gen_email_user_name(firstname):
    rand_2letter_comb = ''.join(random.choice(string.ascii_letters) for l in range(2))
    return firstname + rand_2letter_comb + str(random.randint(1, 9999))


def print_identities_personal_data(identities):
    for i in identities:
        print(f'{i.email}, {i.firstname}, {i.lastname}, {i.city}, {i.country}, {i.id}')


def create_identities_by_given_num(identities_num_to_create):
    identities = []
    for i in range(identities_num_to_create): identities.append(Identity())
    return identities


def get_and_validate_the_num_of_identities_to_be_created():
    try:
        identities_amount = int(input('Number of identities to create: '))
        if identities_amount <= 0: raise ValueError
        return identities_amount
    except ValueError:
        print('Invalid value. Only positive integers are allowed')
        sys.exit()