class StaticDataRetriever:

    def __init__(self, in_file=None, out_file='SDR_Default.json'):
        self.__csv = in_file
        self.__json = out_file
        self.__data_frame = None

    @property
    def csv(self):
        return self.__csv

    @csv.setter
    def csv(self, file_path):
        self.__csv = file_path

    @property
    def json(self):
        return self.__json

    @json.setter
    def json(self, file_name):
        self.__json = file_name

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
