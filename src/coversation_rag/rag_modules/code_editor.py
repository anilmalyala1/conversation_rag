import re
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import find_dotenv,load_dotenv

def extract_code_from_markdown(response: str) -> str:
    # Match triple backtick block with optional language specifier
    match = re.search(r"```(?:java)?\n(.*?)```", response, re.DOTALL)
    return match.group(1).strip() if match else response.strip()

def edit_code(filepath: str, instruction: str):
    load_dotenv(find_dotenv())
    # Read current code
    with open(filepath, "r") as f:
        code = f.read()

    # Save a backup
    with open(filepath + ".bak", "w") as f:
        f.write(code)

    # Prepare LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Construct prompt
    messages = [
        SystemMessage(content="You are a senior Java developer. Modify code as per user's instruction."),
        HumanMessage(content=f"""Here is the code:\n\n{code}\n\nInstruction:\n{instruction}\n\n.""")
    ]

    # Run OpenAI LLM
    response = llm(messages).content



    # Remove markdown formatting
    clean_code = extract_code_from_markdown(response)




        # Save updated code
    with open(filepath, "w") as f:
        f.write(clean_code)

    return {
        "text": f"✅ Updated {filepath}, original saved as .bak",
        "code": clean_code
    }
