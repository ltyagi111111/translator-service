from src.translator import translate_content #,query_llm_robust
# from mock import patch
# from vertexai.language_models import ChatModel, InputOutputTextPair
# from ../src/translator import query_llm_robust

# @patch('vertexai.language_models._PreviewChatSession.send_message')
# def test_unexpected_language(mocker):
#   #copied 
#   # we mock the model's response to return a random message
#   mocker.return_value.text = "I don't understand your request"
#   response = query_llm_robust("Aquí está su primer ejemplo.")
#   #
#   assert query_llm_robust("Aquí está su primer ejemplo.")
#   mocker.assert_called_once()
#   mocker.assert_called_with("Aquí está su primer ejemplo.")
#   assert response == "I don't understand your request"
#   assert response is not None and response != ""

### UNIT TESTING ###
def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert ("chinese" in translated_content or "Chinese" in translated_content)


def test_llm_normal_response():
    is_english, translated_content = translate_content("to be or not to be")
    assert is_english == True
    assert ("to be or not to be"== translated_content.lower())
    

def test_llm_gibberish_response():
    is_english, translated_content = translate_content("jfdjshghui bjfhsdufh")
    assert ((is_english == False) or (translated_content == "jfdjshghui bjfhsdufh"))
    