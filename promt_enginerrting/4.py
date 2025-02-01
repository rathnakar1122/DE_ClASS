# advanced promet engineering.

def create_stepwise_prompt(context):
    # Step 1: Summarize the context
    step1_prompt = f"Summarize this text: {context}"

    # AI summary (this would ideally be generated dynamically based on the context)
    ai_summary = "This is a summary of the context."

    # Step 2: Based on the summary, answer the following questions
    step2_prompt = f"Based on the summary: '{ai_summary}', answer the following questions: {context}"

    return step1_prompt, step2_prompt

context = " Gen ai is growing reapidyl in tech industry "
step1,step2 = create_stepwise_prompt()
