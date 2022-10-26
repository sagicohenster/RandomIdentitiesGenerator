import utils as u


identities_num = u.get_and_validate_the_num_of_identities_to_be_created()
identities = u.create_identities_by_given_num(identities_num)
u.print_identities_personal_data(identities)


