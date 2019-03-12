class StaticDataRetriever:

    def __init__(self):
        self.__data_frame = None

    @property
    def data_frame(self):
        return self.__data_frame

    def csv_to_json(self):
        in_file_path = Path(self.__csv)
        if in_file_path.is_file():
            self.__data_frame = pd.read_csv(self.__csv, sep=',', header=None)
            return self.__data_frame.to_json(self.__json)
        else:
            return 'Error Code: Invalid file path'  # TODO: Create error code system
