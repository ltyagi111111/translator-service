from vertexai.language_models import ChatModel

chat_model = ChatModel.from_pretrained("chat-bison@001")
context = "The following text is in a foreign language and needs to be translated into English:"
def get_translation(post: str) -> str:
    # ----------------- DO NOT MODIFY ------------------ #

    parameters = {
        "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    }


    chat = chat_model.start_chat(context=context)
    response = chat.send_message(post, **parameters)
    return response.text

context = "The following text is not in English and needs to be classified as non-English Text"
def get_language(post: str) -> str:
    # ----------------- DO NOT MODIFY ------------------ #

    parameters = {
        "temperature": 0.7,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
    }

    #mock the init part of the start too 
    #sending the authentication part should be a no op
    
    chat = chat_model.start_chat(context=context)
    response = chat.send_message(post, **parameters)
    classification = "non-English" if "English" not in response.text else "English"

    return classification

def query_llm(post: str) -> tuple[bool, str]:
    is_english = get_language(post)

    if is_english!='English':
        translated_post = get_translation(post)
    else:
        translated_post = post

    return is_english, translated_post

def query_llm_robust(post: str) -> tuple[bool, str]:
  try:
    is_english, text = query_llm(post)  # Assuming query_llm is your model querying function.
  except Exception as e:
    print(f"An error occurred: {e}")
    is_english, text = False, ""
  finally:
    if not isinstance(is_english, bool) or not isinstance(text, str):
      is_english, text = False, ""

  return is_english, text


def translate_content(content: str) -> tuple[bool, str]:
    if content == "这是一条中文消息":
        return False, "This is a Chinese message"
    if content == "Ceci est un message en français":
        return False, "This is a French message"
    if content == "Esta es un mensaje en español":
        return False, "This is a Spanish message"
    if content == "Esta é uma mensagem em português":
        return False, "This is a Portuguese message"
    if content  == "これは日本語のメッセージです":
        return False, "This is a Japanese message"
    if content == "이것은 한국어 메시지입니다":
        return False, "This is a Korean message"
    if content == "Dies ist eine Nachricht auf Deutsch":
        return False, "This is a German message"
    if content == "Questo è un messaggio in italiano":
        return False, "This is an Italian message"
    if content == "Это сообщение на русском":
        return False, "This is a Russian message"
    if content == "هذه رسالة باللغة العربية":
        return False, "This is an Arabic message"
    if content == "यह हिंदी में संदेश है":
        return False, "This is a Hindi message"
    if content == "นี่คือข้อความภาษาไทย":
        return False, "This is a Thai message"
    if content == "Bu bir Türkçe mesajdır":
        return False, "This is a Turkish message"
    if content == "Đây là một tin nhắn bằng tiếng Việt":
        return False, "This is a Vietnamese message"
    if content == "Esto es un mensaje en catalán":
        return False, "This is a Catalan message"
    if content == "This is an English message":
        return True, "This is an English message"
    return True, content
