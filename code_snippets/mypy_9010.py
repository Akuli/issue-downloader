from luguru import logger

LOG_A = logger.opt(lazy=False)
LOG_B = logger.opt(lazy=True)

LOG_A.info('Test {}', lambda x: x)    # should work
LOG_B.info('Test {}', lambda x: x)    # error

logger.opt(lazy=False).info('Test {c}', c=lambda x: x)  # should work
logger.opt(lazy=True).info('Test {d}', d=lambda x: x)   # error
