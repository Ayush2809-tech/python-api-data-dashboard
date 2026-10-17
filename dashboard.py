import streamlit as st
import requests


@st.cache_data(ttl=300)
def fetch_posts():
    API_URL = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    posts = response.json()

    if not isinstance(posts, list):
        raise ValueError("API response must be a list.")

    if not all(
        isinstance(post, dict)
        and all(key in post for key in ("id", "userId", "title", "body"))
        for post in posts
    ):
        raise ValueError("API response contains unexpected post data.")

    return posts

# 1. PAGE CONFIGURATION

st.set_page_config(
    page_title="API Data Dashboard",
    page_icon="📊",
    layout="wide"
)


# 2. DASHBOARD HEADER

st.title("📊 Python API Data Dashboard")

st.write(
    "Welcome to my Python API Data Dashboard! "
    "This project fetches, searches, and filters "
    "data from an external API."
)

st.divider()

# 3. API CONFIGURATION

API_URL = "https://jsonplaceholder.typicode.com/posts"

# 4. FETCH DATA FROM API
try:
    posts = fetch_posts()

    
  
    # 5. API STATUS

    st.success("API connected successfully!")

    st.subheader("📈 Dashboard Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Total Posts",
            value=len(posts)
        )

    with col2:
        st.metric(
            label="API Status",
            value="Connected"
        )

    with col3:
        st.metric(
            label="Technology",
            value="Python"
        )


    # DATA VISUALIZATION


    st.divider()
    st.subheader("📊 Posts Distribution by User")

    # Count posts for each user
    posts_per_user = {}

    for post in posts:
        user_id = post["userId"]

        if user_id not in posts_per_user:
            posts_per_user[user_id] = 0

        posts_per_user[user_id] += 1

    # Display chart
    st.bar_chart(posts_per_user)

    st.divider()

    # 6. SEARCH POSTS
    st.subheader("🔍 Search and Filter Posts")

    search_query = st.text_input(
        "Search posts by title",
        placeholder="Enter a title keyword..."
    )

    # 7. FILTER BY USER ID

    user_ids = sorted(
        {post["userId"] for post in posts}
    )

    selected_user = st.selectbox(
        "Filter by User ID",
        options=["All Users"] + user_ids
    )


    # 8. SEARCH AND FILTER

    filtered_posts = posts

    # title search
    if search_query.strip():
        query = search_query.strip().lower()

        filtered_posts = [
            post
            for post in filtered_posts
            if query in post["title"].lower()
        ]

    #  user ID filter
    if selected_user != "All Users":
        filtered_posts = [
            post
            for post in filtered_posts
            if post["userId"] == selected_user
        ]

    # 9. DISPLAY FILTERED RESULTS

    st.write(f"**Posts found: {len(filtered_posts)}**")

    if not filtered_posts:
        st.warning(
            "No posts found. Try another search keyword "
            "or select a different User ID."
        )

    else:
        st.subheader("📝 Posts")

        for post in filtered_posts:
            with st.expander(
                f"Post {post['id']}: {post['title']}"
            ):
                st.write(f"**Post ID:** {post['id']}")
                st.write(f"**User ID:** {post['userId']}")
                st.write(f"**Title:** {post['title']}")
                st.write("**Content:**")
                st.write(post["body"])


except requests.exceptions.RequestException as error:
    st.error(
        f"Unable to fetch API data. Please check "
        f"your internet connection and try again.\n\n{error}"
    )

except ValueError as error:
    st.error(f"Invalid API response: {error}")