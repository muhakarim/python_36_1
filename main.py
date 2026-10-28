class UserProfile:
    def __init__(self, first_name, last_name, age, phone, work_place, gender, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone
        self.work_place = work_place
        self.gender = gender
        self.country = country

    def info(self):
        return f'{self.first_name}, {self.last_name}, {self.age}, {self.phone}, {self.work_place}, {self.gender}, {self.country}'


user1 = UserProfile('Айдана', 'Иванова', 19, '+996000000000', 'Компания', 'Ж', 'KG')

print(user1.first_name)
print(user1.info())
