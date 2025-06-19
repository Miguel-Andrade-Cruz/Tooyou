from Interfaces.RequisiteInterface import RequisiteInterface



class RequisiteDecorator(RequisiteInterface):
    
    def __init__(self, wrapped: RequisiteInterface, items:list[str]):
        self.items:list[str] = items
        self.wrapped:RequisiteInterface = wrapped
    
    def prepare(self) -> tuple[str, dict | list[str]]:
        
        return self.wrapped.prepare()
        
    
