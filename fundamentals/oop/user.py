

class User:
    def __init__(self, fname, lname, u_email, u_age, member = False, points = 0):
        self.first_name = fname
        self.last_name = lname
        self.email = u_email
        self.age = u_age
        self.is_rewards_member = member
        self.gold_card_points = points

    def display_info(self):
        print(f"{self.first_name} \n{self.last_name} \n{self.email} \n{self.age} \n{self.is_rewards_member} \n{self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print(f'{self.first_name} is already a member')
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = self.gold_card_points + 200
            return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Not enough golden coins :-(")
            return self
        else:
            self.gold_card_points = self.gold_card_points - amount
            return self


tommy = User("Tommy", "Douglas", "ttd@email.com", 34)
ash = User("Ash", "Ketchum", "nevergonnaage@email.com", 10)
marty = User("Marty", "McFly", "MCtoofly@email.com", 17)


tommy.enroll().display_info().spend_points(100).display_info().enroll()