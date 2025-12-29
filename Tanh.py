import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Tanh Activation Function")
x = np.linspace(-10,10,100)
y = np.tanh(x)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
st.write("The hyperbolic tangent (tanh) function is defined as:")
st.latex(r"\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}")
st.write("It maps input values to the range (-1, 1) and is commonly used in neural networks as an activation function.")