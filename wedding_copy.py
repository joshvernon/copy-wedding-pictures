import os
import shutil
import sys
import traceback

# Control data
control_dir = 'control_files'
control_files = ['mom.txt', 'me.txt']

# Input image data
base_data_dir = os.path.expanduser(r"~\Pictures\wedding_pictures")

# Output folder
base_output_dir = r"E:\Josh_Wedding"

# Populate correct subdirectories for input image data.
file_dict = {}
for root, _, files in os.walk(base_data_dir):
    if len(files) > 1:
        file_dict[root] = files

for control_file in control_files:
    # Create the output folder if it doesn't exist.
    output_dir_name = os.path.splitext(control_file)[0]
    output_dir = os.path.join(base_output_dir, output_dir_name)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        print(f"Created output folder {output_dir}")

    # Read the control file.
    with open(os.path.join(control_dir, control_file), 'r') as input_file:
        input_image_ids = [line.rstrip() for line in input_file.readlines()]

    # Copy each image from the correct source folder.
    for image_id in input_image_ids:
        file_basename = f"DSC0{image_id}.jpg"
        for file_dir, file_list in file_dict.items():
            if file_basename in file_list:
                src_path = os.path.join(file_dir, file_basename)
                dst_path = os.path.join(output_dir, file_basename)
                if not os.path.exists(dst_path):
                    try:
                        shutil.copy2(src_path, dst_path)
                        print(f"Successfully copied {src_path} to {dst_path}")
                    except:
                        tb_info = sys.exc_info()
                        traceback.print_exception(*tb_info)
                        print(f"src: {src_path}\ndst: {dst_path}")             
            
                
