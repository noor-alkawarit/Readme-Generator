from generator.prompts import UserPrompts
from generator.readme_builder import ReadmeBuilder

def main():
    print("🚀 Welcome to the Python README Generator!")
    responses = UserPrompts().get_responses()
    builder = ReadmeBuilder(responses)
    builder.save_to_file()

if __name__ == "__main__":
    main()
