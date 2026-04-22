class Person:
    def getGender(self) -> str:
        return "Unknown"


class Male(Person):
    def getGender(self) -> str:
        return "Male"


class Female(Person):
    def getGender(self) -> str:
        return "Female"


if __name__ == "__main__":
    male = Male()
    female = Female()

    print(male.getGender())
    print(female.getGender())