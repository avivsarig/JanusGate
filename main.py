from diff_prompt import diff_to_str
from chat import generate_text

diff: str = diff_to_str()
prompt: str = (
    f"Return commit message for this git diff, reason rather than description,without any other text:\n\n{diff}"
)

commit_messages: list = generate_text(prompt)
while len(commit_messages) < 3:
    more_messages: list = generate_text(prompt)
    for message in more_messages:
        commit_messages.add(message)

print("Possible commit messages:")
for message in commit_messages:
    print(f"- {message}")
