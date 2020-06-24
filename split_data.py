import os
import shutil
import random
 
src_dir = "C:/Users/M.Plaban/Downloads/Compressed/observations-master/observations-master/experiements/data"
dest_dir=os.path.join(src_dir,"split_data")

withmask_dir=os.path.join(src_dir,"with_mask")
nomask_dir=os.path.join(src_dir,"without_mask")
train_foldir=os.path.join(dest_dir,"train")
val_foldir=os.path.join(dest_dir,"val")
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
split =0.2
nomask_split=int(total_nomask_images*split)

if os.path.exists(mask_train_dir):
    shutil.rmtree(mask_train_dir)
if not os.path.exists(mask_train_dir):
    os.mkdir(mask_train_dir)
for i in range(int(total_mask_images*(1-split))):
    shutil.copy(os.path.join(withmask_dir,random.choice(os.listdir(withmask_dir))),mask_train_dir)

if os.path.exists(mask_val_dir):
    shutil.rmtree(mask_val_dir)
if not os.path.exists(mask_val_dir):
    os.mkdir(mask_val_dir)
for i in range(int(total_mask_images*split)):
    shutil.copy(os.path.join(withmask_dir,random.choice(os.listdir(withmask_dir))),mask_val_dir)

if os.path.exists(nomask_train_dir):
    shutil.rmtree(nomask_train_dir)
if not os.path.exists(nomask_train_dir):
    os.mkdir(nomask_train_dir)
for i in range(int(total_mask_images*(1-split))):
    shutil.copy(os.path.join(nomask_dir,random.choice(os.listdir(nomask_dir))),nomask_train_dir)

if os.path.exists(nomask_val_dir):
    shutil.rmtree(nomask_val_dir)
if not os.path.exists(nomask_val_dir):
    os.mkdir(nomask_val_dir)
for i in range(int(total_mask_images*(split))):
    shutil.copy(os.path.join(nomask_dir,random.choice(os.listdir(nomask_dir))),nomask_val_dir)