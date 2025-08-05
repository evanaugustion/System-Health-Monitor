import pandas as pd
import streamlit as st
import time
from streamlit_autorefresh import st_autorefresh

# Refresh the app every 1000 milliseconds (1 second)
st_autorefresh(interval=1000, key="data_refresh")


st.title ("System Health Dashboard")

df = pd.read_csv ('system_log.csv')
print (df)
df['Time'] = pd.to_datetime(df['Time'])

st.line_chart(df.set_index("Time")[["CPU Usage (%)", "Memory Usage (%)", "Disk Usage (%)"]])
latest = df.iloc[-1]

st.subheader("Latest Readings")
st.write(f"**CPU:** {latest['CPU Usage (%)']}%")
st.write(f"**Memory:** {latest['Memory Usage (%)']}%")
st.write(f"**Disk:** {latest['Disk Usage (%)']}%")