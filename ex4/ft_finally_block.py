class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name.capitalize() != plant_name:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")

    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plant_names: list[str]) -> None:
    print("Opening watering system")

    try:
        for plant_name in plant_names:
            water_plant(plant_name)

    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")
        print()


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()

    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])

    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])

    print("Cleanup always happens, even with errors!")
