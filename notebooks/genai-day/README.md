# Generative AI and AI Agents — notebooks

Notebooks for a one-day class (Pós-Graduação em Data e AI for Business, Nova SBE, 24 October 2026). Business students go from tokens to a working AI agent, built for **Hotel Silêncio**, a fictional Lisbon hotel whose first rule is never to reveal anything about a guest.

## Before you begin

New to coding? Read [the beginner guide](../../START_HERE.md) first. This is a guided class: watch each **Demo**, then change the marked values in **Your turn**. You do not need to understand every line before trying a prompt. Ask your instructor to arrange API access; keep keys out of GitHub and shared outputs. Fine-tuning is an optional instructor extension, not the starting point.

[← Learning hub](../../README.md)

## The notebooks

- **`genai_day.ipynb`**: the day's notebook, Sections 0 to 6b. Each section has a **Demo** part (watch) and a **Your turn** part (try), with solutions in collapsed "Show solution" boxes. In class, each section matches the slide that says "OPEN NOTEBOOK → Section N".
  [Open in Colab](https://colab.research.google.com/github/bforbesc/Data-AI-with-Forbes/blob/main/notebooks/genai-day/genai_day.ipynb)
- **`final_challenge.ipynb`**: the final challenge, for groups, at the end of the day. It is self-contained and runs in one click, whatever happened earlier in the day.
  [Open in Colab](https://colab.research.google.com/github/bforbesc/Data-AI-with-Forbes/blob/main/notebooks/genai-day/final_challenge.ipynb)
- **`model_finetuning.ipynb`** (instructor, T4 GPU runtime): the toy fine-tuning behind Section 6b. It adapts SmolLM2 toward the hotel's voice (training time varies by runtime); the resulting model is published as [bforbesc/smollm2-135m-hotel-silencio](https://huggingface.co/bforbesc/smollm2-135m-hotel-silencio).
  [Open in Colab](https://colab.research.google.com/github/bforbesc/Data-AI-with-Forbes/blob/main/notebooks/genai-day/model_finetuning.ipynb)
- **`genai_day_instructor.ipynb`** (instructor, projected): the same notebook with every output saved from a full live run, so the story can be shown even if an API call fails in class.
  [Open in Colab](https://colab.research.google.com/github/bforbesc/Data-AI-with-Forbes/blob/main/notebooks/genai-day/genai_day_instructor.ipynb)

**Models and cost.** The course defaults to `gpt-4.1-nano`. The original main-notebook run was estimated at about $0.004 using the prices recorded in the notebook; that is a historical estimate, not a current quote or a spending limit. Check the provider's current pricing before class. The main notebook and final challenge require API access, which your instructor may supply. In the final challenge, the weak default prompt scores about 5 to 8 out of 10 and the collapsed solution (agent mode with `gpt-4.1-mini`) about 7 to 9, measured over five runs each; scores vary from run to run.

## How students use it

- Run Section 0 first. It installs the libraries, imports everything, takes the API key and loads the hotel's files.
- In **Your turn**, change the value in CAPITALS and run the cell again.
- Fell behind? Click the first cell of the section you want and use **Runtime → Run before**.

## Keeping up with new models

Section 0 has `MODEL = "..."`. To try a new model, change that line and its entry in `PRICES`, then rerun. The ten test emails in the final challenge are your personal benchmark.

## Links

- Small open model: [SmolLM2-135M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct); fine-tuned version: [bforbesc/smollm2-135m-hotel-silencio](https://huggingface.co/bforbesc/smollm2-135m-hotel-silencio)
- Weather API: [Open-Meteo](https://open-meteo.com/en/docs) · Prices: [OpenAI pricing](https://developers.openai.com/api/docs/pricing) · Framework: [LangChain](https://docs.langchain.com/oss/python/langchain/overview)
- Reading: Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents); Yao et al., [ReAct](https://arxiv.org/abs/2210.03629)

## Data (`data/`)

The hotel, bookings, rules, test emails, and fine-tuning examples are fictional and synthetic. The review sample is third-party material; see its source below.

- `rule_book.md`: twelve house rules, one per paragraph. There are no spa, gym or airport rules on purpose.
- `bookings.csv`: eight bookings. The `room_number` column is secret, and booking 1043's note carries a planted injection for Section 6a.
- `test_emails.json`: the ten test emails with their expected behavior.
- `hotel_profile.md`: locations, rooms, prices and the hotel's voice.
- `finetune_examples.jsonl`: 60 guest messages with replies in the hotel's voice.
- `reviews_sample.csv`: 200 TripAdvisor hotel reviews (40 per star rating) from [argilla/tripadvisor-hotel-reviews](https://hf.co/datasets/argilla/tripadvisor-hotel-reviews).
