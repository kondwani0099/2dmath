import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_data(equation):
    x = np.linspace(-10, 10, 400)
    
    if equation == "Linear Equation":
        y = 2*x + 1
    elif equation == "Quadratic Equation":
        y = x**2 - 4*x + 3
    elif equation == "Cubic Equation":
        y = x**3 - 3*x**2 + 2*x - 1
    elif equation == "Exponential Function":
        y = np.exp(0.5*x)
    elif equation == "Logarithmic Function":
        y = np.log(x + 10.1)  # Adding a constant to avoid log(0) or negative values
    elif equation == "Sine Function":
        y = np.sin(x)
    elif equation == "Cosine Function":
        y = np.cos(x)
    elif equation == "Logistic Function":
        y = 1 / (1 + np.exp(-x))
    elif equation == "Ohm's Law (Electricity)":
        y = 2*x  # V = IR with R=2, I=x
    elif equation == "Capacitor Charging (RC Circuit)":
        t = np.linspace(0, 10, 400)
        y = 5 * (1 - np.exp(-t / 5))  # V(t) = V0 (1 - e^(-t/RC)) with V0=5, RC=5
        x = t  # Use time for x-axis
    elif equation == "Spring-Mass System (Hooke's Law)":
        y = -3*x  # F = -kx with k=3
    elif equation == "Projectile Motion":
        theta = np.pi / 4  # 45 degrees
        v0 = 20
        g = 9.8
        y = x * np.tan(theta) - (g * x**2) / (2 * v0**2 * np.cos(theta)**2)
    elif equation == "Damped Harmonic Oscillator":
        t = np.linspace(0, 10, 400)
        A = 5
        beta = 0.1
        omega = 2
        y = A * np.exp(-beta * t) * np.cos(omega * t)
        x = t  # Use time for x-axis
    else:
        y = np.zeros_like(x)  # Default to a flat line if none selected
    
    return x, y

def plot_2d_graph(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y, label='y=f(x)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    return fig

# Streamlit app
st.title("Interactive 2D Plot")

# Dropdown for equation selection
equation = st.selectbox(
    "Choose a mathematical function to plot:",
    [
        "Linear Equation",
        "Quadratic Equation",
        "Cubic Equation",
        "Exponential Function",
        "Logarithmic Function",
        "Sine Function",
        "Cosine Function",
        "Logistic Function",
        "Ohm's Law (Electricity)",
        "Capacitor Charging (RC Circuit)",
        "Spring-Mass System (Hooke's Law)",
        "Projectile Motion",
        "Damped Harmonic Oscillator"
    ]
)

# Generate data based on selected equation
x, y = generate_data(equation)

# Explanation
st.write(f"""
### Explanation
This application visualizes a 2D plot of the {equation}. These functions are commonly used in fields such as mathematics, physics, and engineering to describe various phenomena.

The equation for the selected function is given by:
""")

if equation == "Linear Equation":
    st.latex(r"y = 2x + 1")
elif equation == "Quadratic Equation":
    st.latex(r"y = x^2 - 4x + 3")
elif equation == "Cubic Equation":
    st.latex(r"y = x^3 - 3x^2 + 2x - 1")
elif equation == "Exponential Function":
    st.latex(r"y = e^{0.5x}")
elif equation == "Logarithmic Function":
    st.latex(r"y = \log(x + 10.1)")
elif equation == "Sine Function":
    st.latex(r"y = \sin(x)")
elif equation == "Cosine Function":
    st.latex(r"y = \cos(x)")
elif equation == "Logistic Function":
    st.latex(r"y = \frac{1}{1 + e^{-x}}")
elif equation == "Ohm's Law (Electricity)":
    st.latex(r"V = IR \quad \text{with} \quad R=2 \quad \Rightarrow \quad V = 2I")
elif equation == "Capacitor Charging (RC Circuit)":
    st.latex(r"V(t) = V_0 \left(1 - e^{-t/RC}\right) \quad \text{with} \quad V_0=5, \, RC=5")
elif equation == "Spring-Mass System (Hooke's Law)":
    st.latex(r"F = -kx \quad \text{with} \quad k=3 \quad \Rightarrow \quad F = -3x")
elif equation == "Projectile Motion":
    st.latex(r"y = x \tan(45^\circ) - \frac{9.8x^2}{2 \cdot 20^2 \cos^2(45^\circ)}")
elif equation == "Damped Harmonic Oscillator":
    st.latex(r"x(t) = 5 e^{-0.1t} \cos(2t)")

st.write("You can interact with the plot below.")

# Plot the 2D graph
fig = plot_2d_graph(x, y)
st.pyplot(fig)
