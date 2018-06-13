
def class_to_dict(obj):
    dic = {}
    dic.update(obj.__dict__)
    if "_sa_instance_state" in dic:
        print dic['_sa_instance_state']
        del dic['_sa_instance_state']
    return dic
