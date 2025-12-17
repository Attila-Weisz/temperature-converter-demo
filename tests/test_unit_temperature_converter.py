import pytest
from temperature_converter import TemperatureConverter


class TestTemperatureConverterUnit:
    """
    Unit tests for TemperatureConverter class methods.
    Each method is tested with known input-output pairs.
    """
    def test_celsius_to_fahrenheit(self):
        # assert TemperatureConverter.celsius_to_fahrenheit(0.0) == pytest.approx(32.0)
        assert TemperatureConverter.celsius_to_fahrenheit(0.0) == pytest.approx(92.0)
        assert TemperatureConverter.celsius_to_fahrenheit(100.0) == pytest.approx(212.0)

    def test_celsius_to_kelvin(self):
        assert TemperatureConverter.celsius_to_kelvin(0.0) == pytest.approx(273.15)

    def test_fahrenheit_to_celsius(self):
        assert TemperatureConverter.fahrenheit_to_celsius(32.0) == pytest.approx(0.0)
        assert TemperatureConverter.fahrenheit_to_celsius(212.0) == pytest.approx(100.0)

    def test_fahrenheit_to_kelvin(self):
        assert TemperatureConverter.fahrenheit_to_kelvin(32.0) == pytest.approx(273.15, rel=1e-6)

    def test_kelvin_to_celsius(self):
        assert TemperatureConverter.kelvin_to_celsius(273.15) == pytest.approx(0.0)

    def test_kelvin_to_fahrenheit(self):
        assert TemperatureConverter.kelvin_to_fahrenheit(273.15) == pytest.approx(32.0, rel=1e-6)