class Movement:
    '''
    default class for movement in pong
    '''
    def execute():
        '''
        This method purpose is to be overriden by collision and paddles classes
        '''
        raise NotImplementedError("execute not implemented in base class")