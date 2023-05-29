import streamlit as st
import openai
import pandas as pd
import os
from tqdm import tqdm
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
# import my_key = ""
my_key = "sk-peYuSGE12SKtWtDH9hxx9ZztJv4Fn4ADDKO5AjVmLOI7CNgw"

# 设置页面宽度为较宽的布局
st.set_page_config(layout="wide")

# OPENAI_API_BASE = "https://api.chatanywhere.com.cn/v1"

openai.api_base = "https://api.chatanywhere.com.cn/v1"

default_api_url = openai.api_base
print("Default API URL:", default_api_url)
# Set the environment variable OPENAI_API_BASE
# os.environ["OPENAI_API_BASE"] = OPENAI_API_BASE

def analyze_resume(jd, resume, options):
    """
    通过对输入的简历进行综合分析，评估候选人与给定职位的匹配程度，并返回概要和得分。

    Args:
        jd (str): 职位描述,职位要求
        resume (str): 候选人简历。
        options (dict): 分析选项，例如过滤条件或其他设置。

    Returns:
        DataFrame: 包含简历综合概要和匹配得分的 DataFrame。
    """

    # 进行简历分析
    df = analyze_str(resume, options)

    # 进行数据处理：如果数据类型为列表，则将转换为以逗号分割的字符串；否则不变
    df_string = df.applymap(lambda x: ', '.join(x) if isinstance(x, list) else x).to_string(index=False)
    st.write("OpenAI综合分析..")

    # 构造一个概要问题字符串，内容包括职位要求和简历概要。然后调用 ask_openAI 函数向 OpenAI 请求概要信息。
    summary_question = f"职位要求是：{{{jd}}}" + f"简历概要是：{{{df_string}}}" + "，请直接返回该应聘岗位候选人匹配度概要（控制在200字以内）;'"
    summary = ask_openAI(summary_question)

    # 将概要信息添加到 df DataFrame 中
    df.loc[len(df)] = ['综合概要', summary]

    # 设置额外的打分要求说明
    extra_info = "打分要求：国内top10大学+3分，985大学+2分，211大学+1分，头部企业经历+2分，知名企业+1分，海外背景+3分，外企背景+1分。 "

    # 构建一个评分问题字符串，内容包括职位要求、简历概要以及打分要求说明。然后调用 ask_openAI 函数向OpenAI请求候选人的匹配分数
    score_question = f"职位要求是：{{{jd}}}" + f"简历概要是：{{{df.to_string(index=False)}}}" + \
                     "，请直接返回该应聘岗位候选人的匹配分数（0-100），请精确打分以方便其他候选人对比排序，'" + extra_info
    score = ask_openAI(score_question)

    # 将匹配得分添加到 df DataFrame 中
    df.loc[len(df)] = ['匹配得分', score]
    return df

def ask_openAI(question):
    # 使用OpenAI API获取答案
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=400,
        n=1,
        stop=None,
        temperature=0,
    )
    return response.choices[0].text.strip()

def analyze_str(resume, options):
    # 创建一个文本切割器对象
    text_splitter = CharacterTextSplitter(
        separator="\n",         # 换行符
        chunk_size=600,         # 块大小
        chunk_overlap=100,      # 块重叠
        length_function=len     # 长度
    )
    chunks = text_splitter.split_text(resume)

    embeddings = OpenAIEmbeddings(openai_api_key=my_key)
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    df_data = [{'option': option, 'value': []} for option in options]
    st.write("信息抓取")

    # 创建进度条和空元素
    progress_bar = st.progress(0)
    option_status = st.empty()

    for i, option in tqdm(enumerate(options), desc="信息抓取中", unit="选项", ncols=100):
        question = f"这个应聘者的{option}是什么，请精简返回答案，最多不超过250字，如果查找不到，则返回'未提供'"
        docs = knowledge_base.similarity_search(question)

        # 创建OpenAI对象
        llm = OpenAI(openai_api_key=my_key, temperature=0.3, model_name="text-davinci-003", max_tokens="2000")
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=docs, question=question )
        df_data[i]['value'] = response
        option_status.text(f"正在查找信息：{option}")

        # 更新进度条
        progress = (i + 1) / len(options)
        progress_bar.progress(progress)

    df = pd.DataFrame(df_data)
    st.success("简历要素已获取")
    return df

# 设置页面标题
st.title("🚀 GPT招聘分析机器人")
st.subheader("🪢 Langchain + 🎁 OpenAI")

# 设置默认的JD和简历信息
default_jd = "业务数据分析师JD 岗位职责：..."
default_resume = "应聘简历 个人信息：..."

# 输入JD信息
jd_text = st.text_area("【岗位信息】", height=100, value=default_jd)

# 输入简历信息
resume_text = st.text_area("【应聘简历】", height=100, value=default_resume)

# 参数输入
options = ["姓名", "联系号码", "性别", "年龄", "工作年数（数字）", "最高学历", "本科学校名称", "硕士学校名称", "是否在职", "当前职务", "历史任职公司列表", "技术能力", "经验程度", "管理能力"]
selected_options = st.multiselect("请选择选项", options, default=options)

# 分析按钮
if st.button("开始分析"):
    df = analyze_resume(jd_text, resume_text, selected_options)
    st.subheader("综合匹配得分："+ df.loc[df['option'] == '匹配得分', 'value'].values[0])
    st.subheader("细项展示：")
    st.table(df)