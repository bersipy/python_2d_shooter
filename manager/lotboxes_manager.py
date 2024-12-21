from typing import Dict

from entity.lootBox import LootBox
from utils.id_generator import IdGenerator


class LootboxesManager:
    def __init__(self):
        self.__items : Dict[int, ] = {}
        self.id_generator = IdGenerator()

    @property
    def lootboxes(self):
        return self.__items.values()

    def spawn(self, starting_pos: tuple):
        _id = self.id_generator.generate()
        lootbox = LootBox(starting_pos)
        self.__items[_id] = lootbox

    def draw(self, screen):
        for item in self.__items.values():
            item.draw(screen)

    def update(self):
        self.__clean_already_looted_lootboxes()

    def __clean_already_looted_lootboxes(self):
        self.__items = { k: v for k, v in self.__items.items() if not v.is_looted }
