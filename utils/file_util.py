class FileUtil:
    @staticmethod
    def read_file(file_path: str) -> list[str]:
        # Read the contents of a file and return an array of strings for each line
        with open(file_path, 'r') as file:
            return file.read().strip().splitlines()