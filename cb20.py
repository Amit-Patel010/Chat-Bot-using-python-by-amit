import wikipedia

wikipedia.set_lang("en")
wikipedia.set_user_agent("myWikipediaChatbot/1.0 (your_email@example.com)")

def fetch_wikipedia_data(query):
    """Fetch data from Wikipedia based on the query."""
    try:
        result = wikipedia.summary(query, sentences=3) 
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Sorry, there are multiple articles related to '{query}': {e.options}"
    except wikipedia.exceptions.HTTPTimeoutError:
        return "The request timed out. Please try again later."
    except wikipedia.exceptions.RedirectError:
        return "The page you requested has been redirected to another page."
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find an article on that topic."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def chatbot():
    print("Hello! I am a Wikipedia-based chatbot.")
    print("Ask me anything, and I will try to provide an accurate answer from Wikipedia.")
    print("Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        answer = fetch_wikipedia_data(user_input)
        print(f"Bot: {answer}")

if __name__ == "__main__":
    chatbot()
