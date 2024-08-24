from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

template = """
面白い回答を考えてください。
お題: {お題}
"""

prompt = ChatPromptTemplate.from_template(template)

llm = ChatOllama(model="neoai-8b-chat:latest")

chain = prompt | llm | StrOutputParser()

print(chain.invoke({"お題": "あなたが一つのスーパーパワーを持てるとしたら、どんな力を選びますか？"}))
