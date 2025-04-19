import streamlit as st

st.title("Unit Converter")
st.subheader("Convert between different units of measurement")
st.write("Select a conversion type and enter the value to convert.")
# Conversion options
conversion_types = {
    "Length": {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084,
        "inches": 39.3701
    },
    "Weight": {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274
    },
    "Temperature": {
        "celsius": lambda x: x,
        "fahrenheit": lambda x: (x * 9/5) + 32,
        "kelvin": lambda x: x + 273.15
    }
}
# Select conversion type
conversion_type = st.selectbox("Select conversion type", list(conversion_types.keys()))
# Select input unit
input_unit = st.selectbox("Select input unit", list(conversion_types[conversion_type].keys()))
# Input value
input_value = st.number_input(f"Enter value in {input_unit}", format="%.2f")
# Select output unit
output_unit = st.selectbox("Select output unit", list(conversion_types[conversion_type].keys()))
# Convert value
if conversion_type == "Length" or conversion_type == "Weight":
    converted_value = input_value * conversion_types[conversion_type][output_unit] / conversion_types[conversion_type][input_unit]
else:   
    if input_unit == output_unit:
        converted_value = input_value
    elif input_unit == "celsius":
        converted_value = conversion_types[conversion_type][output_unit](input_value)
    else:
        converted_value = conversion_types[conversion_type][input_unit](input_value)
# Display result
st.subheader(f"Converted value: {converted_value:.2f} {output_unit}")
#footer
st.markdown("---")