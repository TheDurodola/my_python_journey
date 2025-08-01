from shared_data import shared_list


class ClassA:
    def add(self, item):
        shared_list.append(item)

    def print(self):
        print(shared_list)