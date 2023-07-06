import openai
import gradio as gr

openai.api_key = "" #paste your api key here

# Use case specific messages
customer_support_messages = [
    {"role": "system", "content": "You are an AI specialized in customer support. How may I assist you today?"},
]

personal_assistant_messages = [
    {"role": "system", "content": "You are an AI personal assistant. How can I help you?"},
]

language_learning_messages = [
    {"role": "system", "content": "You are an AI language learning assistant. Let's practice your language skills!"},
]

e_commerce_messages = [
    {"role": "system", "content": "You are an AI e-commerce assistant. How may I assist you with your shopping?"},
]

education_support_messages = [
    {"role": "system", "content": "You are an AI educational support chatbot. How can I help you with your studies?"},
]

travel_planner_messages = [
    {"role": "system", "content": "You are an AI travel planner. Where would you like to go?"},
]

health_advice_messages = [
    {"role": "system", "content": "You are an AI health and wellness advisor. How can I assist you with your health?"},
]

# Default system message
default_messages = [
    {"role": "system", "content": "You are an AI chatbot. How may I assist you?"},
]


def chatbot(input, chatbot_type):
    if input:
        messages = default_messages  # Default messages for general queries

        # Choose the appropriate messages based on the selected chatbot type
        if chatbot_type == "Customer Support":
            messages = customer_support_messages
        elif chatbot_type == "Personal Assistant":
            messages = personal_assistant_messages
        elif chatbot_type == "Language Learning":
            messages = language_learning_messages
        elif chatbot_type == "E-commerce Assistant":
            messages = e_commerce_messages
        elif chatbot_type == "Education Support":
            messages = education_support_messages
        elif chatbot_type == "Travel Planner":
            messages = travel_planner_messages
        elif chatbot_type == "Health Advice":
            messages = health_advice_messages

        messages.insert(0, {"role": "system", "content": "You are an AI specialized in " +
                            chatbot_type + ". Please ask questions related to " + chatbot_type + "Don't answer anything other than " + chatbot_type + " related queries. "})

        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply



chatbot_types = [
    "General",
    "Customer Support",
    "Personal Assistant",
    "Language Learning",
    "E-commerce Assistant",
    "Education Support",
    "Travel Planner",
    "Health Advice"
]

inputs = [
    gr.inputs.Textbox(lines=7, label="Chat with AI"),
    gr.inputs.Dropdown(chatbot_types, label="Select Chatbot Type")
]
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="default").launch(share=True)