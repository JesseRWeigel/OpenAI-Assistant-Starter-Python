import time
import openai

# Load the .env file
from dotenv import load_dotenv
load_dotenv()


# Create a client instance
client = openai.Client()

# Step 1: Create an Assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

# Step 2: Create a Thread
thread = client.beta.threads.create()

# Step 3: Add a Message to a Thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

# Step 4: Run the Assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account."
)

# Optionally, wait for the run to complete and retrieve the result
while True:
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    if run.status == "completed":
        break
    time.sleep(1)

# Step 5: Display the Assistant's Response
messages = client.beta.threads.messages.list(
    thread_id=thread.id
)
