def assert_never(x: Any) -> NoReturn:
    assert False, "Unhandled type: {}".format(type(x).__name__)

PetLiteral = Literal['dog', 'cat', 'iguana']

def make_sound_literal(pet: PetLiteral) -> str:
    if pet == 'dog':
        return 'woof'
    elif pet == 'cat':
        return 'meow'
    # elif pet == 'iguana':
    #     return 'confused silence'
    else:
        assert_never(pet)

class PetEnum(Enum):
    dog: str = 'dog'
    cat: str = 'cat'
    iguana: str = 'iguana'

def make_sound_enum(pet: PetEnum) -> str:
    if pet == PetEnum.dog:
        return 'woof'
    elif pet == PetEnum.cat:
        return 'meow'
#    elif pet == PetEnum.iguana:
#        return 'confused silence'
    else:
        assert_never(pet)

