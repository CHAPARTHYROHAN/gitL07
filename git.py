import streamlit as st
import math

# Define the Elec_Power function
def Elec_Power(V, I, PF):
    phi = math.acos(PF)
    P = V * I * math.cos(phi)
    Q = V * I * math.sin(phi)
    S = V * I
    return P, Q, S

# Streamlit UI
st.title('Power Calculation Web App')

# Input fields for voltage, current, and power factor
V = st.number_input('Enter Voltage (V) in Volts:', min_value=0.0, step=0.1)
I = st.number_input('Enter Current (I) in Amps:', min_value=0.0, step=0.1)
PF = st.number_input('Enter Power Factor (PF):', min_value=0.0, max_value=1.0, step=0.01)

# Calculate and display results
if V > 0 and I > 0 and PF >= 0 and PF <= 1:
    P, Q, S = Elec_Power(V, I, PF)
    
    st.write(f'Active Power (P): {P:.2f} Watts')
    st.write(f'Reactive Power (Q): {Q:.2f} VARs')
    st.write(f'Apparent Power (S): {S:.2f} VA')
else:
    st.write('Please enter valid input values for voltage, current, and power factor.')