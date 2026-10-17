# Start here: you do not need to be a programmer

[← Home](README.md)

This collection is for students and curious people who want to understand data and AI by trying things. You can start by reading, clicking, comparing, and asking questions. Writing code is an optional next step.

## Learn concepts, then recognize tools

Start with a question: preparing a table is **data transformation**; choosing a chart is **visualization**; predicting from known answers is **supervised learning**; finding groups without answers is **unsupervised learning**. The hub links each topic to a small example and names the tools used to implement it.

Try the [data basics notebook](notebooks/2-data-basics.ipynb) and [first-classifier notebook](notebooks/3-first-classifier.ipynb) before reading a larger historical project. When you want to build something, use the [data web-app starter and deployment lesson](templates/streamlit-starter/).

## Choose your first activity

| Activity | Why try it? | What you need | Suggested time |
|---|---|---|---|
| [Explore a GDP dashboard](https://github.com/bforbesc/gdp-dashboard#start-here-no-coding) | See how a chart changes when you choose countries and dates | A browser; the shared template demo is linked in the guide | 15 minutes |
| [Try the text-to-numbers notebook](https://colab.research.google.com/github/bforbesc/Data-AI-with-Forbes/blob/main/notebooks/1-ai-fuel-from-text-to-tokens-to-tensors.ipynb) | Understand one small part of how AI processes language | A browser and a Google account to run it in Colab; no API key | 20 minutes |
| [Explore groups in data](https://github.com/bforbesc/clustering-web-app#start-here-no-coding) | See how a computer groups similar observations without answer labels | The app, if available, or a teacher running it; a fictional sample is included | 20 minutes |
| [Check an AI data assistant](https://github.com/bforbesc/Your-Data-Wrestler#start-here-no-coding) | Learn why an AI answer still needs checking | The sample and worksheet; a configured app for the AI part | 20–30 minutes |
| [Play Arita's Puppy Panic](https://github.com/bforbesc/arita-the-game#start-here-no-coding) | Learn how a small idea becomes rules, feedback, and a game | A browser; a teacher can start the game locally | 10–15 minutes |

Times are suggestions, not prerequisites. If an older app is unavailable, use its worksheet or ask your teacher to demonstrate it. A sleeping Streamlit app may offer a wake-up button; a failed deployment needs its owner to fix it.

## Your first notebook, step by step

A **notebook** is a page with explanations, small blocks of code, and their results. **Google Colab** runs that code in your browser so you do not need to install Python.

1. Open the **text-to-numbers notebook** linked above. Sign in to Google if prompted.
2. Choose **File → Save a copy in Drive** if you want to keep your changes.
3. Read the text above each code block. Click the small play triangle beside the first block, then work down the page. Colab may ask you to connect to a runtime: that is the computer that will run the code.
4. Find `TEXT = "Tokens are text that become numbers that were text"`. Replace only the words between the quotation marks with `Cats chase cats`.
5. Run that cell and every cell below it again. At the token step, expect `['cats', 'chase', 'cats']`. The two occurrences of `cats` should share the same vocabulary entry.
6. Explain to a classmate why repeating a word does not create a new word in the vocabulary.

This is a deliberately simple word-splitting example. Real language models often split words into smaller pieces. The goal is to understand the steps, not to reproduce every detail of a production model.

If you get an error, start from the first code cell and run down the page again. Restarting a runtime clears values stored in memory. Ask for help with the error text and the cell you ran; never include a secret key.

## When you are ready for the course

The [Generative AI and AI Agents course](notebooks/genai-day/) builds a fictional hotel assistant. It is designed for a guided class with business students. Start with the text-to-numbers activity, then follow the course's **Demo** and **Your turn** sections. You do not need to understand every line before experimenting with a prompt.

The main course and final challenge call a paid external AI service and need an API key supplied by you or your instructor. Ask your instructor to arrange access; do not put keys in GitHub or shared notebook outputs. The fine-tuning notebook is an optional instructor activity and recommends a T4 GPU, a faster type of computer available in some Colab sessions.

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

## For teachers

Begin with a question, demonstrate one result, then let students change one thing. Ask them to record **what they expected**, **what happened**, and **what they can verify**. A short explanation of an observed result is a useful outcome even when nobody writes code.

The projects are historical experiments at different stages of maturity. Use the ready-made activities in their READMEs, check the app before class, and keep a worksheet fallback. The source code is there for students who want to look deeper.
