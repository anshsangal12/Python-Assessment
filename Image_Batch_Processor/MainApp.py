from IMAGE_READER_FILE import ImageReader
from IMAGE_INFORMATION import ImageInfo
from PIL import Image
from ImageProcessor import ImagProcessor
from BatchProcessor import BatchProcessor
from Exception_handling import Invalid_file_selector_choice , InvalidFileCountError 
from Exception_handling import InvalidFilEPositionError , InvalidFileLengthError , InvalidFileWidthError
from Exception_handling import LeftCoordinatesError , TopCoordinatesError , RightCoordinateError , BottomCoordinateError , InvalidCropCoordinatesError
from Exception_handling import InvalidFileFormat
class Mainapp:
    def __init__(self , image_dir):
        self.user_folder = image_dir
        self.files = []
        self.selected_files = []
        self.batch_processor = BatchProcessor()
    def get_data(self):
        try:
            self.get_files = ImageReader(self.user_folder)
            self.files = self.get_files.get_images()
            return self.files
        except Exception as e:
            print("UNABLE TO READ FILE")
            print("Error" , e)
            return []
    def show_data(self , files):
        for file in files:
            try:
                image = Image.open(file)
                image.show()
                image.close()
            except Exception as error:
                print("DATA IS NOT READABLE")
                print("Error" , error)
    @staticmethod
    def get_inputfile_info(files):
        for file in files:
            try:
                open_file = Image.open(file)
                ImageInfo.get_image_info(open_file)
                open_file.close()
                print("\n")
            except Exception as e:
                print("Unable to open image")
                print("Error" , e)
    
    @staticmethod
    def get_outputfile_info(files):
        for file in files:
            try:
                open_file = Image.open(file)
                ImageInfo.get_image_info(open_file)
                open_file.close()
                print("\n")
            except Exception as e:
                print("Data is not correct")
                print("Error" , e)
                
    
    
    @staticmethod
    def get_app_functionality():
        try:
            ImagProcessor.app_functionality()
        except Exception as e:
            print("Unable to ahow app functionality")
            print("Error" , e)
    
    def select_functionality(self):
        while True:
            try:
                select_option = input("ENTER FUNCTIONALITY WHICH YOU WANT TO ACCESS: ")
                select_option = select_option.lower()
                if select_option!="resize" and select_option!="rotate" and select_option!="crop" and select_option!="imageconverter":
                    raise ValueError("Sorry this functionality is not available")
            
                break
            
            except ValueError as e:
                print("Error" , e)
                
        return select_option
    
    
    def select_filess(self):
         self.selected_files = []
         print("\n")
         print("Available image")
         
         for i in range(len(self.files)):
             print(i , ":" , self.files[i])
        
         print("\n")
         
         while True:
             try:
                 choice = input("ENTER YOUR CHOICE SPECIFIC_FILES/ALL_FILES(s/a)\n")
                 
                 if choice.lower()!="s" and choice.lower()!="a":
                     raise Invalid_file_selector_choice("PLESE ENTER A VALID OPTION (s/a)")
                 
                 break
             
             
             except Exception as e:
                print("Error" , e)
                 
         if choice.lower() == "s":
                self.select_specific_files()
        
         elif choice.lower() == "a":
            self.selected_files = self.files
        
         return self.selected_files
        
            
        
    def select_specific_files(self):
        while True:
            try:
                no_of_files = int(input("Enter the no of files you want to select: "))
                
                if no_of_files>len(self.files) or no_of_files<=0:
                    raise InvalidFileCountError(f"Plese enter a valid no like between {1 , len(self.files)}")
                
                
                break
            except Exception as e:
               print("Error" , e)
                
            
        for i in range(no_of_files):
            while True:
                try:
                    file_position = int(input(f"Plese enter the {i+1} file position\n"))
                    if file_position>=len(self.files) or file_position<0:
                        raise InvalidFilEPositionError(f"PLESE ENTER A VALID NUMBER LIE BETWEEN {0 , len(self.files)-1}")
                    
                    break

                except Exception as e:
                    print("Error" , e)
                    
                
                
            file = self.files[file_position]
            self.selected_files.append(file)
                
                
   
    def resize(self):
        while True:
            try:
                new_length = int(input("PLEASE ENTER A NEW LENGTH: "))
                new_width = int(input("PLEASE ENTER A NEW WIDTH: "))

                if new_length <= 0:
                    raise InvalidFileLengthError("Length should be greater than zero")

                if new_width <= 0:
                    raise InvalidFileWidthError("Width should be greater than zero")

                break

            except Exception as e:
               print("Error:", e)

        dimension = (new_length, new_width)

        try:
            self.batch_processor.process_images(
                self.selected_files,
                "resize",
                dimension
            )
        except Exception as e:
         print("UNABLE TO RESIZE IMAGE")
         print("Error:", e)

    def rotate(self):
       while True:
         try:
            angle = int(input("PLEASE ENTER THE ANGLE VALUE: "))
            break

         except ValueError as e:
            print("PLEASE ENTER A VALID ANGLE")
            print("Error", e)
            
       try:
           self.batch_processor.process_images(
            self.selected_files,
            "rotate",
            angle
        )
       except Exception as e:
        print("UNABLE TO ROTATE IMAGE")
        print("Error", e)
        
        
    def crop(self):
        while True:
            try:
                left_coordinates = int(input("ENTER YOUR LEFT COORDINATES: "))

                top_coordinates = int(input("ENTER THE TOP COORDINATES: "))

                right_coordinates = int(input("ENTER THE RIGHT COORDINATES: "))

                bottom_coordinates = int(input("ENTER THE BOTTOM COORDINATES: "))

                if left_coordinates < 0:
                    raise LeftCoordinatesError("Left coordinate cannot be less than zero")

                if top_coordinates < 0:
                    raise TopCoordinatesError("Top coordinates cannot be less than zero")

                if right_coordinates < 0:
                    raise RightCoordinateError("Right coordinate cannot be less than zero" )

                if bottom_coordinates < 0:
                    raise BottomCoordinateError("Bottom coordinate cannot be less than zero")

                if left_coordinates >= right_coordinates or top_coordinates >= bottom_coordinates:
                    raise InvalidCropCoordinatesError("Left coordinate should be less than right coordinate" )

                
                break

            except Exception as e:
                print("Error", e)

        box = ( left_coordinates, top_coordinates, right_coordinates, bottom_coordinates)

        try:
                self.batch_processor.process_images(
                    self.selected_files,
                    "crop",
                    box
                )

        except Exception as e:
                print("UNABLE TO CROP IMAGE")
                print("Error", e)

    def image_converter(self):
        while True:
            try:
                output_format = input(
                    "Enter the format in which you want to convert your image: "
                )

                output_format = output_format.strip().lower()

                if output_format == "":
                    raise InvalidFileFormat("Output format cannot be empty")

                break

            except Exception as e:
                print("PLEASE ENTER A VALID FORMAT")
                print("Error:", e)

        try:
            self.batch_processor.process_images(
                self.selected_files,
                "convert",
                output_format
            )

        except Exception as e:
         print("UNABLE TO CONVERT IMAGE")
         print("Error:", e)
        
        
    
    def process_image(self , select_option):
        if select_option=="resize":
            self.resize()
        elif select_option=="rotate":
            self.rotate()
        elif select_option=="crop":
            self.crop()
        elif select_option=="imageconverter":
            self.image_converter()
        
    def run(self):
        self.files  =  self.get_data()
        
        if len(self.files)==0:
            print("No supported images files found")
            return
        self.selected_files = self.select_filess()
        Mainapp.get_inputfile_info(self.selected_files)
        Mainapp.get_app_functionality()
        select_option = self.select_functionality()
        self.process_image(select_option)
    
    