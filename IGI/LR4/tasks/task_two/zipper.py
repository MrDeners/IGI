import zipfile


class Zipper:
    @staticmethod
    def zip(file_name, zip_name):
        """
                Zip a file.

                Args:
                    file_name (str): Name of the file to be zipped.
                    zip_name (str): Name of the resulting zip file.
                """
        with zipfile.ZipFile(f"{zip_name}.zip", 'w') as zipf:
            zipf.write(f'{file_name}.txt')
