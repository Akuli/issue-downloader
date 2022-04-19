from typing import TypeVar, overload, Type, Optional, Generic


# Define a Player base class that can be paired with some data.
T = TypeVar('T')

class Player(Generic[T]):
    pass


# Create an overloaded function to handle casting
# both Player and Optional[Player] to corresponding
# specific subtypes.
# (to ensure Optional state stays intact, unlike raw cast())

PT = TypeVar('PT', bound=Player)

@overload
def playercast(totype: Type[PT], obj: Player) -> PT:
    ...

@overload
def playercast(totype: Optional[Type[PT]],
               obj: Optional[Player]) -> Optional[PT]:
    ...

def playercast(totype: Optional[Type[PT]],
               obj: Optional[Player]) -> Optional[PT]:
    return obj  # type: ignore


# Now define a PlayerConcrete subtype, assign a few to Player vars,
# and then attempt to cast them back to PlayerConcrete.

class PlayerConcrete(Player[int]):
    pass

player1: Optional[Player] = PlayerConcrete()
player2: Player = PlayerConcrete()

# Gives Optional[PlayerConcrete] as I would expect.
reveal_type(playercast(PlayerConcrete, player1))

# This, however, gives Any.
reveal_type(playercast(PlayerConcrete, player2))



# Doing the same thing with distinct functions works as expected.

def playercast_nonopt(totype: Type[PT], obj: Player) -> PT:
    return obj  # type: ignore

def playercast_opt(totype: Optional[Type[PT]],
                   obj: Optional[Player]) -> Optional[PT]:
    return obj  # type: ignore

# Gives Optional[PlayerConcrete].
reveal_type(playercast_opt(PlayerConcrete, player1))

# Gives PlayerConcrete.
reveal_type(playercast_nonopt(PlayerConcrete, player2))
