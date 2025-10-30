from InquirerPy import inquirer

class UserPrompts:
    def __init__(self):
        self.questions = [
            ("title", "Project Title:"),
            ("description", "Project Description:"),
            ("installation", "Installation Instructions:"),
            ("usage", "Usage Information:"),
            ("license", "Select a license:", ["MIT", "Apache 2.0", "GPL 3.0", "BSD 3", "None"]),
            ("author", "Author Name:"),
            ("contact", "Contact Information (email or GitHub):"),
        ]

    def get_responses(self):
        responses = {}
        for q in self.questions:
            if len(q) == 3:
                responses[q[0]] = inquirer.select(message=q[1], choices=q[2]).execute()
            else:
                responses[q[0]] = inquirer.text(message=q[1]).execute()
        return responses
