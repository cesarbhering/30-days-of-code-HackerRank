class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        list = []
        return list


class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        list = [2, 1, 3]
        return list

    @staticmethod
    def get_expected_result():
        return 1


class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        list = [2, 3, 1, 1]
        return list

    @staticmethod
    def get_expected_result():
        return 2
