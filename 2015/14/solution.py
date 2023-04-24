import sys
from dataclasses import dataclass


@dataclass
class Reindeer:
    name: str
    speed: int
    flight_period: int
    rest_period: int

    def __post_init__(self):
        self.distance = 0
        self.flight_time = 0
        self.rest_time = 0

    def fly(self):
        if self.flight_time < self.flight_period:
            self.distance += self.speed
            self.flight_time += 1
        else:
            self._rest()

    def _rest(self):
        if self.rest_time < self.rest_period:
            self.rest_time += 1
        else:
            self.flight_time = 0
            self.rest_time = 0
            self.fly()


def award_leader(reindeers: list[Reindeer], scoreboard: dict[str, int]) -> None:
    longest_distance = max(r.distance for r in reindeers)
    for r in reindeers:
        if r.distance == longest_distance:
            scoreboard[r.name] += 1


reindeers = []
for line in sys.stdin:
    name, _, _, speed, _, _, flight_period, *_, rest_period, _ = line.split()
    speed, flight_period, rest_period = map(int, (speed, flight_period, rest_period))
    reindeers.append(Reindeer(name, speed, flight_period, rest_period))

scoreboard = {r.name: 0 for r in reindeers}
for i in range(2503):
    for reindeer in reindeers:
        reindeer.fly()
    award_leader(reindeers, scoreboard)

print("Part One:", max(r.distance for r in reindeers))
print("Part Two:", max(scoreboard.values()))
