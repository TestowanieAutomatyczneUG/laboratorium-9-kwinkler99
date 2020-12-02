class ExternalModule():
    def api_call(self):
        pass

    def api_call_with_param(self,age):
        pass

    def some_func(self):
        response = self.api_call()
        return response

    def some_func_with_param(self,age):
        response = self.api_call_with_param(age)
        return response