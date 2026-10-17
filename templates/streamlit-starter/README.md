# 🌐 Build and publish your first data web app

[← Learning hub](../../README.md) · **Data transformation · Visualization · Web apps · Deployment**

**The question:** how can someone explore a data result without opening your code?

This small, reusable template turns a fictional six-row order table into a page with a selector, a total, and a chart. It shows a general pattern: **data → visitor's choice → transformation → visible result → check**. The tools here are examples, not the learning goal.

## What you will learn

- **Pandas** holds and summarizes the table.
- **Plotly** turns the summary into an interactive chart.
- **Streamlit** gives a Python script a browser interface and reruns it when a control changes.
- **Deployment** means running that app on another computer so people can visit a web address. A local app runs only while your computer and server are running.

The sample is fictional, has no personal data, uses no AI service, and needs no secret keys. Reading the code and checking the six records is a complete introductory activity; running it is the next step.

## 1. Read, predict, and check

Open [app.py](app.py). You do not need to understand the imports. Find the six orders and add their values:

| Choice | Expected total | Expected rows | Expected bars |
|---|---:|---:|---:|
| All | €160 | 6 | 2 |
| Books | €60 | 3 | 1 |
| Games | €100 | 3 | 1 |

Find the code comments marked **DATA**, **INPUT**, **TRANSFORM**, and **OUTPUT**. The file [requirements.txt](requirements.txt) lists the libraries the app needs; it is the app's list of dependencies.

## 2. Run a copy locally

You need Python installed; use Python 3.11–3.13 for this starter (verified here on Python 3.13). On GitHub, choose **Code → Download ZIP** for the hub, extract it, and open a terminal in `templates/streamlit-starter` inside that extracted folder.

```bash
python -m venv .venv
```

Activate the environment with `source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\Activate.ps1` in Windows PowerShell. If your Python command is `python3` or `py`, use that to create the environment. Then:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local address printed by Streamlit, usually `http://localhost:8501`. Try each choice and check it against the table above. Stop the app by pressing **Ctrl+C** in the terminal.

## 3. Make one change

Add another Books order worth €15 to the list in `app.py`. Predict the new totals before saving: **Books €75**, **Games €100**, **All €175**. Refresh or let Streamlit rerun. Then change the question, title, or categories for a tiny project of your own. Keep the units visible.

## 4. Publish your own copy

Publishing is optional. Use your own fork or repository so you control what becomes public.

1. Create a GitHub account if needed, and **Fork** the Data & AI with Forbes repository. A fork is your own copy on GitHub. Alternatively, put just this starter's files in a new repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/), sign in, and connect your own GitHub repository when prompted.
3. Choose **Create app** and the option for an existing app. Select your repository, its branch, and the main Python file. In a fork of the whole hub, the path is `templates/streamlit-starter/app.py`. If you copied these files to the repository root, it is `app.py`.
4. Choose the same supported Python version you used locally in **Advanced settings**. Keep `requirements.txt` next to `app.py`; the host uses it to install the libraries.
5. Deploy, open the resulting `streamlit.app` address, and repeat all three checks in the table. A deployment is successful when the page works for a visitor, not simply when files have been uploaded.

The host's interface and limits can change. See the [official deployment steps](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy) and [dependency-file guidance](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies). This lesson explains deployment; it does not create a hosted app for you.

## If something goes wrong

| Symptom | First check |
|---|---|
| `No module named ...` | Activate the environment and install this folder's requirements. |
| The host cannot find `app.py` | Check the exact file path and branch selected for deployment. |
| The deployed version differs from your copy | Save and commit the intended changes to your own selected branch. |
| A total is unexpected | Inspect the filtered table and add its visible values before changing the chart. |

## Take it further

Compare this small pattern with the historical [GDP dashboard](https://github.com/bforbesc/gdp-dashboard), [clustering example](https://github.com/bforbesc/clustering-web-app), and [data-agent experiment](https://github.com/bforbesc/Your-Data-Wrestler). What new work does each add to the same basic app structure?

Code and documentation use the hub's [MIT License](../../LICENSE). When using the starter elsewhere, keep that license notice with your copy.
