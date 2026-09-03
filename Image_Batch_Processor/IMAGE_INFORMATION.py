
from PIL import Image
class ImageInfo:
    @staticmethod
    def get_image_info(image):
        try:
          print(f"""
    
Image Information

File name : {image.filename}
Format    : {image.format}
Size      : {image.size}
Mode      : {image.mode}
Width     : {image.width}
Height    : {image.height}
""")
        except Exception as e:
            print("Not able to get the file info")
            print("Error: " , e)









