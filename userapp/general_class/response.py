class ResponseGeneral():
    def __init__(self):
        self.__response = {"status":"","data":{}}
        
    def get_response(self):
        return self.__response
    
    def set_status(self,status):
        self.__response["status"] = status;
    
    def set_data(self,data):
        self.__data["data"] = data
        
    def set_data_and_status(self,data,status):
        self.__response["status"] = status
        self.__response["data"] = data
        return self.__response