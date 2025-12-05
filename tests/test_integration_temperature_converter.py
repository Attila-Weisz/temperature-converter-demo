import math
from io import StringIO
from contextlib import redirect_stdout
from temperature_converter import TemperatureConverter

def test_convert_and_print_celsius():
    """
    Tests the convert_and_print method for Celsius input.
    0 C should convert to 32 F and 273.15 K.
    """
    memory_buffer_obj = StringIO()
    with redirect_stdout(memory_buffer_obj):
        TemperatureConverter.convert_and_print(0.0, 'C')

    out = memory_buffer_obj.getvalue()
    assert "0.00 C = 32.00 F" in out
    assert "0.00 C = 273.15 K" in out


def test_roundtrip_celsius_to_fahrenheit_and_back():
    """
    Tests the roundtrip conversion from Celsius to Fahrenheit and back.
    25 C should convert to 77 F and back to approximately 25 C.
    """
    original = 25.0
    f = TemperatureConverter.celsius_to_fahrenheit(original)
    back_to_c = TemperatureConverter.fahrenheit_to_celsius(f)

    assert math.isclose(back_to_c, original, rel_tol=1e-6)