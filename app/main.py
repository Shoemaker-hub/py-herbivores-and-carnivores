class Animal:
    alive = []

    def __init__(
            self, name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        Animal.alive.append(self)
        print(self.__dict__)

    def __repr__(self) -> None:
        return (f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore_animal: Herbivore) -> None:
        if (herbivore_animal.hidden is True
                or not isinstance(herbivore_animal, Herbivore)):
            return
        herbivore_animal.health -= 50
        if herbivore_animal.health <= 0:
            Animal.alive.remove(herbivore_animal)
