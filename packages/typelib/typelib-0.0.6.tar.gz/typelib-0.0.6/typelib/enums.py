
import core
import utils

def EnumType(enum_data = None, annotations = None, docs = None):
    out = core.Type("enum", None, annotations = annotations, docs = docs)
    out.type_data = enum_data or EnumData()
    return out

class EnumData(object):
    class Symbol(object):
        def __init__(self, name, annotations = [], doc = ""):
            self.name = name
            self.annotations = annotations
            self.doc = doc
 
        def to_json(self):
            return self.name
 
    def __init__(self, *symbols):
        self.fqn = None
        self.symbols = list(*symbols)
        self.source_types = []
        self.annotations = []

    @property
    def name(self):
        return utils.normalize_name_and_ns(self.fqn, "")[0]

    @property
    def namespace(self):
        return utils.normalize_name_and_ns(self.fqn, "")[1]
 
    def signature(self, thetype):
        return "Enum<%s>" % thetype.fqn
    
    def add_symbol(self, name, annotations = [], doc = ""):
        self.symbols.append(EnumData.Symbol(name, annotations, doc))
 
    def __str__(self):
        return "[%s: %s]" % (self.fqn, ",".join([s.name for s in self.symbols]))
 
    def to_json(self, thetype, visited = None):
        out = {
            "type": "enum",
            "doc": thetype.documentation, 
            "symbols": [s.to_json() if type(s) not in (str,unicode) else s for s in self.symbols]
        }
 
        if thetype.name:
            out["name"] = thetype.fqn
        return out

