# Standard Library
from concurrent.futures import ThreadPoolExecutor, as_completed

# External
from openai import APIError, OpenAI

# Project
from app.config import API_KEY_CHATGPT, LOGGER


MAX_TOKENS = 150
EXPERT_ROLE = "You are an expert in psychological emotion analysis. You can read perfectly a user comentary, analyze it and determine which potential emotion could be experiencing the user"
DYNAMIC_PROMPT_EMOTION = """
                Analyze the following comentary and determine the psychological emotion contained in it...
                Respond in a single word the feeling that is happening in that emotion.
                Respond in ONLY Spanish language.
                DO NOT REPEAT THE FEELINGS!.

                Here is the comentary:
                """
DYNAMIC_PROMPT_CONCLUSION = """
                            Analyze the following python list that contains the most repeated feelings of users from a certain survey.
                            Build a strong and concise conclusion or summary of that feelings, imaging a fictional survey.
                            The summary MUST BE in Spanish language.

                            Here is the list:
                            """


client = OpenAI(
    api_key=API_KEY_CHATGPT,
)


def analyze_emotion(comentary: str) -> str:
    if not isinstance(comentary, str) or comentary == "":
        return "Comentario vacio o invalido!"

    prompt = f'{DYNAMIC_PROMPT_EMOTION} "{comentary}"'
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": EXPERT_ROLE},
                {"role": "user", "content": prompt},
            ],
            max_tokens=MAX_TOKENS,
        )
        if not isinstance(response.choices[0].message.content, str):
            return "No valid response from the model."
        return response.choices[0].message.content

    except APIError as e:
        LOGGER.error(f"API error occurred: {str(e)}")
        return f"An error occurred: {str(e)}"


def analyze_emotion_wrapper(comentary: str) -> str:
    try:
        return analyze_emotion(comentary)
    except Exception as e:
        LOGGER.error(f"Error in analyzing emotion: {str(e)}")


## 2.a
def feelings_analysis(db_data: list[dict]) -> dict[str, int]:
    all_feeling_comentaries = {}
    with ThreadPoolExecutor() as executor:
        future_to_comentary = {
            executor.submit(analyze_emotion_wrapper, item.get("recomendacion_abierta", "")): item
            for item in db_data
        }
        for future in as_completed(future_to_comentary):
            chatgpt_response = future.result()
            if chatgpt_response in all_feeling_comentaries:
                all_feeling_comentaries[chatgpt_response] += 1
            else:
                all_feeling_comentaries[chatgpt_response] = 1
    return all_feeling_comentaries


def build_conclusion(main_feelings: list[str]) -> str:
    if not isinstance(main_feelings, list):
        return "Invalid list!"

    prompt = f'{DYNAMIC_PROMPT_CONCLUSION} "{main_feelings}"'
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": EXPERT_ROLE},
                {"role": "user", "content": prompt},
            ],
            max_tokens=MAX_TOKENS,
        )
        if not isinstance(response.choices[0].message.content, str):
            return "No valid response from the model."
        return response.choices[0].message.content

    except APIError as e:
        LOGGER.error(f"API error occurred: {str(e)}")
        return f"An error occurred: {str(e)}"


## 2.b
def get_main_issues_conclusion(feelings_data: dict[str, int]) -> tuple[list[str], str]:
    if not feelings_data or not isinstance(feelings_data, dict):
        return "Invalid input. Please provide a non-empty dictionary."

    sorted_feelings = sorted(feelings_data.items(), key=lambda item: item[1], reverse=True)
    top_three_feelings = [feeling for feeling, _ in sorted_feelings[:3]]
    chatgpt_conclusion = build_conclusion(top_three_feelings)
    return (top_three_feelings, chatgpt_conclusion)
