class SpeakMixin:
    def speak(self):
        name = self.__class__.__name__.lower()
        print(f"The {name} says hello!")


class RollOverMixin:
    def roll_over(self):
        name = self.__class__.__name__.lower()
        print(f"{name} did a barrel roll!")


class Dog(SpeakMixin, RollOverMixin):
    pass

dog = Dog()
dog.speak()
dog.roll_over()