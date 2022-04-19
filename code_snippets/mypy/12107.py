from enum import (
        auto,
        Enum,
        )

class Game(Enum):

    TENNIS = auto()
    PING_PONG = auto()
    SOCCER = auto()

    def is_racquet_sport(self) -> bool:
        return self in {self.TENNIS, self.PING_PONG}
                # error: Non-overlapping container check (
                #           element type: "Game",
                #           container item type: "auto"
                #           )
                #           [comparison-overlap]
