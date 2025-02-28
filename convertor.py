#unit convertor project 1 by muskan nisar
import streamlit as st

# Custom styling
st.markdown(
    """
    <style>
    .big-font { font-size:25px !important; color: #ff5733; font-weight: bold; }
    .result-text { font-size:20px !important; color: #2ecc71; font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True
)

# Custom function for unit conversion
def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {
            "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Miles": 0.000621371,
            "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
        },
        "Weight": {
            "Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274
        }
    }

    # Temperature conversions
    def convert_temperature(val, from_u, to_u):
        if from_u == to_u:
            return val
        if from_u == "Celsius":
            return val * 9/5 + 32 if to_u == "Fahrenheit" else val + 273.15
        if from_u == "Fahrenheit":
            return (val - 32) * 5/9 if to_u == "Celsius" else (val - 32) * 5/9 + 273.15
        if from_u == "Kelvin":
            return val - 273.15 if to_u == "Celsius" else (val - 273.15) * 9/5 + 32

    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)

    base_value = value / conversion_factors[category][from_unit]
    return base_value * conversion_factors[category][to_unit]

# Streamlit UI
st.markdown("<h1 class='big-font'>🚀 Unit Converter by Muskan</h1>", unsafe_allow_html=True)
st.write("✨ A stylish and efficient unit converter for all your needs!")

# Category Selection
category = st.selectbox("📏 Choose a category:", ["Length", "Weight", "Temperature"])

# Units based on category
units = {
    "Length": ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"],
    "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("🔄 Convert from:", units[category])
to_unit = st.selectbox("➡ Convert to:", units[category])
value = st.number_input("✏ Enter value:", min_value=0.0, format="%.2f")

# Live conversion (no button needed)
if value:
    result = convert_units(value, from_unit, to_unit, category)
    st.markdown(f"<p class='result-text'>{value} {from_unit} = {result:.2f} {to_unit} ✅</p>", unsafe_allow_html=True)
