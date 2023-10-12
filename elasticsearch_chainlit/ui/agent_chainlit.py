import chainlit as cl
from elasticsearch_agent.agent.agent_factory import agent_factory2

from langchain.agents.agent import AgentExecutor
from elasticsearch_chainlit.log_init import logger

KEY_AGENT = "agent"
KEY_USER_QUESTIONS = "user_questions"

@cl.on_chat_start
async def on_chat_start():
    agent = agent_factory2()
    cl.user_session.set(KEY_AGENT, agent)
    cl.user_session.set(KEY_USER_QUESTIONS, "")
    await cl.Message(content="Agent started").send()


@cl.on_message
async def main(question):
    agent: AgentExecutor = cl.user_session.get(KEY_AGENT)
    cb = cl.AsyncLangchainCallbackHandler()
    user_questions = cl.user_session.get(KEY_USER_QUESTIONS)
    message = f"""
Make sure that you query first the indices in the ElasticSearch database.
Make sure that after querying the indices you query the field names.

Here are some previous questions to give you some context:
```
{user_questions}
```

Then answer this question:
{question}
"""
    logger.info(message)
    response = await cl.make_async(agent.run)(message, callbacks=[cb])
    await cl.Message(content=response).send()
    cl.user_session.set(KEY_USER_QUESTIONS, f"{user_questions}\n{question}")