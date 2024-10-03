import ollama
import time


def run_conversation(user_input):
    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": f"{user_input}",
            },
        ],
    )
    return response["message"]["content"]

if __name__=="__main__":
    while True:
        user_input=input()
        if user_input.lower()=="exit" or "quit":
            break
        else:
            start_time=time.time()
            print(run_conversation(user_input))
            end_time=time.time()
            print("Total time taken to execute program:",end_time-start_time)
