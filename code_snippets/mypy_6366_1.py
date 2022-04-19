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
