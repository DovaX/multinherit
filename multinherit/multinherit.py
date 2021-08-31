def find_parent_classes_recursively(cls):
    """Finds all parent classes recursively with any inheritance structure and omits duplicates"""
    all_parent_classes=[]
    base_classes=cls.__bases__
    for base_class in base_classes:
        if base_class not in all_parent_classes:
            all_parent_classes.append(base_class)
            new_parent_classes=find_parent_classes_recursively(base_class)
            all_parent_classes+=new_parent_classes
    all_parent_classes=list(set(all_parent_classes))
    return(all_parent_classes)

        
def initialize_if_not_initialized_yet(cls,instance,**kw): 
    """Initialize and stores initialized parent classes for each individual instance"""
    if cls not in instance._classes_initialized:
        instance._classes_initialized.append(cls)
        cls.__init__(instance,**kw)
   
    
def multi_super(cls,instance,**kw):
    """Performs super() command with any inheritance structure without calling any parent classes twice"""  
    if not hasattr(instance,"_classes_initialized"):
        instance._classes_initialized=[]
    initialize_if_not_initialized_yet(cls,instance,**kw)