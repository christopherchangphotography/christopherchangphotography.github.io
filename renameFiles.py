
# Pythono3 code to rename multiple
import os
# files in a directory or folder
 
# importing os module
def main():
    print(os.getcwd())

    for filename in os.listdir("images/fulls"):
        x = filename.replace(' ', '').replace("Medium", "").replace("Large","").replace("jpeg", "jpg")
        print(x)
        os.rename("images/fulls/" + filename, "images/fulls/" + x)
        
    for filename in os.listdir("images/thumbs"):
        x = filename.replace(' ', '').replace("Medium", "").replace("Large","").replace("jpeg", "jpg")
        print(x)
        os.rename("images/thumbs/" + filename,"images/thumbs/" + x)

# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()