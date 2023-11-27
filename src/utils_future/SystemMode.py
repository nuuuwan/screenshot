import os

TEST_OS_LIST = ['nt']


class SystemMode:
    @staticmethod
    def is_test():
        return os.name in TEST_OS_LIST
