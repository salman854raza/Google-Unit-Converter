import streamlit as st

# Inject CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2ef);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 4px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        color: white;
        text-align: center;
        margin-bottom: 30px;
        font-size: 36px;
    }
    .stButton>button {
        background: linear-gradient(135deg, #007bff, #0056b3);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.5);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #0056b3, #004085);
        box-shadow: 0px 8px 20px rgba(0, 201, 255, 0.6);
    }
    .result-box {
        background: rgba(255, 255, 255, 0.1);
        font-weight: bold;
        font-size: 20px;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(0, 201, 255, 0.3);
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: black;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of measurement")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.sidebar.number_input("Enter the value to convert", min_value=0.0, value=0.0, step=0.1)

col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilometer", "Meter", "Mile", "Yard", "Foot", "Inch"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilometer", "Meter", "Mile", "Yard", "Foot", "Inch"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Kilometer': 0.001, 'Meter': 1, 'Mile': 0.000621371, 
        'Yard': 1.09361, 'Foot': 3.28084, 'Inch': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Gram': 1000, 'Milligram': 1000000, 
        'Pound': 2.20462, 'Ounce': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):  
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value

# Button for conversion
if st.button("🤖 Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)
    
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Developed with love by Salman Raza</div>", unsafe_allow_html=True)