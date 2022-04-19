from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import MediaType

class FileFormatError(Exception):
    pass

class MediaTypeValueError(FileFormatError):
    def __init__(self, value):
        super().__init__(f'{value!r} is not a valid media type.')

class UnsupportedFileFormatError(FileFormatError):
    def __init__(self, media_type: 'MediaType'):
        super().__init__('File is not a supported format.', {'media_type': media_type})
