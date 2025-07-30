# 导入假模型和链工具
from langchain_community.llms.fake import FakeListLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

# 1. 创建假模型，设置固定回复内容
llm = FakeListLLM(responses=[
    "北京今天天气晴朗，气温 25℃。",
    "上海今天有小雨，气温 22℃。",
    "广州今天多云，气温 28℃。"
])

# 2. 定义提问模板
prompt = PromptTemplate(
    input_variables=["city"],
    template="查询 {city} 的天气情况。"
)

# 3. 创建简单的问答链（替代旧的 LLMChain，避免 deprecation 警告）
chain = RunnableSequence(prompt | llm)

# 4. 测试运行
if __name__ == "__main__":
    # 测试三个城市
    result1 = chain.invoke({"city": "北京"})
    print(f"北京天气: {result1}")

    result2 = chain.invoke({"city": "上海"})
    print(f"上海天气: {result2}")

    result3 = chain.invoke({"city": "广州"})
    print(f"广州天气: {result3}")