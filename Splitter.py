import os
import random
import shutil
from tqdm import tqdm

# Parameters
split_ratio = 0.8  # 80% train, 20% val
base_dir = os.getcwd()
source_folder = os.path.join(base_dir, 'garbage_classification')  # Your main folder with class folders

train_folder = os.path.join(base_dir, 'train')
val_folder = os.path.join(base_dir, 'val')

# Create output folders
for folder in [train_folder, val_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Iterate through class folders
for class_name in os.listdir(source_folder):
    class_path = os.path.join(source_folder, class_name)
    if not os.path.isdir(class_path):
        continue

    # Make class subfolders in train and val
    os.makedirs(os.path.join(train_folder, class_name), exist_ok=True)
    os.makedirs(os.path.join(val_folder, class_name), exist_ok=True)

    images = [img for img in os.listdir(class_path) if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)

    split_index = int(len(images) * split_ratio)
    train_images = images[:split_index]
    val_images = images[split_index:]

    # Move images to train
    for img in tqdm(train_images, desc=f"[Train] {class_name}"):
        src = os.path.join(class_path, img)
        dst = os.path.join(train_folder, class_name, img)
        shutil.move(src, dst)

    # Move images to val
    for img in tqdm(val_images, desc=f"[Val] {class_name}"):
        src = os.path.join(class_path, img)
        dst = os.path.join(val_folder, class_name, img)
        shutil.move(src, dst)

print("✅ Dataset successfully split into 'train' and 'val'.")
