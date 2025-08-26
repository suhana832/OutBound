import streamlit as st
from jd_parser import parse_jd
from profile_scraper import search_profiles_with_serper

st.set_page_config(page_title="Outbound Candidate Finder", layout="wide")

st.title("🚀 Outbound Candidate Finder")
st.write("Fetch top LinkedIn/GitHub profiles based on your Job Description.")

# Sidebar JD input
st.sidebar.header("Job Description Input")
jd = parse_jd()  # default JD

role = st.sidebar.text_input("Role", jd["role"])
skills = st.sidebar.text_area("Skills (comma separated)", ", ".join(jd["skills"]))
experience = st.sidebar.text_input("Experience", jd["experience"])
targetcompanies = st.sidebar.text_input("companies", jd["companies"])
location = st.sidebar.text_input("Location", jd["location"])


if st.sidebar.button("🔍 Search Profiles"):
    jd_updated = {
        "role": role,
        "skills": [s.strip() for s in skills.split(",") if s.strip()],
        "experience": experience,
        "target companies":companies,
        "location": location
    }

    st.info("Fetching profiles from Google via Serper API...")
    profiles = search_profiles_with_serper(jd_updated)

    st.success(f"✅ {len(profiles)} profiles found")

    for i, profile in enumerate(profiles, 1):
        with st.container():
            st.subheader(f"{i}. {profile['title']}")
            st.write(profile['snippet'])
            st.markdown(f"[🔗 View Profile]({profile['url']})")
            st.divider()
