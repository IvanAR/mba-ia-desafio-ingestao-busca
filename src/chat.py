from model import get_chat_model
from search import search_prompt

model = get_chat_model()

def main():
    print("Chat started. Write 'exit' to end.\n")

    while True:
        user_input = input("Write yout question about Amulet Titan deck: \n").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("Ending chat.")
            break

        try:
            prompt = search_prompt(user_input)
            response = model.invoke(prompt)
            print(f"Gemini: {response.content}\n", flush=True)
        except Exception as e:
            print(f"Error: {e}\n", flush=True)

if __name__ == "__main__":
    main()