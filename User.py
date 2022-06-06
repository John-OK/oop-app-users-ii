class User:
    total_posts_num = 0
    all_posts = {}

    def __init__(self, name, email_address, driver_license_number, you_name_it="I named it!"):
        self.name = name.lower()
        self.email_address = email_address.lower()
        self.driver_license_number = str(driver_license_number).lower()
        self.you_name_it = str(you_name_it).lower()
        self.posts = {}

    def new_post(self):
        post = input("Message:\n")
        if len(post) > 0:
            self.posts[User.total_posts_num] = post
            User.all_posts[User.total_posts_num] = post
            User.total_posts_num += 1
            print(f"You're message '{post}' has been posted.")
        else:
            print(f"You didn't post anything. Wouldn't you like to share {self.name.title()}?\n")

    def delete_post(self):
        post_to_delete = input(f"Which post would you like to delete?\n{self.posts}\nEnter 'q' to cancel\n")

        if post_to_delete.lower() == 'q':
            print(f"I'm glad you've changed your mind {self.name.title()}.")
        elif type(int(post_to_delete)) == int:
            try:
                self.posts[int(post_to_delete)] = "YOU DELETED THIS POST."
                User.all_posts[int(post_to_delete)] = f"{self.name} DELETED THIS POST."
            except:
                print(f"I'm sorry {name}. I'm afraid I can't do that")

bob = User('Bob', 'BobMartin@supergeeks.org', 'A1234567')
sue = User('Sue', 'suziq@aboynamedsue.com', 'B9876543', 'Anything but "Sue!"')
jesus = User('DaJesus', 'dajesus@weroll.net',
             'Z4682467', 'Nobody messes wit da Jesus!')

print(bob.name, sue.email_address, jesus.you_name_it)
bob.new_post()
sue.new_post()
bob.new_post()
bob.delete_post()
sue.delete_post()
bob.delete_post()
print(bob.posts)
print(sue.posts)
print(User.all_posts)