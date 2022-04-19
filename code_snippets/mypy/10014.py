DRIVE_TYPE = TypeVar('DRIVE_TYPE', bound='Driver')

# This WORKS
# DRIVER_STATE_TYPE = TypeVar('DRIVER_STATE_TYPE', bound='DriverState')


@dataclass
class DriverState(Generic[DRIVE_TYPE]):
    driver: DRIVE_TYPE
    pid: str = ''


# This doesn't work
DRIVER_STATE_TYPE = TypeVar('DRIVER_STATE_TYPE', bound='DriverState')


@dataclass
class Driver(Generic[DRIVER_STATE_TYPE]):
    config: DRIVER_STATE_TYPE


@dataclass
class ESState(DriverState['ESDriver']):
    special_name: str = 'ES Driver'


@dataclass
class ESDriver(Driver[
    ESState
]):
    def name(self) -> None:
        print(self.config.special_name)
