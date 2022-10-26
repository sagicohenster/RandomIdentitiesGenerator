import utils as u


class Identity:
    def __init__(self):
        self.firstname = u.gen_rand_firstname()
        self.lastname = u.gen_rand_lastname()
        self.email = u.gen_rand_email(self.firstname)
        self.city = u.gen_rand_city()
        self.country = u.gen_rand_country()
        self.id = u.gen_rand_id()