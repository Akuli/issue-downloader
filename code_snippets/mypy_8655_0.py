def test_launch_missile_only_accepts_str() -> None:
    with pytest.raises(TypeError):
        launch_missile(10)  # error: Argument 1 to "launch_missile" has incompatible type "int"; expected "str" [arg-type]
