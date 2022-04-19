def test2() -> None:
    def worker(d: int) -> int:
        return d + 1

    output: List[Optional[int]] = run_tasks(
        [1, 2, 2, 1], worker,
    )
    from pprint import pprint

    pprint(output)
    assert output == [None, 3, None, 2]


test2()
