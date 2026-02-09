# 🧠 AI CLI Chatbot (Vicuna-7B v1.5 + llama.cpp)

A **local, terminal-based AI chatbot** powered by **Vicuna-7B v1.5** running through **llama.cpp**.

This is not a gimmick script or a novelty demo.
It’s a **half-decent, genuinely usable local LLM** that can write **paragraphs, code, explanations**, and hold coherent conversations **without rambling itself into oblivion**.

No cloud.
No API keys.
No subscriptions.
Just your machine and a real model.

---

## ✨ Features

* 🧠 **Vicuna-7B v1.5** instruction-tuned model
* ⚡ **llama.cpp backend** (CPU-friendly)
* 💬 Live streaming responses (token by token)
* 🧾 Conversation memory
* 🎨 Colored CLI output
* 🧹 Built-in commands (`help`, `clear`, `exit`)
* 🧩 Simple, readable Python — easy to modify

---

## 🖥️ Tested Hardware (Important)

This project has **ONLY been tested** on the following hardware:

* **CPU:** 12th Gen Intel i3-1215U (8 cores) @ 4.40 GHz
* **GPU:** Intel Alder Lake-UP3 GT1 (UHD Graphics)
* **RAM:** 8 GB DDR4
* **OS:** Linux

⚠️ **No guarantees** are made for other systems.
Different CPUs, RAM amounts, or operating systems **may behave differently**.

Use this project **at your own risk**.

If performance is too slow or your system struggles:

* Press **`Ctrl + C`** to stop the AI mid-response
* Type **`exit`** to cleanly quit the chatbot

---

## 📦 Requirements

There is **no `requirements.txt`** by design.

### You only need:

* **Python 3.9+**
* **llama-cpp-python**

Install the dependency:

```bash
pip install llama-cpp-python
```

That’s it.
No PyTorch. No Transformers. No CUDA setup.

---

## 🧠 Model (Required Download)

This project uses the following model:

**Model name:**

```
vicuna-7b-v1.5.Q4_K_M.gguf
```

**Download from Hugging Face (≈4–5 GB):**
[https://huggingface.co/TheBloke/vicuna-7B-v1.5-GGUF](https://huggingface.co/TheBloke/vicuna-7B-v1.5-GGUF)

> GitHub does not allow files this large, so the model is **not included** in the repository.

---

## 📁 Folder Structure (Very Important)

Set your project up like this:

```
ai-cli-chatbot/
│
├── chatbot.py
└── models/
    └── vicuna-7b-v1.5.Q4_K_M.gguf
```

### Rules:

* Put the **Python script and `models/` folder in the same directory**
* Put the **GGUF model inside `models/`**
* The code will handle the rest automatically

No extra configuration needed.

---

## ▶️ Usage

Run the chatbot:

```bash
python3 chatbot.py
```

### Commands inside the chatbot:

| Command         | Description                       |
| --------------- | --------------------------------- |
| `help`          | Show available commands           |
| `clear`         | Clear conversation history        |
| `exit` / `quit` | Exit the chatbot                  |
| `Ctrl + C`      | Interrupt AI response immediately |

---

## 🧪 What This Model Can Actually Do

This isn’t just a “hello world” LLM.

It can:

* Write **multi-paragraph text**
* Generate **code**
* Explain technical concepts
* Hold structured conversations
* Stay on-topic reasonably well

Especially impressive considering it runs **CPU-only on 8 GB RAM**.

---

## ⚙️ Configuration (Optional)

Inside the script:

```python
N_CTX = 2048
N_GPU_LAYERS = 0
```

* Increase `N_CTX` for longer memory (uses more RAM)
* Increase `N_GPU_LAYERS` **only** if your system supports it

---

## 📌 Notes

* Fully **local** — nothing leaves your machine
* No telemetry, tracking, or API calls
* Performance depends heavily on your hardware
* Expect slower responses on weaker systems

---

## 📄 License

This project is licensed under the **MIT License**.

### MIT License

```
MIT License

Copyright (c) 2026 Xyt564

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---
