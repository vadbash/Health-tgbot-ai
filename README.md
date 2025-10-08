# Health-tgbot-ai

A Telegram bot powered by AI for health-oriented assistance.

## Overview

**Health-tgbot-ai** is a Python-based Telegram bot designed to provide health-related support using AI. It integrates Telegram’s messaging capabilities with AI models (e.g. GPT) to respond to user queries, offer suggestions, and assist with wellness topics.

Key capabilities include:

-   Conversational health advice (within limitations)

-   Responding to user messages with AI-generated replies

-   Configurable via a simple config file

-   Lightweight and easy to deploy
  
## Prerequisites

Before running the bot, you’ll need:

-   A Telegram bot token (from BotFather)
    
-   An AI / LLM API key (e.g. OpenAI)
    
-   Python 3.7+
    

## Installation & Setup

1.  Clone the repo:
    
    `git clone https://github.com/vadbash/Health-tgbot-ai.git`
    
2.  Create a virtual environment and install dependencies:
    
    ``pip install -r requirements.txt`` 
    
3.  Configure the bot:
    
    -   Open `config.py`
        
    -   Insert your Telegram bot token and AI API key (and any other settings)
        
4.  Run the bot:
    
    `python bot.py` 
    

## Usage

Once running, users can:

-   Send health-oriented queries to the bot (e.g. “How can I improve sleep?”)
    
-   Receive AI-powered responses