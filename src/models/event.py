from dataclasses import dataclass
import datetime as dt
@dataclass
class event:
    """Class for managing real life events"""
    
    title : str
    s_date : dt.date
    e_date : dt.date
    s_time : dt.time
    e_time : dt.time

    id : int = None
    description : str = ""
    category_id : int = 0       

    def valid_title(self) -> bool:
        return len("".join(self.title.split())) > 0
    
    def valid_id(self) -> bool:
        if self.id is not None:
            return self.id > 0 
        return True
    def date_check(self) -> bool:
        return self.s_date <= self.e_date 
    def time_check(self) -> bool:
        if self.e_date == self.s_date:
            return self.s_time < self.e_time
        return True

    def __post_init__(self):
        error_msg = "Erorr: "
        errors = []
        if not self.valid_title():
            errors.append("Title can't be empty")
        if not self.valid_id():
            errors.append("Invalid id")
        if not self.date_check():
            errors.append("Finish date can't be earlier than start date")
        if not self.time_check():
            errors.append("Finish time can't be earlier than start time")
        error_msg = error_msg +  ",".join(errors)
        if errors :raise ValueError(error_msg)
            
            
