#!/usr/bin/python3
def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)

    if temperature > 40:
        raise ValueError(
            f"{temperature}°C is too hot for plants (max 40°C)"
        )

    if temperature < 0:
        raise ValueError(
            f"{temperature}°C is too cold for plants (min 0°C)"
        )

    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"Input data is '{value}'")
        try:
            temperature = input_temperature(value)
            print(f"Temperature is now {temperature}°C")
        except Exception as error_msg:
            print(f"Caught input_temperature error: {error_msg}")
        finally:
            print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()


# ================================================================#
# Exep [is a runtime Error Reporting mechanism][gives you the
# message to understand the problem] [have types (syntaxErrot,
# ValueError, etc)] -- we used here value error 
# ... Traceback [gives you the line to look for the Code in This
# line]. raise [keyword used to raise your own Exep]
# ================================================================#