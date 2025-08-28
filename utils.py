from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from prompt import user_goal_prompt

def generate_learning_path(google_api_key: str, user_goal: str) -> str:
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=google_api_key)

    # Combine goal with prompt
    learning_path_prompt = f"User Goal: {user_goal}\n{user_goal_prompt}"

    response = model.invoke([HumanMessage(content=learning_path_prompt)])
    
    return response.content
