# Start here: you do not need to be a programmer

[📚 Learning hub](https://github.com/bforbesc/data-ai-with-forbes) · [🧭 Beginner guide](https://github.com/bforbesc/data-ai-with-forbes/blob/main/START_HERE.md)

Courses, notebooks, and project examples for students exploring data and AI. The resources below include browser-based examples and optional code.

## Learn concepts, then recognize tools

Start with a question: preparing a table is **data transformation**; choosing a chart is **visualization**; predicting from known answers is **supervised learning**; finding groups without answers is **unsupervised learning**. The hub links each topic to a small example and names the tools used to implement it.

The [first-classifier notebook](notebooks/first-classifier.ipynb) introduces supervised learning.

## Choose your first activity

| Activity | What it covers | What you need |
|---|---|---|
| [Explore a GDP dashboard](https://github.com/bforbesc/gdp-dashboard#start-here-no-coding) | See how a chart changes when you choose countries and dates | A browser; the shared template demo is linked in the guide |
| [Try the text-to-numbers notebook](https://colab.research.google.com/github/bforbesc/Data-AI-with-Forbes/blob/main/notebooks/ai-fuel-from-text-to-tokens-to-tensors.ipynb) | Understand one small part of how AI processes language | A browser and a Google account to run it in Colab; no API key |
| [Explore groups in data](https://github.com/bforbesc/clustering-web-app#start-here-no-coding) | See how a computer groups similar observations without answer labels | The hosted app or a local copy; fictional sample included |
| [Check an AI data assistant](https://github.com/bforbesc/Your-Data-Wrestler#start-here-no-coding) | Learn why an AI answer still needs checking | The sample and worksheet; a configured app for the AI part |
| [Play Arita's Puppy Panic](https://github.com/bforbesc/arita-the-game#start-here-no-coding) | Learn how a small idea becomes rules, feedback, and a game | A browser and a local copy |

Older hosted apps may be unavailable. Their READMEs include sample data and worked examples that can be read without running the app.

## Your first notebook, step by step

A **notebook** is a page with explanations, small blocks of code, and their results. **Google Colab** runs that code in your browser so you do not need to install Python.

1. Open the **text-to-numbers notebook** linked above. Sign in to Google if prompted.
2. Choose **File → Save a copy in Drive** if you want to keep your changes.
3. Read the text above each code block. Click the small play triangle beside the first block, then work down the page. Colab may ask you to connect to a runtime: that is the computer that will run the code.
4. Find `TEXT = "Tokens are text that become numbers that were text"`. Replace only the words between the quotation marks with `Cats chase cats`.
5. Run that cell and every cell below it again. At the token step, expect `['cats', 'chase', 'cats']`. The two occurrences of `cats` should share the same vocabulary entry.

The vocabulary contains unique words, so both occurrences of `cats` use the same entry.

This is a deliberately simple word-splitting example. Real language models often split words into smaller pieces. The goal is to understand the steps, not to reproduce every detail of a production model.

If you get an error, start from the first code cell and run down the page again. Restarting a runtime clears values stored in memory. Ask for help with the error text and the cell you ran; never include a secret key.

## When you are ready for the course

The [Generative AI and AI Agents course](notebooks/genai-day/) builds a fictional hotel assistant. It covers prompting, context, retrieval, tools, agents, and evaluation, with **Demo** and **Your turn** sections.

The main course and final challenge require an API key for a paid external AI service. Keep keys out of GitHub and shared notebook outputs. The optional fine-tuning notebook recommends a T4 GPU runtime in Colab.

## A few words you will meet

| Word | In plain language |
|---|---|
| Repository, or repo | A project folder on GitHub, with its files and change history |
| Dashboard | A page of charts and numbers you can explore |
| Dataset | A collection of observations, often a table |
| Row / column | One observation / one kind of information about it |
| CSV | A plain-text table with values separated by commas |
| Streamlit | A tool used to turn Python scripts into interactive web apps |
| Token | A piece of text represented inside a language model |
| Tensor | An array of numbers; think of a list or a table extended to more dimensions |
| Prompt | The instructions or question you give an AI model |
| Agent | A program that uses an AI model to decide which tools or steps to try |
| API key | A secret credential that lets software use an external service |

## Keep learning

The [references and resources page](resources/README.md) brings together books, courses, newsletters, a curated LLM maths playlist, and my articles.
