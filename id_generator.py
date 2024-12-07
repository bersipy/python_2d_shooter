class IdGenerator:
    def __init__(self):
        self.last_id = 0

    def generate(self) -> int:
        self.last_id += 1
        return self.last_id
