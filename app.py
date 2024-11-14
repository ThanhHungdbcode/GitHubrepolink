import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data (replace with your actual file or DataFrame)
@st.cache_data
def load_data():
    # Load only specific columns and specify data types to reduce memory usage
    usecols = ["column1", "column2", "column3"]  # Replace with actual column names
    dtype = {"column1": "float32", "column2": "int32", "column3": "category"}  # Replace with actual types
    return pd.read_csv(r"C:\Users\Lenovo\df_Cleaned CA - FL (3).csv", usecols=usecols, dtype=dtype)

data = load_data()

# Convert non-numeric columns to categorical or remove them for numerical analysis
data_numeric = data.select_dtypes(include=["number"])

# Set the title of the Streamlit app
st.title("Data Visualization App")

# Show raw data if the user wants to see it
if st.checkbox("Show Raw Data"):
    st.write(data)

# Sidebar for selecting visualizations
st.sidebar.header("Select Visualization")
chart_type = st.sidebar.selectbox("Choose a chart type:", ("Bar Chart", "Line Chart", "Heatmap", "Scatter Plot"))

# Sidebar for selecting features
st.sidebar.header("Select Features")
x_axis = st.sidebar.selectbox("X-Axis Feature", data.columns)
y_axis = st.sidebar.selectbox("Y-Axis Feature", data.columns)

# Display selected chart
if chart_type == "Bar Chart":
    st.header(f"Bar Chart: {y_axis} vs {x_axis}")
    fig, ax = plt.subplots()
    sns.barplot(x=x_axis, y=y_axis, data=data, ax=ax, color="blue")
    st.pyplot(fig)

elif chart_type == "Line Chart":
    st.header(f"Line Chart: {y_axis} vs {x_axis}")
    fig, ax = plt.subplots()
    sns.lineplot(x=x_axis, y=y_axis, data=data, ax=ax)
    st.pyplot(fig)

elif chart_type == "Heatmap":
    st.header("Heatmap of Correlations")
    fig, ax = plt.subplots()
    sns.heatmap(data_numeric.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

elif chart_type == "Scatter Plot":
    st.header(f"Scatter Plot: {y_axis} vs {x_axis}")
    fig, ax = plt.subplots()
    sns.scatterplot(x=x_axis, y=y_axis, data=data, ax=ax)
    st.pyplot(fig)

# Allow user to download filtered data
if st.checkbox("Download Filtered Data"):
    st.download_button(label="Download CSV", data=data.to_csv(index=False), file_name="filtered_data.csv", mime="text/csv")
