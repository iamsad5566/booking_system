class BookingProcedure:
    '''
    ## An interface defining booking procedure
    - SelectDateAndTime: 
    '''
    def __init__(self):
        pass
    def selectDateAndTime(self):
        raise NotImplementedError
    
    def keyInPersonalInformation(self):
        raise NotImplementedError
    
    def creditCardInformation(self):
        "If necessary"
        raise NotImplementedError
    
    def clickBooking(self):
        raise NotImplementedError