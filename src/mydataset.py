import torch.utils.data as data
import PIL as Image

class dateSet(data.dataset):
    def __init__(self, image, label, word_embeddings, attributes, transform):
        self.images = image
        self.labels = label
        self.word_embeddings= word_embeddings
        self.attributes = attributes
        self.transform = transform

    def __len__(self):
        return len(self.images)

    def __getitem__(self, item):
        sample = {
            'image': self.transform(Image.open(self.images[item]).convert('RGB'))
        }
        if self.labels is not None:
            sample['label'] = self.labels[item]
            sample['attributes'] = self.attributes[sample['label']]
            sample['word_embeddings'] = self.word_embeddings[sample['label']]
        return sample

