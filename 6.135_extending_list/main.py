class SuperList(list):

    def __len__(self):
        return 1000


super_list = SuperList()

print(len(super_list))

super_list.append('Wes')

print(super_list[0])

print(issubclass(SuperList, list))

print(issubclass(list, object))