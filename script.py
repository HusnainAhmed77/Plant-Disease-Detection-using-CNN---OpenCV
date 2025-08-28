import os, shutil, random
from pathlib import Path

# Paths
DATA_DIR = Path("clean_data")
SPLIT_DIR = Path("split_data")

# Split ratios
train_ratio, val_ratio = 0.7, 0.15  # 70% train, 15% val, 15% test

# Create split folders
for split in ["train", "val", "test"]:
    (SPLIT_DIR / split).mkdir(parents=True, exist_ok=True)

# Loop through classes
for class_folder in DATA_DIR.iterdir():
    if class_folder.is_dir():
        files = list(class_folder.glob("*.jpg"))
        random.shuffle(files)

        n_total = len(files)
        n_train = int(train_ratio * n_total)
        n_val = int(val_ratio * n_total)

        # Split the dataset
        train_files = files[:n_train]
        val_files = files[n_train:n_train+n_val]
        test_files = files[n_train+n_val:]

        # Copy files to new folders
        for split, split_files in zip(["train", "val", "test"], [train_files, val_files, test_files]):
            split_class_dir = SPLIT_DIR / split / class_folder.name
            split_class_dir.mkdir(parents=True, exist_ok=True)
            for f in split_files:
                shutil.copy(f, split_class_dir / f.name)

        print(f"{class_folder.name}: {n_total} → "
              f"{len(train_files)} train, {len(val_files)} val, {len(test_files)} test")
