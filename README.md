# **Extraction of frames:**

To extract frames from a given video/stream and save the frames in the specified folder

## **Usage:**

**1.For input video**

  python extract_frames.py --input path_to_video --output folder_to save_frames 

**2.For webcam feed**

python extract_frames.py --output folder_to_save_frames  

(Note:Output frames are with png extention)



# **Reversing a video:**

To reverse a given video and save in the name as specified by the user

## **Usage:**

python extract_frames.py --input path_to_video --output output_file_name_without_any_extension

(Note:The output video will be in mp4 format)


# **Creating video from frames:**

Inorder to create a video from frames stored in a folder use "create_video_from_frames.py" file.This code can take up image frames with jpg,png and jpeg extensions and create a video.

## **Usage:**

python create_video_from_frames.py --input folder_name --fps required_fps_video --width 800 --height 800 --output output_video_file_name
