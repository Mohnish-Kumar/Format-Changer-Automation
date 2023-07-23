import os

def convert_extension(old_ext, new_ext):
    for filename in os.listdir('.'):
        if filename.endswith(old_ext):
            base_name = os.path.splitext(filename)[0]
            new_name = f"{base_name}.{new_ext}"
            os.rename(filename, new_name)

if __name__ == "__main__":
    old_extension = input("Enter the old extension to convert (e.g., mp4): ").strip().lower()
    new_extension = input("Enter the new extension (e.g., txt): ").strip().lower()

    convert_extension(old_extension, new_extension)
