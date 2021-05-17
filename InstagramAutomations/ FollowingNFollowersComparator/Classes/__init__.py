from instaloader import Instaloader, Profile


class InstaBot:  # Exploring private methods and attributes
    def __init__(self, username, password, account):
        # User data
        self.account = account
        self.username = username
        self.password = password

        # User lists
        self.__followers_list = []
        self.__following_list = []

        # Library variables
        self.login = Instaloader()
        self.login.login(self.username, self.password)
        self.profile = Profile.from_username(self.login.context, self.account)

    def __get_followers(self):
        self.__followers_list = [f.username for f in self.profile.get_followers()]

    def __get_following(self):
        self.__following_list = [f.username for f in self.profile.get_followees()]

    def ff_comparator(self):
        data = {}
        self.__get_followers()
        self.__get_following()

        my_mistake = []
        for u in self.__followers_list:
            if u not in self.__following_list:
                my_mistake.append(u)

        their_mistake = []
        for u in self.__following_list:
            if u not in self.__followers_list:
                their_mistake.append(u)

        data["My Mistake"] = my_mistake
        data["Their Mistake"] = their_mistake
        return data
