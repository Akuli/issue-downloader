x = lambda: quit()
print(1) # ok

if __name__ == "__main__":
    print(2)  # Mypy: Statement is unreachable

