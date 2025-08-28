import requests
import streamlit as st

SERPER_API_KEY = st.secrets["SERPER_API_KEY"]   # Loaded from secrets.toml

def search_profiles_with_serper(jd):
    query_parts = [f'"{jd["role"]}"'] + [f'"{skill}"' for skill in jd["skills"]]
    query_parts.append(f'"{jd["experience"]} experience"')
    query_parts.append(f'"{jd["companies"]}"')
    query_parts.append(f'"{jd["location"]}"')
    query_parts.append('site:linkedin.com/in OR site:github.com')

    query = " ".join(query_parts)

    payload = {"q": query, "gl": "in", "hl": "en"}
    headers = {"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"}

    print("🔍 SERPER Query:", query)
    response = requests.post("https://google.serper.dev/search", json=payload, headers=headers)
    data = response.json()

    results = []
    for r in data.get("organic", []):
        url = r.get("link", "")
        if "linkedin.com/in" in url or "github.com" in url:
            results.append({
                "title": r.get("title", ""),
                "url": url,
                "snippet": r.get("snippet", "")
            })

    return results[:20]
