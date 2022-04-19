class addbase:
    def __init__(self, fp):
        self.fp = fp
        self.read = self.fp.read
        self.readline = self.fp.readline
        if hasattr(self.fp, "readlines"): self.readlines = self.fp.readlines
        if hasattr(self.fp, "fileno"):
            self.fileno = self.fp.fileno
        else:
            self.fileno = lambda: None
        if hasattr(self.fp, "__iter__"):
            self.__iter__ = self.fp.__iter__
            if hasattr(self.fp, "next"):
                self.next = self.fp.next
