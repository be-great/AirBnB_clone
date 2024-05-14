from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()

# Call reload() method on this variable to load objects\
# from the JSON file into memory
storage.reload()
