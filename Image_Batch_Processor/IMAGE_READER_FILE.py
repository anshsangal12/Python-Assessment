
import os
class ImageReader:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def get_images(self):
        images = []
        supported_formats = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

        for file in os.listdir(self.folder_path):
            if file.lower().endswith(supported_formats):
                full_path = os.path.join(self.folder_path, file)
                images.append(full_path)

        return images









