# Data & AI with Forbes

**Learn by doing. Build useful tools. Keep the experiments.**

I'm Bernardo Forbes Costa. This is the home base for my data and AI learning content, practical tools, and experiments built over the years: from Streamlit dashboards and unsupervised learning to data agents and a browser game.

Some projects are historical references. Tools have evolved and many things are easier to build today, but the questions, design choices, and lessons are still useful. Here you'll find the teaching notebooks alongside the projects that put those ideas into practice.

[Learning notebooks](#learning-notebooks) · [Projects & experiments](#projects--experiments) · [Project stories](projects/README.md) · [LinkedIn](https://www.linkedin.com/in/bernardoforbescosta/)

## Start here

| If you want to… | Start with… |
|---|---|
| Understand how text becomes input to an AI model | **AI's fuel: From Text to Tokens to Tensors**, below |
| Work through a hands-on GenAI course | [Generative AI and AI Agents](notebooks/genai-day/) |
| Explore dashboards, clustering, and data agents | [Projects & experiments](projects/README.md) |
| See a playful experiment in building a game | [Arita's Puppy Panic](projects/README.md#aritas-puppy-panic) |

## Projects & experiments

A collection of my past and ongoing experiments, centralized here as teaching references. The original repositories hold the code; the [project catalogue](projects/README.md) explains what each one explores and how to learn from it.

| Project | The experiment | Teaching angle |
|---|---|---|
| [GDP Dashboard](https://github.com/bforbesc/gdp-dashboard) | An interactive GDP dashboard built with Streamlit, based on a dashboard template | Turn a table into an interactive story; examine filtering, missing data, and comparisons |
| [Clustering Web App](https://github.com/bforbesc/clustering-web-app) | An unsupervised learning demo using KMeans and t-SNE | Explore how preprocessing and cluster choices change what you see |
| [Your Data Wrestler](https://github.com/bforbesc/Your-Data-Wrestler) | An agent that helps explore, clean, and visualize data | Compare AI suggestions with checks you can reproduce yourself |
| [Arita's Puppy Panic](https://github.com/bforbesc/arita-the-game) | A playful browser game and experiment in building with AI tools | Explore prototyping, game rules, feedback, and iteration |

These are references to explore and discuss, with different levels of maturity. A source link is not a guarantee that a hosted demo is running or that older dependencies work with today's environment. See each [project story](projects/README.md) for context and original links.

## Learning notebooks

Teaching notebooks for data and AI, clearly and simply explained. Each notebook runs in Google Colab and illustrates ideas hands-on, for students, professionals, and anyone curious. Some come with a LinkedIn article.

| Title | What it covers | Notebook | Article |
|-------|----------------|----------|---------|
| **AI's fuel: From Text to Tokens to Tensors** | Converts a sentence into tokens, maps them to indices, builds one-hot vectors, and stacks them into a tensor. | [![Open in Colab](https://img.shields.io/badge/Open-Colab-yellow?logo=google-colab)](https://colab.research.google.com/github/bforbesc/Data-AI-with-Forbes/blob/main/notebooks/1-ai-fuel-from-text-to-tokens-to-tensors.ipynb) | [Read](https://www.linkedin.com/pulse/ais-fuel-from-text-tokens-tensors-bernardo-forbes-costa-phd-bhyhf) |
| **Generative AI and AI Agents** (full-day course) | From tokens to a working AI agent for a fictional hotel: APIs, LLM calls, prompting, embeddings, RAG, tool calling, the ReAct loop, LangChain, prompt injection and toy fine-tuning. [More](notebooks/genai-day/) | [![Open in Colab](https://img.shields.io/badge/Open-Colab-yellow?logo=google-colab)](https://colab.research.google.com/github/bforbesc/Data-AI-with-Forbes/blob/main/notebooks/genai-day/genai_day.ipynb) | |
| **Generative AI and AI Agents: final challenge** | Configure an AI concierge as a workflow or an agent and score it on ten test emails. | [![Open in Colab](https://img.shields.io/badge/Open-Colab-yellow?logo=google-colab)](https://colab.research.google.com/github/bforbesc/Data-AI-with-Forbes/blob/main/notebooks/genai-day/final_challenge.ipynb) | |
| **Generative AI and AI Agents: model fine-tuning** | Fine-tune a tiny open model (SmolLM2-135M) on 60 examples to change its style, and see what fine-tuning does not change. Result on [Hugging Face](https://huggingface.co/bforbesc/smollm2-135m-hotel-silencio). | [![Open in Colab](https://img.shields.io/badge/Open-Colab-yellow?logo=google-colab)](https://colab.research.google.com/github/bforbesc/Data-AI-with-Forbes/blob/main/notebooks/genai-day/model_finetuning.ipynb) | |


## How to use this home base

1. **Pick an idea.** Open a notebook in Colab, or choose a project from the catalogue.
2. **Try it and question it.** Run notebook cells from top to bottom; use the project discussion prompts to investigate a design choice.
3. **Make it yours.** Change an input, compare outcomes, or sketch how you would rebuild an older experiment with today's tools.
4. **Share what you learn.** [Open an issue](https://github.com/bforbesc/Data-AI-with-Forbes/issues) with a question, a broken link, or a lesson suggestion. See [Contributing](CONTRIBUTING.md) to add material.

Follow along on [LinkedIn](https://www.linkedin.com/in/bernardoforbescosta/) and watch or star this repo for new content.

## Reuse and attribution

This repository is shared under the [MIT License](LICENSE). Linked projects, datasets, and other third-party resources retain their own licenses and attribution requirements; check the original source before reusing them.
