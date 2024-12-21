from items import Items


class InventoryManager:
    def __init__(self):
        self.__inventory = {}

        for item in Items.get_items():
            self.__inventory[item] = 0

    def add(self, item: str, number: int):
        self.__inventory[item] += number

    def remove(self, item: str, number: int):
        if self.__inventory[item] < number:
            raise ValueError(f"We don't have enough {item} to delete (we are trying to delete {number} of {self.__inventory[item]})")
        self.__inventory[item] -= number

    def get(self, item: str):
        return self.__inventory[item]
