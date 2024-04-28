import streamlit as st

# Define the list of Rashis
RASHI_LIST = [
    "Mesha",
    "Vrishabha",
    "Mithuna",
    "Kataka",
    "Simha",
    "Kanya",
    "Tula",
    "Vrischika",
    "Dhanasu",
    "Makara",
    "Khumbha",
    "Meena",
]


# Compatibility logic for Lagna, Moon, Mars, Venus
def check_compatibility(man_rashi, woman_rashi):
    man_index = RASHI_LIST.index(man_rashi)
    incompatible_positions = [
        (man_index + 5) % 12,  # 6th position
        (man_index + 7) % 12,  # 8th position
        (man_index + 11) % 12,  # 12th position
    ]
    return RASHI_LIST.index(woman_rashi) not in incompatible_positions


# Compatibility logic for Sun
def check_sun_compatibility(man_sun, woman_sun):
    man_index = RASHI_LIST.index(man_sun)
    incompatible_position = (man_index + 6) % 12
    return RASHI_LIST.index(woman_sun) != incompatible_position


# --- Streamlit App Structure ---

st.title("Compatibility Checker")

# --- Lagna Compatibility ---
st.header("Lagna Compatibility")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Select Man's Lagna")
    man_lagna = st.selectbox("", RASHI_LIST, key="man_lagna")

with col2:
    st.subheader("Select Woman's Lagna")
    woman_lagna = st.selectbox("", RASHI_LIST, key="woman_lagna")


st.markdown("<hr style='margin-top: 30px; margin-bottom: 30px;'>", unsafe_allow_html=True)

# --- Moon Compatibility ---
st.header("Moon Compatibility")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Select Man's Moon Rashii")
    man_moon = st.selectbox("", RASHI_LIST, key="man_moon")

with col2:
    st.subheader("Select Woman's Moon Rashii")
    woman_moon = st.selectbox("", RASHI_LIST, key="woman_moon")


st.markdown("<hr style='margin-top: 30px; margin-bottom: 30px;'>", unsafe_allow_html=True)

# --- Mars Compatibility --- (Similar structure to Moon)
st.header("Mars Compatibility")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Select Man's Mars Rashii")
    man_mars = st.selectbox("", RASHI_LIST, key="man_mars")

with col2:
    st.subheader("Select Woman's Mars Rashii")
    woman_mars = st.selectbox("", RASHI_LIST, key="woman_mars")


st.markdown("<hr style='margin-top: 30px; margin-bottom: 30px;'>", unsafe_allow_html=True)

# --- Venus Compatibility --- (Similar structure to Moon)
st.header("Venus Compatibility")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Select Man's Venus Rashii")
    man_venus = st.selectbox("", RASHI_LIST, key="man_venus")

with col2:
    st.subheader("Select Woman's Venus Rashii")
    woman_venus = st.selectbox("", RASHI_LIST, key="woman_venus")


st.markdown("<hr style='margin-top: 30px; margin-bottom: 30px;'>", unsafe_allow_html=True)


# --- Sun Compatibility --- (Similar structure to Moon)
st.header("Sun Compatibility")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Select Man's Sun Rashii")
    man_sun = st.selectbox("", RASHI_LIST, key="man_sun")

with col2:
    st.subheader("Select Woman's Sun Rashii")
    woman_sun = st.selectbox("", RASHI_LIST, key="woman_sun")

st.markdown("<hr style='margin-top: 30px; margin-bottom: 30px;'>", unsafe_allow_html=True)

if st.button("Check All Compatibilities"):
    # Check Lagna
    if check_compatibility(man_lagna, woman_lagna):
        st.success("Lagna: Compatible")
    else:
        st.error("Lagna: Not Compatible")

    # Check Moon
    if check_compatibility(man_moon, woman_moon):
        st.success("Moon: Compatible")
    else:
        st.error("Moon: Not Compatible")

    # Check Mars
    if check_compatibility(man_mars, woman_mars):
        st.success("Mars: Compatible")
    else:
        st.error("Mars: Not Compatible")

    # Check Venus
    if check_compatibility(man_venus, woman_venus):
        st.success("Venus: Compatible")
    else:
        st.error("Venus: Not Compatible")

    # Check Sun
    if check_sun_compatibility(man_sun, woman_sun):
        st.success("Sun: Compatible")
    else:
        st.error("Sun: Not Compatible")



