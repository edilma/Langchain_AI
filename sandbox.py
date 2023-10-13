from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
from langchain.prompts.chat import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate
    
)

chat_model = ChatOpenAI()
print (chat_model.predict("hi"))

# I am commenting this whole block
'''
prompt = f"""Translate the text \
that is delimited by triple backticks 
into a style that is {style}.
text: ```{customer_email}```
"""
'''


system_template = """You are a helpful assistance who generates comma separated lists.
A user will pass a category, and you should  generate 5 objects in that category in a comma separated ONLY return
the comma separated list, and nothing more"""

system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template) 

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

# I copy this boilerplate code from langchain documentation
class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""

    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split(", ")

chain = LLMChain ( llm= ChatOpenAI(),
                  prompt= chat_prompt, 
                  output_parser= CommaSeparatedListOutputParser())

print (chain.run("colors"))