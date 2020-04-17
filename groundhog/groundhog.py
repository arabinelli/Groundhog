import functools

class Groundhog():

    def __init__(self,app_name):
        self.app_name = app_name
        self.connectors = []

    def watch(self, func):
        """Defines the decorator"""
        functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except BaseException as e:
                self._call_out(func,e,*args,**kwargs)
                raise e
        return wrapper
    
    def _call_out(self,func,e,*args,**kwargs):
        for connector in self.connectors:
            connector.notify(self.app_name,func,e,args,kwargs)
    
    def register_connector(self,Connector,*connector_args,**connector_kwargs):
        """
        Registers a new connector.

        ARGUMENTS:
        Connector (class): A connector is a python class with a notify method 
                           taking as arguments: monitored_app_name, func, error, 
                           func_args and func_kwargs
        *connector_args: any arguments needed to initialize the connector
        **connector_kwargs: any keyword arguments needed to initialize the connector
        """
        connector_instance = Connector(*connector_args,**connector_kwargs)
        self.connectors.append(connector_instance)