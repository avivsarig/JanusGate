from diff_prompt import diff_to_str
from chat import generate_text

diff = diff_to_str()
prompt = f"Return commit message for this git diff, without any other text:\n\n{diff}"
commit_message = generate_text(prompt)
print(commit_message)
