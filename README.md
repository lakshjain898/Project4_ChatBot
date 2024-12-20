# Chatbot Using NLTK

This project is a simple chatbot built using Python and the NLTK (Natural Language Toolkit) library. The chatbot is capable of engaging in basic conversations and responding to user inputs. It is designed to provide a starting point for natural language processing (NLP) enthusiasts.

---

## Features

- **Basic Conversations**: The chatbot can respond to general queries and engage in casual conversations.
- **Customizable Reflections**: Uses reflections to make responses more dynamic and human-like.
- **Conversation Logging**: Keeps track of all user-chatbot interactions in a `chatbot_log.txt` file for reference or debugging.
- **Fallback Responses**: Handles unknown inputs gracefully with default replies.

---

## Installation and Setup

### Prerequisites
1. Python 3.6 or higher
2. NLTK Library

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/chatbot_nltk.git
   ```
2. Navigate to the project directory:
   ```bash
   cd chatbot_nltk
   ```
3. Install the required library:
   ```bash
   pip install nltk
   ```
4. Run the chatbot script:
   ```bash
   python chatbot.py
   ```

---

## How It Works

1. **Chat Logic**: The chatbot uses a predefined set of patterns and responses for its conversations. Patterns are regular expressions that match user inputs, and responses are predefined replies to those patterns.
2. **Reflections**: Reflections are used to modify user input dynamically, making the chatbot's responses more personalized. For instance, replacing "I" with "you" in user input.
3. **Logging**: All conversations are saved in `chatbot_log.txt`, which is created in the same directory as the script.

---

## Example Interaction

**User**: Hello!

**Chatbot**: Hi there! How can I assist you today?

**User**: What can you do?

**Chatbot**: I can engage in basic conversations and respond to your queries.

**User**: Bye!

**Chatbot**: Goodbye! Have a great day!

---

## Customization

### Adding New Patterns and Responses
You can add more patterns and responses in the chatbot's script to enhance its capabilities. Simply edit the `pairs` list in the code:
```python
pairs = [
    [r"your pattern here", ["response 1", "response 2"]]
]
```

### Changing Reflections
Modify the `reflections` dictionary to customize how user inputs are altered:
```python
reflections = {
    "I am": "you are",
    "I": "you",
    "my": "your"
}
```

---

## Contributing

Contributions are welcome! Feel free to fork this repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

---


## Acknowledgments

- **NLTK Documentation**: [Natural Language Toolkit](https://www.nltk.org/)
- Inspired by the NLTK `chat` module examples.

---

