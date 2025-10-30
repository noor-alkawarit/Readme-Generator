class ReadmeBuilder:
    def __init__(self, data):
        self.data = data

    def generate_content(self):
        return f"""# {self.data['title']}

## Description
{self.data['description']}

## Installation
{self.data['installation']}

## Usage
{self.data['usage']}

## License
This project is licensed under the {self.data['license']} license.

## Author
**{self.data['author']}**

## Contact
For questions or feedback, reach out at: {self.data['contact']}
"""

    def save_to_file(self, filename="README.md"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.generate_content())
        print("✅ README.md generated successfully!")
