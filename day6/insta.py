class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print(f"{username} is an user now!")
    
    def follow(self, user):
        self.following += 1
        user.followers += 1

user1 = User("001", "Rupam")
user2 = User("002", "Biswas")
user2.follow(user1)
print(user1.followers)
