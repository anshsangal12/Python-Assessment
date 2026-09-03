from PIL import Image


class ImagProcessor:

    @staticmethod
    def app_functionality():
        print("""
                    ------------------------
                         functionality
                    -------------------------

        resize                                      rotate
        resize your image                           rotate your image

        crop                                        imageconverter
        crop your image                             convert image format
        """)

    @staticmethod
    def rotate_image(image, angle, expand):
        rotated_image = image.rotate(angle, expand=expand)
        return rotated_image

    @staticmethod
    def resize_image(image, scale_factor):
        # new_image_size = (
        #     int(image.width * scale_factor),
        #     int(image.height * scale_factor)
        # )
        new_length = scale_factor[0]
        new_width = scale_factor[1]

        resize_image = image.resize((new_length , new_width))

        return resize_image

    @staticmethod
    def crop_image(image, box):
        cropped_image = image.crop(box)
        return cropped_image

    @staticmethod
    def convert_image(image, output_path, output_format):
        image.save(output_path, format=output_format)
   



