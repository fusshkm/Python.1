# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-3ec8cd1376934c47be8d31162c21c0a4", base_url="https://api.deepseek.com")

def create_message(role,content):
    """
    创建标准的消息格式，包括用户、助手或系统消息。

    参数：
    role (str):消息的角色，值为"user"、"assistant" 或 “system”。
    content (str or list): 消息的内容，可以是字符串(文本)或包含文本和图像的数组。

    返回：
    dict: 符合 OpenAI API 要求的消息格式。
    """

    return{
        "role": role,
        "content": content
    }

def process_user_input(input_text):
    """
    根据用户输入的内容，生成对应的消息格式。

    参数：
    input_text (str): 用户的输入文本。

    返回：
    dict:生成的用户消息。
    """

    return create_message("user",input_text)

def chat_with_DeepSeek(client,messages):
    """
    使用 DeekSeek 模型进行多轮对话的核心函数。

    参数：
    client (OpenAI)：实例化的OpenAI 客户端。
    messages (list): 包含对话上下文的消息列表，包括用户、助手和系统消息。

    返回：
    str:模型生成的回复内容。
    """


    response = client.chat.completions.create(
       model = "deepseek-chat", # 使用deepseek-chat 模型
       messages = messages
    )

    # 提取并返回助手生成的回复内容
    return response.choices[0].message.content

def multi_round_chat():
    """
    多轮对话机器人示例函数
    """
    # 初始化消息列表,包含系统信息
    messages = []

    # 创建系统信息，设置对话的上下文
    system_message = create_message("system","you are a helpful assistant.")
    messages.append(system_message)

    while True:

        #捕获用户输入
        user_input = input("User: ")

        #处理用户输入并生成相应的信息
        user_message = process_user_input(user_input)
        messages.append(user_message)

        #调用DeekSeek 模型进行回答
        assistant_reply = chat_with_DeepSeek(client,messages)
        print(assistant_reply)

        # 将助手回复添加到消息列表，多轮对话必备
        messages.append(create_message("assistant",assistant_reply))

        # 提供退出机制，用户可以输入 'exit' 退出对话
        if user_input.lower() == 'exit':
            print("对话结束.")
            break
if __name__ == '__main__':
    multi_round_chat()