from MainApp import Mainapp

def main():
    print("""
            IMAGE BATCH PROCESSOR
    PLESE SELECT THE FOLDER CONTAINING YOUR IMAGES
          """)
    select_folder = input("Select folder\n")
    user = Mainapp(select_folder)
    user.run()


if __name__=="__main__":
    main()