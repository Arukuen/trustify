# Trustify - A Filipino Fake News Detector API using Scikit-Learn

This API is used by a browser extension [here](https://github.com/H3XoRuSH/Filipino-Fake-News-Detector).

### How to Run
1. Clone the repository.
2. Run `pip install -r requirements.txt` to install the required dependencies.
3. Run `uvicorn main:app`. If this does not work, you may:
  - Add `C:\Users\[ACCOUNT]\AppData\Local\Programs\Python\Python39\Scripts` (or similar to this) to the PATH. Run `uvicorn main:app` in the terminal.
  - Add Python to Path `C:\Users\[ACCOUNT]\AppData\Local\Programs\Python\Python39`. Run `python -m uvicorn main:app`.

### Credits
The dataset used in this application can be found in this [link](https://github.com/jcblaisecruz02/Tagalog-fake-news).
