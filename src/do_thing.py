def do_thing(x: float, y: float, z: str) -> str:
    xy = x + y
    return f"{z} {xy}"


if __name__ == "__main__":
    result = do_thing(1.5, 2.5, "The result is:")
    print(result)
