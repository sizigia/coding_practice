class UserInfo:
    def __init__(self, name, age, gender, occupation):
        self.name = str(name)
        self.age = int(age)
        self.gender = str(gender)
        if gender == 'woman':
            self.treatment = 'Miss'
        else:
            self.treatment = 'Mister'
        self.occupation = occupation

    def newJob(self, new_occupation):
        self.occupation = new_occupation
        print(self.occupation)
        congrats = f'Ayeee, you {self.treatment} {self.occupation}'
        return congrats


if __name__ == '__main__':
    users_online = []
    name = input("What's your name? ", )
    age = int(input("What's your age? "))
    gender = str(input("How do you identify yourself? "))
    occupation = str(input("What do you do for a living? "))
    user = UserInfo(name, age, gender, occupation)
    users_online.append(user)
    print(user.name)
    print(user.occupation)
    print(user.newJob('Manager'))
    print("Users online right now:", *map(lambda user_: user.name, users_online))
    print("Professionals online right now:", *
          map(lambda user_: user.occupation, users_online))
