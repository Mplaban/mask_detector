import os
import shutil
import random
 
def split_data_create(src):
    src_dir = src
    dest_dir=os.path.join(src_dir,"split_data")

    withmask_dir=os.path.join(src_dir,"with_mask")
    nomask_dir=os.path.join(src_dir,"without_mask")
    train_foldir=os.path.join(dest_dir,"train")
    val_foldir=os.path.join(dest_dir,"val")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    if not os.path.exists(train_foldir):
        os.mkdir(train_foldir)
    if not os.path.exists(val_foldir):
        os.mkdir(val_foldir)
    mask_train_dir=os.path.join(train_foldir,"with_mask")
    mask_val_dir=os.path.join(val_foldir,"with_mask")
    nomask_train_dir=os.path.join(train_foldir,"without_mask")
    nomask_val_dir=os.path.join(val_foldir,"without_mask")

    total_mask_images=len(os.listdir(withmask_dir))
    total_nomask_images=len(os.listdir(nomask_dir))
    split =0.4
    print(total_mask_images)
    print(total_nomask_images)
    print(total_mask_images+total_nomask_images)
    print("Copying......")
    if os.path.exists(mask_train_dir):
        shutil.rmtree(mask_train_dir)
    if not os.path.exists(mask_train_dir):
        os.mkdir(mask_train_dir)
    for i in range(int(total_mask_images*split),total_mask_images,1):
        shutil.copy(os.path.join(withmask_dir,os.listdir(withmask_dir)[i]),mask_train_dir)

    if os.path.exists(mask_val_dir):
        shutil.rmtree(mask_val_dir)
    if not os.path.exists(mask_val_dir):
        os.mkdir(mask_val_dir)
    for i in range(int(total_mask_images*split)):
        shutil.copy(os.path.join(withmask_dir,os.listdir(withmask_dir)[i]),mask_val_dir)

    if os.path.exists(nomask_train_dir):
        shutil.rmtree(nomask_train_dir)
    if not os.path.exists(nomask_train_dir):
        os.mkdir(nomask_train_dir)
    for i in range(int(total_nomask_images*split),total_nomask_images,1):
        shutil.copy(os.path.join(nomask_dir,os.listdir(nomask_dir)[i]),nomask_train_dir)

    if os.path.exists(nomask_val_dir):
        shutil.rmtree(nomask_val_dir)
    if not os.path.exists(nomask_val_dir):
        os.mkdir(nomask_val_dir)
    for i in range(int(total_nomask_images*(split))):
        shutil.copy(os.path.join(nomask_dir,os.listdir(nomask_dir)[i]),nomask_val_dir)

if __name__ == "__main__":
    src="./data"
    split_data_create(src)
