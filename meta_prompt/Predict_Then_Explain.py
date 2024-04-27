pte_prompt = """
Original Post(OP)'s title: {title}
Original Post(OP)'s text: {text}
Argument: {argument}

Explanation: Based on the context and the argument presented, explain why this argument could or could not be considered as having successfully changed the main view expressed by the OP.

Prediction: After providing your explanation, predict whether the argument has successfully changed the OP's view. Respond with 'positive' if it has and 'negative' if it has not.

Based on the above information, please give me your answer following these guidelines:
1. You should provide your prediction before you respond with the explanation.
2. Your prediction should be explicitly stated as 'positive' or 'negative'.

The response is:""".strip()