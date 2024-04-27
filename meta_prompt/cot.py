cot_prompt = """
Original Post(OP)'s title: {title}
Original Post(OP)'s text: {text}
Argument: {argument}

Prediction: predict whether the argument has successfully changed the OP's view. Respond with 'positive' if it has and 'negative' if it has not.

Based on the above information, please give me your answer following these guidelines:
1. Your prediction should be explicitly stated as 'positive' or 'negative'.
2. You should follow the following instruction and respond with reasoning steps.

Let's think step by step.""".strip()