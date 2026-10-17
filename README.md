# 📊 API Data Dashboard

An interactive data dashboard built using Python and Streamlit that fetches,
processes, filters, and visualizes data from an external REST API.

The project demonstrates practical Python development skills, API integration,
JSON data handling, interactive data visualization, caching, error handling,
and unit testing.

## 🚀 Features

- **REST API Integration:** Fetches posts from an external API.
- **JSON Processing:** Processes and validates API responses.
- **Interactive Dashboard:** Displays API data through a web interface.
- **Dynamic Metrics:** Displays the total number of posts.
- **Title Search:** Searches posts by title.
- **User Filtering:** Filters posts by User ID.
- **Data Visualization:** Displays a bar chart showing post distribution by user.
- **Caching:** Caches API responses for improved efficiency.
- **Error Handling:** Handles API request failures and invalid response data.
- **Unit Testing:** Includes tests for search and filtering functionality.

## 🛠️ Tech Stack

- Python
- Streamlit
- Requests
- REST API
- JSON
- unittest

## 🌐 API Used

This project uses the JSONPlaceholder Posts API to retrieve sample post data.

API Endpoint:

https://jsonplaceholder.typicode.com/posts

## 📸 Dashboard Overview

The dashboard provides:

- Total post count
- API connection status
- Title-based search
- User ID filtering
- Individual post details
- Posts distribution chart

## 📁 Project Structure

API_Dashboard/
├── dashboard.py
├── api_test.py
├── test_dashboard.py
├── requirements.txt
├── README.md
└── .gitignore


## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd API_Dashboard
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the Dashboard

```bash
python -m streamlit run dashboard.py
```

The dashboard will open in your default browser.


## 🧪 Testing

The project includes unit tests for the search and filtering helper functions.

Run the tests using:

```bash
python -m unittest -v test_dashboard.py
```

The current test suite contains six tests covering:

- Counting posts
- Searching posts by title
- Case-insensitive search
- Searching when no matching result exists
- Filtering posts by User ID
- Displaying posts from all users

## 🧠 Key Learnings

Through this project, I practised:

- Making HTTP requests using Python
- Working with external REST APIs
- Processing and validating JSON data
- Building interactive applications using Streamlit
- Implementing search and filtering
- Using caching to reduce repeated API requests
- Creating data visualizations
- Handling request and data validation errors
- Writing unit tests using Python's `unittest` framework
- Organizing and documenting a Python project

## 🔮 Future Improvements

Potential future improvements include:

- Adding more data sources
- Introducing additional search and filtering options
- Expanding test coverage to include API requests and error scenarios
- Improving the dashboard interface
- Deploying the dashboard online

## 👨‍💻 Author

**Ayush Saxena**

- **GitHub:** https://github.com/Ayush2809-tech
- **LinkedIn:** https://www.linkedin.com/in/ayush-saxena-2809s/
- **Portfolio:** https://ayush2809-tech.github.io/Ayush_PortFolio/

---

If you find this project useful, consider giving the repository a star ⭐
