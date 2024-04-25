import openmesh as om
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

# Specify the directories for lrecord and vrecord files
lrecord_dir  = 'record/lrecord/'
image_dir = 'exp/images/'
vrecord_dir = 'record/vrecord/'
loutput_dir = 'landmark_results/'

# Specify the directory where the base mesh is located
base_mesh_path = 'toy_example/mean_face.obj'

# Specify the output directory for the new .obj files
voutput_dir = 'vertex_results/'

# Create the output directory if it doesn't exist
os.makedirs(loutput_dir, exist_ok=True)
os.makedirs(voutput_dir, exist_ok=True)


# Process each .npy file in the vrecord directory
for filename in os.listdir(vrecord_dir):
    if filename.endswith('.npy'):

        base_mesh = om.read_trimesh(base_mesh_path)
        # Load the vertex data from the .npy file
        vertex_data = np.load(os.path.join(vrecord_dir, filename))
        vertex_data = vertex_data.transpose()
        
        # Update the vertex positions in the mesh
        for i in range(len(vertex_data)):
            base_mesh.points()[i] = vertex_data[i, :]
        
        # Write the updated mesh to a new .obj file
        # The new file will have the same name as the .npy file but with a .obj extension
        output_filename = os.path.splitext(filename)[0] + '.obj'
        om.write_mesh(os.path.join(voutput_dir, output_filename), base_mesh)




for landmark_file in os.listdir(lrecord_dir):
    if landmark_file.endswith('.npy'):
        # The image file name matches the landmark file name but with a different extension
         # Construct the base filename by removing the '.npy' and the extraneous '_l'
        base_filename = landmark_file[:-len('.npy')]  # Removes the extension
        if base_filename.endswith('_l'):
            base_filename = base_filename[:-len('_l')]  # Removes the extraneous '_l'

        image_filename = base_filename + '.jpg'  # Adjust if your images have a different extension
        image_path = os.path.join(image_dir, image_filename)
        landmark_path = os.path.join(lrecord_dir, landmark_file)

        # Load the image and landmarks
        image = cv2.imread(image_path)
        if image is None:
            print(f"Failed to load image {image_path}. Skipping...")
            continue
        landmarks = np.load(landmark_path)

        # Draw landmarks on the image
        for (x, y) in landmarks:
            cv2.circle(image, (int(x), int(y)), 2, (0, 255, 0), -1)  # Green color for the landmarks

     
        # Save or display the image with landmarks
        # To save the image
        output_image_path = os.path.join(loutput_dir, f'landmarked_{image_filename}')
        cv2.imwrite(output_image_path, image)





