import os
import shutil 
import random
REAL_SOURCE = "../dataset/REAL/real_dataset"
FAKE_SOURCE = "../dataset/FAKE/Ai_generated_dataset"
OUTPUT = "../processed_dataset"
SPLITS = {
    "train": 0.7,
    "val": 0.15,
    "test": 0.15
} 
def collect_images(source_root):
    image_paths = []
    for category in os.listdir(source_root):
        category_path = os.path.join(source_root, category)
        if os.path.isdir(category_path):
            for file in os.listdir(category_path):
                full_path = os.path.join(category_path, file)
                image_paths.append(
                    (category, full_path)
                )           
    return image_paths
real_images = collect_images(REAL_SOURCE)
fake_images = collect_images(FAKE_SOURCE)
random.shuffle(real_images)
random.shuffle(fake_images)
def split_data(images):
    total = len(images)
    train_end = int(total * 0.7)
    val_end = int(total * 0.85)
    return {
        "train": images[:train_end],
        "val": images[train_end:val_end],
        "test": images[val_end:]
    }
real_split = split_data(real_images)
fake_split = split_data(fake_images)
def save_split(split_data_dict, label):
    for split_name, images in split_data_dict.items():
        output_folder = os.path.join(
            OUTPUT,
            split_name,
            label
        )
        os.makedirs(output_folder, exist_ok=True)
        for idx, (category, image_path) in enumerate(images):
            ext = os.path.splitext(image_path)[1]
            new_name = f"{category}_{idx}{ext}"
            dst = os.path.join(
                output_folder,
                new_name
            )
            shutil.copy(image_path, dst)
save_split(real_split, "real")
save_split(fake_split, "fake")
print("DATASET PREPARED SUCCESSFULLY")