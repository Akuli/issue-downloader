import tensorflow as tf


def bar() -> tf.Tensor:
    return tf.zeros(0)


def foo() -> str:
    return bar()
