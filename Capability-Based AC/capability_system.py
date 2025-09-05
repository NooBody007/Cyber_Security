
class Subject:
    def __init__(self, name: str):
        self.name = name
        self.capabilities: list[Capability] = []

    def get_cap(self, obj):
        for cap in self.capabilities:
            if cap.obj == obj:
                return cap
        return None

class Object:
    def __init__(self, name: str):
        self.name = name
        self.owners: list[Subject] = []

class Capability:
    def __init__(self, obj, rights: list[str]):
        self.obj = obj
        self.rights = rights  

    def has_right(self, right: str):
        return right in self.rights


def add_capability(grt: Subject, trg: Subject, obj: Object, rights: list[str]):
    grt_cap = grt.get_cap(obj)
    if ((not grt_cap) or ('own' not in grt_cap.rights)):
        raise PermissionError(f"{grt.name} does not have 'own' permission on {obj.name}")

    trg_cap = trg.get_cap(obj)
    if trg_cap:
        for right in rights:
            if right not in trg_cap.rights:
                trg_cap.rights.append(right)
    else:
        trg.capabilities.append(Capability(obj, rights.copy()))

    if ('own' in rights) and (trg not in obj.owners):
        obj.owners.append(trg)

def remove_capability(grt: Subject, trg: Subject, obj: Object, right: str):
    grt_cap = grt.get_cap(obj)
    if not grt_cap or 'own' not in grt_cap.rights:
        raise PermissionError(f"{grt.name} does not have 'own' permission on {obj.name}")

    trg_cap = trg.get_cap(obj)
    if trg_cap is None:
        return 

    if right in trg_cap.rights:
        trg_cap.rights.remove(right)

    if right == 'own' and trg in obj.owners:
        obj.owners.remove(trg)

    
    if not trg_cap.rights:
        trg.capabilities.remove(trg_cap)


def check_access(subject: Subject, obj: Object, right: str):
    cap = subject.get_cap(obj)

    return cap is not None and cap.has_right(right)


def get_owners(obj: Object):
    owner_names = [] 

    for owner in obj.owners:  
        owner_names.append(owner.name)  

    return owner_names  
