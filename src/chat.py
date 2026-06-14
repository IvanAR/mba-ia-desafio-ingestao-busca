from model import get_chat_model
from search import search_prompt

model = get_chat_model()

def main():
    print("Chat iniciado\n")

    while True:
        user_input = input("O que deseja saber hoje? \n").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("Finalizando chat.")
            break

        try:
            prompt = search_prompt(user_input)
            response = model.invoke(prompt)
            print(f"Gemini: {response.content}\n", flush=True)
        except Exception as e:
            print(f"Erro: {e}\n", flush=True)

if __name__ == "__main__":
    main()