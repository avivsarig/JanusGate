from list_files import list_added_files, list_modified_files
from diff_prompt import diff_to_str
from chat import generate_text

commit_message = ""

added_files = list_added_files()

if added_files != [""]:
    commit_message += "Added files:\n"

    for file in added_files:
        if "__init__.py" in file:
            continue
        with open(file, "r") as f:
            file_contents = f.read()

        prompt = f"In one short sentence, without specifics - what is the main function of this file?\n\n{file_contents}"
        commit_message += f"{file}:\n{generate_text(prompt,30)}\n\n"

modified_files = list_modified_files()

if modified_files != [""]:
    commit_message += "Modified files:\n\n"

    for file in modified_files:
        changes = diff_to_str(file)
        prompt = f"As consicely as possible, without specifics - What was changed in this code?\n\n{changes}"
        commit_message += f"{file}:\n{generate_text(prompt,60)}\n\n"

if commit_message == "":
    print("No changes were made")
else:
    print("Suggested Commit Message:\n" + commit_message)
