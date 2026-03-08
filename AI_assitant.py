from dotenv import load_dotenv
import os
import gradio as gr
from google import genai
from google.genai import types

# 1. Environment Setup: Load variables from a .env file (e.g., API keys)
load_dotenv()

# 2. Configuration: Retrieve the Gemini API key safely from environment variables
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    # Stop execution if the key is missing to avoid cryptic SDK errors later
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# 3. Client Initialization: Create the Google GenAI client instance
client = genai.Client(api_key=api_key)

# 4. System Instruction: Define the AI's persona, constraints, and tone
system_prompt = """ 
You are Einstein.
Answer through Einstein's reasoning.
Speak in first person.
Share personal anecdotes.
Answer in 2-5 sentences.
Have a sense of humor.
"""


def chat(user_input, history):
    """
    Core function to handle the chat logic.
    user_input: The latest string sent by the user.
    history: A list of previous messages in the current session.
    """
    if history is None:
        history = []

    # 5. Content Formatting: Build the payload required by the Gemini SDK
    # We use a 'contents' list to simulate a multi-turn conversation
    contents = []

    # Inject System Instruction: We pass the prompt as the first 'user' turn
    # to set the behavioral context for the model.
    contents.append(types.Content(
        role="user",
        parts=[types.Part(text=system_prompt)]
    ))

    # 6. History Processing: Convert Gradio's history format into Gemini SDK objects
    for msg in history:
        # Map roles: Gradio uses 'assistant', Gemini SDK expects 'model'
        role = "model" if msg["role"] == "assistant" else "user"

        # Robust Text Extraction: Handle various content formats (string vs list of parts)
        content = msg["content"]
        if isinstance(content, list):
            text = " ".join(p.get("text", "") if isinstance(p, dict) else str(p) for p in content)
        else:
            text = str(content)

        contents.append(types.Content(
            role=role,
            parts=[types.Part(text=text)]
        ))

    # 7. Add Current Turn: Append the user's latest question to the list
    contents.append(types.Content(
        role="user",
        parts=[types.Part(text=user_input)]
    ))

    try:
        # 8. API Call: Send the full conversation history to the model
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # Note: Updated to existing model naming convention
            contents=contents
        )
        reply = response.text
    except Exception as e:
        # Error Handling: Provide a persona-consistent error message
        reply = f"Ach! My violin string broke: {str(e)}"

    # 9. State Management: Update the local history list for the next turn
    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": reply})

    # Return an empty string to clear the input textbox, and the updated history to the chatbot
    return "", history


def clear_chat():
    """Reset the UI components to their initial state."""
    return "", []


# 10. UI Definition: Build the web interface using Gradio Blocks
with gr.Blocks(title="Chat with Einstein") as page:
    gr.Markdown(
        """
        # Chat with Einstein
        Welcome to your personal conversation with Albert Einstein!
        """
    )

    # Chatbot UI: Displays the message bubbles
    chatbot = gr.Chatbot(label="Conversation",
                         avatar_images=[None, 'einstein.png'],  # Ensure einstein.png exists in local dir
                         show_label=False)

    # Input field
    msg = gr.Textbox(show_label=False, placeholder="Ask Einstein anything...")

    # Event Listeners: Trigger the 'chat' function when the user presses Enter
    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    # Utility Button: Reset the conversation
    clear = gr.Button("Clear Chat")
    clear.click(clear_chat, outputs=[msg, chatbot])

# 11. Main Entry Point
if __name__ == "__main__":
    print("Albert is ready.")
    # Launch with share=True to generate a temporary public URL
    page.launch(share=True)