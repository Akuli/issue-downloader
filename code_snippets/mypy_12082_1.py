class Thing:
    thing: str | None
    def something(self, that: Thing) -> bool:
        if self.thing is not None or that.thing is not None:
            return True
        else:
            return self.thing == that.thing  # no error, despite None == None
