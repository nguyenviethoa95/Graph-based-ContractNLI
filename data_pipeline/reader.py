import json
from typing import List


class ContractNLIDataset:
    def __init__(self, filepath):
        self.data = self._load_from_file_(filepath)
        self.documents = self._parse_documents_()
        self.labels = self._parse_labels_()

    @staticmethod
    def _load_from_file_(filepath):
        with open(filepath, "rb") as f:
            data = json.load(f)
        return data

    def _parse_documents_(self):
        return self.data["documents"]

    def _parse_labels_(self):
        return self.data["labels"]

    def get_documents_by_ids(self, ids: List[int]):
        filtered_documents = []
        for doc in self.documents:
            if doc["id"] in ids:
                filtered_documents.append(doc)
        return filtered_documents

    def get_document_by_id(self, id: int):
        for doc in self.documents:
            if doc["id"] == id:
                return doc

    def get_document_text_by_id(self, id: int):
        for doc in self.documents:
            if doc["id"] == id:
                return doc["text"]

    def get_document_annotations_by_id(self, id):
        document = self.get_document_by_id(id)
        return document['annotation_sets'][0]['annotations']

    def get_document_span_by_id(self, id):
        document = self.get_document_by_id(id)
        return document['spans']

    def get_all_ids(self):
        ids = [doc['id'] for doc in self.documents]
        return ids


class CUADDataset:
    def __init__(self):
        pass

    @staticmethod
    def _load_from_file_(filepath):
        with open(filepath) as f:
            data = json.load(f)
        return data


if __name__ == "__main__":
    import os
    os.chdir(r'C:\Users\Nguyen\PycharmProjects\master_thesis')
    train_dataset = ContractNLIDataset(filepath=r"./data/contractNLI/train.json")
    all_ids = train_dataset.get_all_ids()

    for id in all_ids:
        annotations = train_dataset.get_document_annotations_by_id(id)
        spans = train_dataset.get_document_span_by_id(id)
        text = train_dataset.get_document_text_by_id(id)

        for nda_id, values in annotations.items():
            if values["choice"] != "NotMentioned" and nda_id == 'nda-2':
                evidence = []
                for span_id in values["spans"]:
                    start, end = spans[span_id]
                    evidence.append(get_span_by_start_end(text, start, end ))
                evidence = "\n".join(evidence)
                print("DocId: ", id)
                print("Hypothesis: ", nda_id)
                print(evidence)
