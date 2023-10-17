from typing import List

import chainlit as cl
from elasticsearch_agent.agent.agent_factory import agent_factory

from langchain.agents.agent import AgentExecutor
from elasticsearch_chainlit.log_init import logger
from elasticsearch_chainlit.config import cfg

KEY_AGENT = "agent"
KEY_USER_QUESTIONS = "user_questions"

@cl.on_chat_start
async def on_chat_start():
    agent = agent_factory()
    cl.user_session.set(KEY_AGENT, agent)
    cl.user_session.set(KEY_USER_QUESTIONS, [])
    await cl.Message(content="ElasticSearch Agent started. Please check the README section to see how the agent can be used.").send()


@cl.on_message
async def main(question):
    agent: AgentExecutor = cl.user_session.get(KEY_AGENT)
    cb = cl.AsyncLangchainCallbackHandler()
    user_questions: List = cl.user_session.get(KEY_USER_QUESTIONS)
    user_questions = user_questions[-cfg.questions_to_keep:] # Just keep the latet questions
    joined_questions = '\n'.join(user_questions)

    memory_questions = f"""
Here are some previous questions that you do not need to answer but consider in relationship to the actual question:
```
{joined_questions}
```
""" if len(joined_questions) else ""

    message = f"""
Make sure that you query first the indices in the ElasticSearch database.
Make sure that after querying the indices you query the field names.

{memory_questions}

Then answer this question:
{question}
"""
    logger.info(message)
    logger.info(f"Memory size: {len(joined_questions)}")
    response = await cl.make_async(agent.run)(message, callbacks=[cb])
    await cl.Message(content=response).send()
    user_questions.append(question)
    cl.user_session.set(KEY_USER_QUESTIONS, user_questions)