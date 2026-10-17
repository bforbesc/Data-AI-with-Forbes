# Projects & experiments

[← Back to the home base](../README.md)

These projects document my experiments with data, software, and AI tools over the years. They are here as historical references and teaching material: what I tried, what the result does, and the questions we can still learn from it.

Building a dashboard, an ML demo, an agent, or a game can be easier with today's tools. Revisiting an older project is a useful way to ask what has changed in the building process and what still needs human judgment.

The code stays in its original repository. This catalogue connects the projects with the learning content here, without duplicating their code or implying that every app is actively maintained. Hosted links below come from the original READMEs; their availability has not been verified.

## GDP Dashboard

**New to coding? [Start with the guided activity](https://github.com/bforbesc/gdp-dashboard#start-here-no-coding).**

**Experiment:** turning country GDP data into an interactive Streamlit dashboard. This repository uses a GDP dashboard template; it is a reference for learning through adaptation.

[Source code](https://github.com/bforbesc/gdp-dashboard) · [App entry point](https://github.com/bforbesc/gdp-dashboard/blob/main/streamlit_app.py)

The app reshapes a wide CSV into country–year observations, filters countries and years, plots GDP over time, and shows endpoint comparisons. Its bundled data covers 1960–2022; it is a historical dataset rather than a live economic feed.

**Learn from it**

- Follow the path from CSV to `melt`, filters, chart, and metrics.
- Compare two date ranges. How does the starting year change the story?
- Find a missing value and inspect how it affects the chart and the endpoint comparison.
- Discuss what extra data and labels you would need to compare living standards rather than total GDP.

**Revisit with today's tools:** rebuild the same interface, then check whether the new version preserves units, missing values, and the meaning of each comparison. Faster implementation still needs careful interpretation.

**Context:** the original README links to [Streamlit's shared GDP dashboard template demo](https://gdp-dashboard-template.streamlit.app/). That is a template reference, not a verified deployment of this repository. Follow the original repository's instructions to run its own code locally. Keep its Apache-2.0 license and upstream attribution when reusing it.

## Clustering Web App

**New to coding? [Start with the guided activity](https://github.com/bforbesc/clustering-web-app#start-here-no-coding).**

**Experiment:** making unsupervised learning explorable through a Streamlit app for cross-sectional data.

[Source code](https://github.com/bforbesc/clustering-web-app) · [App entry point](https://github.com/bforbesc/clustering-web-app/blob/main/ml-web-app.py) · [Hosted link from the original README](https://clustering-web-app.streamlit.app)

The app takes a CSV, preprocesses features, fits KMeans, compares cluster counts using inertia, silhouette scores, and the Davies–Bouldin index, and visualizes the result with t-SNE. KMeans assigns the clusters; t-SNE provides the two-dimensional view.

**Learn from it**

- Start with a clean numeric dataset, without missing values, duplicates, or identifier columns. Use more than 30 rows: the current t-SNE configuration uses perplexity 30, and the app evaluates cluster counts from 2 through 15.
- Change the selected number of clusters. Compare the metrics with the cluster descriptions rather than choosing solely from the plot.
- Trace the standardization step. Why would features measured on very different scales affect the result?
- Ask whether a visually separated group represents a meaningful segment or an artifact of preprocessing and projection.

**Revisit with today's tools:** rebuild the demo with explicit validation, reproducible random seeds, and explanations of what the metrics do and do not establish.

**Context:** this is an older implementation and uses older library APIs, so dependency updates may be necessary. The Davies–Bouldin index is non-negative and lower is better; it is not bounded above by 1. The original README credits [Data Professor](https://github.com/dataprofessor) as inspiration.

## Your Data Wrestler

**New to coding? [Start with the guided activity](https://github.com/bforbesc/Your-Data-Wrestler#start-here-no-coding).**

**Experiment:** an agent that helps wrestle raw data into something you can explore, clean, and visualize.

[Source code](https://github.com/bforbesc/Your-Data-Wrestler) · [Setup and usage](https://github.com/bforbesc/Your-Data-Wrestler#setup) · [Hosted link from the original README](https://your-data-wrestler.streamlit.app/)

The Streamlit app combines data uploads, natural-language questions, cleaning suggestions, and interactive visualizations. The current repository describes Strands Agents with OpenAI models for tool-using data analysis. It is a useful bridge from the [GenAI and agents notebooks](../notebooks/genai-day/) to an application built around a real task.

**Learn from it**

- Use a small synthetic dataset with a known duplicate and missing value. Record the row count and missing-value counts before cleaning.
- Ask the agent to describe the data quality issues, then compare its claims with direct checks.
- Review a suggested cleaning step before applying it. What assumptions would mean imputation or outlier removal introduce?
- Ask a question with a calculable answer, verify it independently, and compare the result with the generated explanation and chart.

**Revisit with today's tools:** compare a fixed analysis workflow with a tool-using agent on the same dataset and questions. Evaluate correctness, repeatability, and how much intervention each needs.

**Context:** AI features require an OpenAI API key and can incur API charges. Use synthetic or public data for teaching; consult the original implementation before uploading private data. Follow the original setup instructions, substituting `https://github.com/bforbesc/Your-Data-Wrestler.git` for the placeholder clone URL in its README. The original credits name @bforbesc and Claudia.

## Arita's Puppy Panic

**New to coding? [Start with the guided activity](https://github.com/bforbesc/arita-the-game#start-here-no-coding).**

**Experiment:** gaming as a playful way to explore building with AI tools.

[Source code](https://github.com/bforbesc/arita-the-game) · [Game description](https://github.com/bforbesc/arita-the-game#readme)

A tiny browser game about protecting a dog from everyday chaos: move left and right, collect bones, hearts, and toys, and avoid poop, brooms, and baths. Reaching the target score reveals a generated puppy picture as a reward.

**Learn from it**

- Play a round and write down the rules before reading the implementation.
- Trace how input, movement, collisions, scoring, and the win condition fit together in `game.js`.
- Change one rule, such as the target score or an object's behavior. Predict the effect on difficulty before testing.
- Compare keyboard and drag controls. Is the feedback clear enough to understand what happened?

**Revisit with today's tools:** prototype a variation from a short brief, then check the generated behavior against explicit rules. The teaching focus is the development experiment; this catalogue does not claim the game uses an AI model at runtime.

**Try locally:** clone the repository, change into that folder, and run:

```bash
git clone https://github.com/bforbesc/arita-the-game.git
cd arita-the-game
python3 -m http.server 4173 --bind 127.0.0.1
```

Open [localhost:4173](http://localhost:4173), press **Start round**, and use the arrow keys or drag on the game area. These commands replace the author-specific absolute folder path shown in the original README. A hosted deployment is not listed here.

## Add the next experiment

Use the [project template](TEMPLATE.md) to record the motivation, original source, what someone can learn, and what you would do differently today. Add a short entry to the home page so the collection remains easy to discover.
