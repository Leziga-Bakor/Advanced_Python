class Myclass():
    def __init__(self):
        '''
        This is an implementation of private variable to ensure that the my_methon in Myclass is not over ridden 
        by my_class method in Subclass
        
        '''
        print(self.__my_method())

    def my_method(self):
        return 'This is Myclass'
    
    __my_method = my_method
    
class Subclass(Myclass):

    def my_method(self):
        return 'This is subclass'
    
my_instance = Subclass()