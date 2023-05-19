# import guidance

valid_answers = ['Action', 'Final Answer']
valid_tools = ['Google Search']

prompt_start_template = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Answer the following questions as best you can. You have access to the following tools:

Google Search: A wrapper around Google Search. Useful for when you need to answer questions about current events. The input is the question to search relavant information.

Strictly use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [Google Search]
Action Input: the input to the action, should be a question.
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

For examples:
Question: How old is CEO of Microsoft wife?
Thought: First, I need to find who is the CEO of Microsoft.
Action: Google Search
Action Input: Who is the CEO of Microsoft?
Observation: Satya Nadella is the CEO of Microsoft.
Thought: Now, I should find out Satya Nadella's wife.
Action: Google Search
Action Input: Who is Satya Nadella's wife?
Observation: Satya Nadella's wife's name is Anupama Nadella.
Thought: Then, I need to check Anupama Nadella's age.
Action: Google Search
Action Input: How old is Anupama Nadella?
Observation: Anupama Nadella's age is 50.
Thought: I now know the final answer.
Final Answer: Anupama Nadella is 50 years old.

### Input:
{{question}}

### Response:
Question: {{question}}
Thought: {{gen 't1' stop='\\n'}}
{{select 'answer' logprobs='logprobs' options=valid_answers}}: """

prompt_mid_template = """{{history}}{{select 'tool_name' options=valid_tools}}
Action Input: {{gen 'actInput' stop='\\n'}}
Observation: {{do_tool tool_name actInput}}
Thought: {{gen 'thought' stop='\\n'}}
{{select 'answer' logprobs='logprobs' options=valid_answers}}: """

prompt_final_template = """{{history}}{{select 'tool_name' options=valid_tools}}
Action Input: {{gen 'actInput' stop='\\n'}}
Observation: {{do_tool tool_name actInput}}
Thought: {{gen 'thought' stop='\\n'}}
{{select 'answer' options=valid_answers}}: {{gen 'fn' stop='\\n'}}"""

class CustomAgentGuidance:
    def __init__(self, guidance, tools, num_iter=3):
        self.guidance = guidance
        self.tools = tools
        self.num_iter = num_iter

    def do_tool(self, tool_name, actInput):
        return self.tools[tool_name](actInput)
    
    def __call__(self, query):
        prompt_start = self.guidance(prompt_start_template)
        result_start = prompt_start(question=query, valid_answers=valid_answers)

        result_mid = result_start
        
        for _ in range(self.num_iter - 1):
            if result_mid['answer'] == 'Final Answer':
                break
            history = result_mid.__str__()
            prompt_mid = self.guidance(prompt_mid_template)
            result_mid = prompt_mid(history=history, do_tool=self.do_tool, valid_answers=valid_answers, valid_tools=valid_tools)
        if result_mid['answer'] != 'Final Answer':
            history = result_mid.__str__()
            prompt_mid = self.guidance(prompt_final_template)
            result_final = prompt_mid(history=history, do_tool=self.do_tool, valid_answers=['Final Answer'], valid_tools=valid_tools)
        else:
            history = result_mid.__str__()
            prompt_mid = self.guidance(history + "{{gen 'fn' stop='\\n'}}")
            result_final = prompt_mid()
        return result_final