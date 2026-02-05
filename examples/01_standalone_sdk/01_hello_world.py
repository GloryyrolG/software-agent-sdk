import os
from dotenv import load_dotenv

# load_dotenv(".env")

from openhands.sdk import LLM, Agent, Conversation, Tool
from openhands.tools.file_editor import FileEditorTool
from openhands.tools.task_tracker import TaskTrackerTool
from openhands.tools.terminal import TerminalTool


llm = LLM(
    # model=os.getenv("LLM_MODEL", "anthropic/claude-sonnet-4-5-20250929"),
    # api_key=os.getenv("LLM_API_KEY"),
    # base_url=os.getenv("LLM_BASE_URL", None),

    # model="openai/endor-text-mixtral-8x22b-20250309",
    # base_url="http://localhost:8881/llm/endor-text-mixtral-8x22b-20250309/v1",
    # base_url="http://xinyu-tu-default.siri-interactive-vm.svc.kube.us-west-3b.k8s.cloud.apple.com:8881/llm/endor-text-mixtral-8x22b-20250309/v1",

	# x
    # model="openai/anthropic-claude-opus-4-1-20250805-v1:0",  # :0
    # base_url="http://xinyu-tu-default.siri-interactive-vm.svc.kube.us-west-3b.k8s.cloud.apple.com:8881/llm/anthropic-claude-opus-4-1-20250805-v1:0/v1",

    # model="openai/endor-text-qwen3-235b-latest",
    # base_url="http://xinyu-tu-default.siri-interactive-vm.svc.kube.us-west-3b.k8s.cloud.apple.com:8881/llm/endor-text-qwen3-235b-latest/v1",
    # base_url="http://172.25.110.167:8881/llm/endor-text-qwen3-235b-latest/v1",
    # base_url="http://localhost:8881/llm/endor-text-qwen3-235b-latest/v1",

    # model="openai/gemini-2.5-pro",
    # base_url="http://17.87.107.226:8881/llm/gemini-2.5-pro/v1",

    # api_key="any",

    model="openai/gpt-5-2025-08-07",
    api_key=input("Please enter your OpenAI API key: "),

    # reasoning_effort="high",
)

agent = Agent(
    llm=llm,
    tools=[
        Tool(name=TerminalTool.name),
        Tool(name=FileEditorTool.name),
        Tool(name=TaskTrackerTool.name),
    ],
)

cwd = os.getcwd()
conversation = Conversation(agent=agent, workspace=cwd)

conversation.send_message("Write 3 facts about the current project into FACTS.txt.")
conversation.run()
exit(0)

prompt = "What llm model are you using? Please give its specific version and trained by which company. "
# prompt += "然后 请你帮我构建一个app，要求是：经销商上传表格信息，AI自动化处理汇总后，将结果在前端展示出来"
prompt += """
# Role
你是一位经验丰富的全栈架构师（擅长Python/FastAPI + React/Next.js）和资深UI/UX设计师（擅长Apple HIG设计规范）。

# Task
请基于以下用户需求，构建一个**生产级（Production-Ready）**的Web应用原型。
拒绝任何形式的Mock数据或"Coming Soon"占位符，必须实现真实的数据处理逻辑。

## 1. 用户核心需求
请你帮我构建一个app，要求是：用户上传问卷调查结果，AI总结后给出结论，并在前端展示

## 2. 核心技术栈 (非强制，只要能高水平交付满足用户需求的app就行)
* **前端:** React + Tailwind CSS + Lucide React (图标)。
* **UI组件库:** 使用 **Shadcn UI** 的设计理念（无需安装包，直接生成组件代码）。
* **后端:** FastAPI (Python) - 适合处理数据分析和AI任务。
* **数据交互:** 使用 Axios 或 Fetch 进行前后端真实通信。

## 3. UI/UX 设计规范 (Apple Style)
* **布局风格:** 严格遵循 **"Bento Grid" (便当盒风格)** 布局。使用卡片式设计将信息模块化。
* **视觉质感:** 界面必须"Clean & Minimalist"。使用大量的留白，**圆角设置为 `rounded-2xl` 或 `rounded-3xl`**。
* **配色:** 使用中性色（白色/浅灰）作为背景，配合一个高质感的主色调（如Apple Blue或Midnight Green）。
* **交互:** 必须包含 Loading 状态（骨架屏 Skeleton）、上传进度条和错误提示 Toast。

## 4. 后端与AI能力集成规范
* **API设计:** 设计高水平RESTful API。
* **真实逻辑:** * 后端必须真实解析用户上传的数据（如CSV/Excel/JSON）。
    * 不要写 `return "fake result"`。或是简单统计字符个数等。请编写具体的数据预处理代码（使用Pandas等或是基于AI能力）。
* **AI能力集成:** * 在后端逻辑中，你需要集成AI分析能力。
    * 请参考我提供的这段 **[AI能力调用示例代码]** 来编写后端的Service层：
    '''
     from openai import OpenAI

client = OpenAI(
    api_key="sk-aal58s2gWETYNHTiD49904329c7942C7Ac8dC70625041265",
    base_url="https://ai-yyds.com/v1"
)
# 创建一个请求来获取回应
prompt = "你是谁"
completion = client.chat.completions.create(
    model="gemini-3-pro-preview",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)
result = completion.choices[0].message.content
print(result)
    '''
"""
conversation.send_message(prompt)
conversation.run()
print("All done!")
