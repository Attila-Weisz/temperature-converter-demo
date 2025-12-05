class TemperatureConverter:
    """
    Converts temperatures between Celsius, Fahrenheit, and Kelvin.
    1. Celsius to Fahrenheit: (C * 9/5) + 32
    2. Celsius to Kelvin: C + 273.15
    3. Fahrenheit to Celsius: (F - 32) * 5/9
    4. Fahrenheit to Kelvin: ((F - 32) * 5/9
    5. Kelvin to Celsius: K - 273.15
    6. Kelvin to Fahrenheit: ((K - 273.15) * 9/5) + 32
    """

    @staticmethod
    def celsius_to_fahrenheit(c: float) -> float:
        return c * 9.0 / 5.0 + 32.0

    @staticmethod
    def celsius_to_kelvin(c: float) -> float:
        return c + 273.15

    @staticmethod
    def fahrenheit_to_celsius(f: float) -> float:
        return (f - 32.0) * 5.0 / 9.0

    @staticmethod
    def fahrenheit_to_kelvin(f: float) -> float:
        return TemperatureConverter.celsius_to_kelvin(
            TemperatureConverter.fahrenheit_to_celsius(f)
        )

    @staticmethod
    def kelvin_to_celsius(k: float) -> float:
        return k - 273.15

    @staticmethod
    def kelvin_to_fahrenheit(k: float) -> float:
        return TemperatureConverter.celsius_to_fahrenheit(
            TemperatureConverter.kelvin_to_celsius(k)
        )

    @staticmethod
    def convert_and_print(temperature: float, unit: str) -> None:
        """
        Converts the given temperature to the other two units and prints the results.

        Parameters:
        - temperature (float): The temperature value to convert.
        - unit (str): The unit of the temperature value ('C', 'F', or 'K').

        Returns:
        - None: Prints the converted temperature values.

        Exceptions:
        - Handles invalid unit input.
        """
        u = unit.strip().lower()

        if u == 'c':
            print(f"{temperature:.2f} C = "
                  f"{TemperatureConverter.celsius_to_fahrenheit(temperature):.2f} F")
            print(f"{temperature:.2f} C = "
                  f"{TemperatureConverter.celsius_to_kelvin(temperature):.2f} K")

        elif u == 'f':
            print(f"{temperature:.2f} F = "
                  f"{TemperatureConverter.fahrenheit_to_celsius(temperature):.2f} C")
            print(f"{temperature:.2f} F = "
                  f"{TemperatureConverter.fahrenheit_to_kelvin(temperature):.2f} K")

        elif u == 'k':
            print(f"{temperature:.2f} K = "
                  f"{TemperatureConverter.kelvin_to_celsius(temperature):.2f} C")
            print(f"{temperature:.2f} K = "
                  f"{TemperatureConverter.kelvin_to_fahrenheit(temperature):.2f} F")

        else:
            print("Invalid unit.")


def main():
    try:
        raw_temp = input("Enter temperature value: ")
        temperature = float(raw_temp)
        unit = input("Enter unit (C/F/K): ")
    except ValueError:
        print("Invalid temperature value.")
        return

    TemperatureConverter.convert_and_print(temperature, unit)


if __name__ == "__main__":
    main()