def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()

    print("Input data is '25'")
    temperature = input_temperature("25")
    print(f"Temperature is now {temperature}°C")
    print()

    print("Input data is 'abc'")
    try:
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}°C")
    except Exception as error_msg:
        print(f"Caught input_temperature error: {error_msg}")
    finally:
        print()
        print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

# ==============================================================================#
# ln 1-2 take a str input and return an int. the converted str the (Tempretue)
# try && except && finally they're useful
# as stores the error and save it in an {error_msg} variable
# ==============================================================================#
