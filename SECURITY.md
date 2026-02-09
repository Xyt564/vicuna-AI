# 🔐 Security Policy

## Overview

This project is a **local, offline AI CLI chatbot** built using **Vicuna-7B v1.5** and **llama.cpp**.

It does **not** expose network services, APIs, or web interfaces by default.
All model inference runs **locally on the user’s machine**.

That said, security still matters — especially when running large native libraries and models.

---

## Supported Versions

This project does **not** currently maintain versioned security support.

Only the **latest commit** in the repository should be considered supported.

Older commits may contain bugs, outdated dependencies, or unresolved issues.

---

## Threat Model & Scope

### What this project **does NOT** do:

* ❌ No network listeners
* ❌ No remote connections
* ❌ No cloud APIs
* ❌ No telemetry or data collection
* ❌ No authentication or user accounts

### What this project **does** rely on:

* Local execution of:

  * Python
  * `llama-cpp-python`
  * A GGUF model file supplied by the user

Security risks are therefore mostly limited to:

* Local code execution
* Dependency vulnerabilities
* Malicious or corrupted model files

---

## Model File Safety

⚠️ **Model files are large binary blobs and should be treated with care.**

Recommendations:

* Only download models from **trusted sources**
* Prefer official Hugging Face repositories
* Do **not** run unknown or modified GGUF files from untrusted sources

The recommended model for this project:

```
vicuna-7b-v1.5.Q4_K_M.gguf
```

Downloaded from:

* [https://huggingface.co/TheBloke/vicuna-7B-v1.5-GGUF](https://huggingface.co/TheBloke/vicuna-7B-v1.5-GGUF)

---

## Dependency Security

This project intentionally keeps dependencies minimal.

Primary dependency:

* `llama-cpp-python`

Recommendations:

* Keep Python up to date
* Regularly update `llama-cpp-python`
* Avoid installing unrelated or unofficial forks unless you understand the risks

Install dependencies using trusted package sources only:

```bash
pip install llama-cpp-python
```

---

## Denial of Service & Resource Exhaustion

Large language models are **resource-intensive** by nature.

Potential issues:

* High CPU usage
* High RAM usage
* Long-running inference loops

Mitigations:

* Press **`Ctrl + C`** to interrupt model output at any time
* Type **`exit`** to safely quit the chatbot
* Adjust context size (`N_CTX`) if memory usage is too high

This project makes **no guarantees** regarding stability on low-memory or unsupported systems.

---

## Reporting Security Issues

If you discover a **security vulnerability**, **crash**, or **unsafe behavior**:

* Please open a **GitHub Issue**
* Clearly label it as **Security**
* Include:

  * OS
  * Hardware specs
  * Python version
  * `llama-cpp-python` version
  * Steps to reproduce (if possible)

⚠️ This is a solo / small-scale project.
There is **no guaranteed response time**, but reports are appreciated.

---

## Responsible Usage

This software is provided for **educational and personal use**.

You are responsible for:

* How you run it
* What models you load
* What code you modify or execute

The author assumes **no liability** for misuse, data loss, or system instability.

---

## Disclaimer

This project is provided **“as is”**, without warranty of any kind.

Use at your own risk.

---
