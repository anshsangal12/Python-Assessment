import os
from PIL import Image
from ImageProcessor import ImagProcessor

class BatchProcessor:
    def process_images(self , files , functionality , value):
        successfull = 0
        failed = 0
        for file in files:
            try:
                image = Image.open(file)
                print("processing: " , file)
                if functionality=="resize":
                    print("BEFORE: " , image.size)
                    new_image = ImagProcessor.resize_image(image   , value)
                    print("AFTER: " , new_image.size)
                    output_path = self.save_image(new_image , file , "resize")
                    
                elif functionality=="rotate":
                    new_image = ImagProcessor.rotate_image(image  , value , True)
                    
                    output_path = self.save_image(new_image , file , "rotate")
                    
                elif functionality=="crop":
                    new_image = ImagProcessor.crop_image(image , value)
                    output_path  = self.save_image(new_image , file , "crop")
                    
                elif functionality=="convert":
                    file_name = os.path.basename(file)
                    name = os.path.splitext(file_name)[0]
                    output_path = os.path.join("output", name + "_converted." + value.lower())
                    
                    ImagProcessor.convert_image(image , output_path , value)
                    
                else:
                    print("this is functionality is not available")
                    image.close()
                    continue

                successfull= successfull+1
                image.close()
            except Exception as error:
                print("UNABLE TO PROCESS" , file)
                print("Error:" , error)
                failed = failed+1
            
            
        self.generate_summary(successfull , failed)
            
          
          
          
    def save_image(self , image , file , functionality):
        if not os.path.exists("output"):
            os.mkdir("output")
        file_name = os.path.basename(file)
        output_path = os.path.join("output" , functionality+"_"+file_name)
        image.save(output_path)
        return output_path
    
    
    def generate_summary(self , successfull , failed):
        print("\n")
        print("Files successfully added in the output directory: " , successfull)
        print("files failed during the processing:" , failed)
        
        
            