# coding: utf-8

import os

class NcloudKey :

    ACCESS_KEY = ''
    SECRET_KEY = ''

    def __init__(self, args={}) :
        if 'access_key' in args :
            NcloudKey.ACCESS_KEY = args['access_key']
        if 'secret_key' in args :
            NcloudKey.SECRET_KEY = args['secret_key']

    def get_configure_filepath(self) :
        return os.path.join(
            os.path.expanduser('~'),
            '.ncloud',
            'configure')

    def read_configure_file(self) :
        configure_filepath = self.get_configure_filepath()

        if not os.path.exists(configure_filepath) :
            print('Please check configure file (linux : $HOME/.ncloud/configure, Windows : %HOME%\.ncloud\configure)')

        pp = PropertiesParser()
        prop_list = pp.parse(configure_filepath)

        return prop_list

    def keys(self) :
        if NcloudKey.ACCESS_KEY != '' and NcloudKey.SECRET_KEY != '' :
            return {
                "access_key": NcloudKey.ACCESS_KEY,
                "secret_key": NcloudKey.SECRET_KEY
            };

        prop_list = self.read_configure_file()

        prop_dict = {}
        for k, v in prop_list :
            prop_dict[k] = v

        NcloudKey.ACCESS_KEY = prop_dict['ncloud_access_key_id']
        NcloudKey.SECRET_KEY = prop_dict['ncloud_secret_access_key']

        return {
            "access_key": NcloudKey.ACCESS_KEY,
            "secret_key": NcloudKey.SECRET_KEY
        };


class PropertiesParser(object):

    def parse(self, filepath):
        with open(filepath, 'r') as f:
            lines = f.readlines()

            prop_list = []
            for line in lines:
                if line == '' or len(line) < 3 or line[0] == "#" :
                    continue

                split_str = line.strip().split('=')

                if len(split_str) < 2 :
                    continue

                prop_list.append((split_str[0].strip(), split_str[1].strip()))

        return prop_list


# print(NcloudKey().keys())
# print(NcloudKey({'access_key':'abc', 'secret_key':'def'}).keys())

# print(PropertiesParser().parse("/Users/user/.ncloud/configure"))

