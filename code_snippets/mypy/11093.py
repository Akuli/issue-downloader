Block = dict[str, str]

def main() -> Block:

    out = Block()  # error: Need type annotation for "out" (hint: "out: Dict[<type>, <type>] = ...")

    return out

if __name__ == "__main__":
    main()
