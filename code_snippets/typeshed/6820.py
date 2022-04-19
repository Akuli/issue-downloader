from configparser import RawConfigParser

cfg = RawConfigParser()
cfg.add_section("default")

cfg.set("default", "some_option1", True)
r1 = cfg.get("default", "some_option1")
print(r1, type(r1))


cfg.set("default", "some_option2", 1)
r2 = cfg.get("default", "some_option2")
print(r2, type(r2))

cfg.set("default", "some_option3", b"bytes")
r3 = cfg.get("default", "some_option3")
print(r3, type(r3))
