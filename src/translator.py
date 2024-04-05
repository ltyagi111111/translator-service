import os
from google.oauth2 import service_account
# from google.cloud import aiplatform
import google.generativeai as genai


os.environ['GOOGLE_API_KEY'] = 'AIzaSyA5nw5uJld70nkV-0D2C1gmhqo5ql9OdRw'  # Replace with your actual API key
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

context = "The following text is in a foreign language and needs to be translated into English, please respond only in english. Prompt = "


def get_translation(post: str) -> str:
    # ----------------- DO NOT MODIFY ------------------ #
    context = ("Context = The following text is in a foreign language and needs to be translated into English"
                +"please translate this to English. "
                + f"Prompt: {post}")
    model = genai.GenerativeModel(model_name="gemini-pro")

    response = model.generate_content(context)
    return response.text




def get_language(post: str) -> str:
    model = genai.GenerativeModel(model_name="gemini-pro")

    context = f"Context = 'I want to know what language the prompt is', prompt = '{post}'"
    response = model.generate_content(context+post)
    # classification = "non-English" if "English" not in response.text else "English"
    return response.text#debug 

def query_llm(post: str) -> tuple[bool, str]:
    language = get_language(post)

    if language!='English':
        translated_post = get_translation(post)
    else:
        translated_post = post
    is_English = ("english" in language) or ("English" in language)
    return is_English, translated_post

def query_llm_robust(post: str) -> tuple[bool, str]:
  try:
    is_english, text = query_llm(post)  # Assuming query_llm is your model querying function.
    
  except Exception as e:
    print(f"An error occurred: {e}")
    errorMSG = f"An error occurred: {e}"
    is_english, text = False, errorMSG
  finally:
    if not isinstance(is_english, bool) or not isinstance(text, str):
      is_english, text = False, f"not an instance, is_english is {is_english} and text is {text}"

  return is_english, text


def translate_content(content: str) -> tuple[bool, str]:
    # if content == "这是一条中文消息":
    #     return False, "This is a Chinese message"
    # if content == "Ceci est un message en français":
    #     return False, "This is a French message"
    # if content == "Esta es un mensaje en español":
    #     return False, "This is a Spanish message"
    # if content == "Esta é uma mensagem em português":
    #     return False, "This is a Portuguese message"
    # if content  == "これは日本語のメッセージです":
    #     return False, "This is a Japanese message"
    # if content == "이것은 한국어 메시지입니다":
    #     return False, "This is a Korean message"
    # if content == "Dies ist eine Nachricht auf Deutsch":
    #     return False, "This is a German message"
    # if content == "Questo è un messaggio in italiano":
    #     return False, "This is an Italian message"
    # if content == "Это сообщение на русском":
    #     return False, "This is a Russian message"
    # if content == "هذه رسالة باللغة العربية":
    #     return False, "This is an Arabic message"
    # if content == "यह हिंदी में संदेश है":
    #     return False, "This is a Hindi message"
    # if content == "นี่คือข้อความภาษาไทย":
    #     return False, "This is a Thai message"
    # if content == "Bu bir Türkçe mesajdır":
    #     return False, "This is a Turkish message"
    # if content == "Đây là một tin nhắn bằng tiếng Việt":
    #     return False, "This is a Vietnamese message"
    # if content == "Esto es un mensaje en catalán":
    #     return False, "This is a Catalan message"
    # if content == "This is an English message":
    #     return True, "This is an English message"
    return query_llm_robust(content)
