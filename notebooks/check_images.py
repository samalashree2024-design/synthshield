from PIL import Image
import os
DATASET_PATH = "../processed_dataset"
bad_images = []
for split in os.listdir(DATASET_PATH):
    split_path = os.path.join(DATASET_PATH, split)
    for label in os.listdir(split_path):
        label_path = os.path.join(split_path, label)
        for file in os.listdir(label_path):
            image_path = os.path.join(
                label_path,
                file
            )
            try:
                img = Image.open(image_path)
                img.verify()
            except Exception as e:
                print("CORRUPT:", image_path)
                bad_images.append(image_path)
print("\nTOTAL CORRUPT IMAGES:", len(bad_images))