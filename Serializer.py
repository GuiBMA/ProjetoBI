import json

class Serializer:
    def __init__(self, file_path="interview_data.json"):
        self.file_path = file_path
        self.data = {
            "questions": [],
            "interviewees": []
        }
        # Carrega os dados do arquivo
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {
                "questions": [],
                "interviewees": []
            }

    def save_data(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def add_question(self, question):
        if question not in self.data['questions']:
            self.data['questions'].append(question)

    def add_interviewee(self, interviewee_data):
        self.data['interviewees'].append(interviewee_data)

    def serialize(self):
        self.save_data()
