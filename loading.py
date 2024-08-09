import os
import logging

class Directory:
    def __init__(self, parent_directory, directory):
        self.parent_directory = parent_directory
        self.directory = directory
        self.path = os.path.join(self.parent_directory, self.directory)

    def create_directory(self):
        try:
            os.mkdir(self.path)
            logging.info(f'Directory {self.path} created')
        except FileExistsError:
            logging.info(f'Directory {self.path} already exists')
        except Exception as e:
            logging.error(f'An unexpected error occured during directory creation: {e}')


