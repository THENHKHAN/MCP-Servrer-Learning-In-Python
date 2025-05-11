# 🧠 MCP Server Learning in Python

## 📘 Overview

The **Model Context Protocol (MCP)** allows you to build servers that expose **data** and **functionality** to LLM (Large Language Model) applications in a **secure**, **modular**, and **standardized** way.

Think of it as a specialized **web API** tailored for LLMs.

### ✨ What MCP Servers Can Do

- 🔍 **Resources**: Expose data (like `GET` endpoints) – used to load context into the LLM.
- 🛠️ **Tools**: Provide functionality (like `POST` endpoints) – used to run code or cause side effects.
- 💬 **Prompts**: Define reusable templates for interacting with LLMs.
- 📦 And much more!

---

## 🎯 Project Purpose

This repository is a **learning sandbox** for MCP servers, covering:
- 🚀 Basic starter examples
- 📁 Small to large projects
- 🔬 Experimentation with different MCP patterns

Whether you're new to MCP or want to build serious projects with it, this repo will grow alongside your understanding.

---

🧠 MCP Primitives
🗃️ Resources – Like read-only APIs (GET) for loading data into LLM context

🛠️ Tools – Like actions (POST) that trigger side effects

🧾 Prompts – Templated user interaction patterns

## 🧩 What is the MCP Python SDK?

The **Model Context Protocol (MCP) Python SDK** is the official tool for building structured, standardized interfaces between LLMs and external tools or data sources. It supports building both **servers** and **clients** that communicate using defined primitives.

---

## 🧠 Prerequisite Knowledge

This quickstart assumes you have familiarity with the following concepts:

- **Python**: Basic to intermediate knowledge of Python programming.
- **LLMs**: Familiarity with Large Language Models (LLMs) like Claude.

If you're not familiar with these technologies, we recommend reviewing relevant documentation or tutorials before proceeding.

---

## 🖥️ System Requirements

To use this SDK, ensure your system meets the following requirements:

- **Python**: Version 3.10 or higher is required. You can verify your Python version by running:

  ```bash
  python --version
