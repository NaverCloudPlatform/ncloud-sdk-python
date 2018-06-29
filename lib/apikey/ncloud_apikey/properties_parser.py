# coding: utf-8

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

#print(PropertiesParser().parse("/Users/user/.ncloud/configure"))
