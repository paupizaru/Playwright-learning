# Learning Project: Web Automation with Python & Playwright

This project is focused on learning and practicing web automation using [Playwright](https://playwright.dev/python/docs/intro) with Python. The goal is to get familiar with the syntax, best practices, project structure, and key concepts like locators, assertions, fixtures, and more.

## 🚀 Technologies Used

- 🐍 Python 3.10+
- 🎭 Playwright for Python
- 🧪 Pytest for running tests
- 📦 pip for dependency management

## 📁 Project Structure

```
playwright-python-learning/
├── tests/
│   ├── test_example.py
│   └── ...
├── pages/
│   ├── login_page.py
│   └── ...
├── utils/
│   └── helpers.py
├── pytest.ini
├── conftest.py
├── requirements.txt
└── README.md
```

## ✅ Features Implemented

- [x] Environment setup with Playwright and Pytest  
- [x] Basic navigation and validation tests  
- [x] Using selectors and assertions  
- [x] Basic Page Object Model (POM)  
- [ ] Handling forms and authentication  
- [ ] Running tests in parallel  
- [ ] CI/CD integration (GitHub Actions)

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/playwright-python-learning.git
cd playwright-python-learning
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install the required browsers:

```bash
playwright install
```

## ▶️ Running Tests

To run all tests:

```bash
pytest tests/
```

Run with more verbosity or in headed mode:

```bash
pytest -v --headed
```

## 📚 Useful Resources

- [Playwright for Python Docs](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Playwright Page Object Model Guide](https://playwright.dev/python/docs/pom)

---

This project is part of my learning journey, so it will keep evolving as I progress in Python and Playwright automation skills.
