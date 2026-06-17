import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.set_page_config(page_title="Smart Agriculture")

if "token" not in st.session_state:
    st.session_state.token = None

# ======================
# LOGIN / REGISTER PAGE
# ======================
if st.session_state.token is None:

    st.title("🌱 Smart Agriculture System")

    page = st.radio(
        "Choose Option",
        ["Login", "Register"]
    )

    if page == "Register":

        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Register"):

            r = requests.post(
                f"{API}/auth/register",
                json={
                    "username": username,
                    "password": password
                }
            )

            st.write(r.json())

    else:

        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            r = requests.post(
                f"{API}/auth/login",
                json={
                    "username": username,
                    "password": password
                }
            )

            if r.status_code == 200:

                st.session_state.token = r.json()["access_token"]

                st.success("Login Successful")

                st.rerun()

            else:
                st.error("Invalid Credentials")

# ======================
# DASHBOARD
# ======================
else:

    st.title("🌾 Farmer Dashboard")

    if st.button("Logout"):

        st.session_state.token = None

        st.rerun()

    temp = st.number_input("Temperature")

    hum = st.number_input("Humidity")

    soil = st.number_input("Soil Moisture")

    if st.button("Send Sensor Data"):

        requests.post(
            f"{API}/sensors/",
            json={
                "temperature": temp,
                "humidity": hum,
                "soil_moisture": soil
            }
        )

        st.success("Sensor Data Stored")

    if st.button("Get Recommendation"):

        r = requests.post(
            f"{API}/ai/recommend",
            params={
                "temperature": temp,
                "humidity": hum,
                "soil_moisture": soil
            }
        )

        st.success(
            f"Recommended Crop: "
            f"{r.json()['recommended_crop']}"
        )