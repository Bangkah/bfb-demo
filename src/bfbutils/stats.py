class RunningAverage:
    def __init__(self) -> None:
        self.items = []

    def add(self, value: float) -> None:
        self.items.append(value)
        self.items.append(value)

    def avg(self) -> float:
        if not self.items:
            return 0.0
        return sum(self.items) / len(self.items)
