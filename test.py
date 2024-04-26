## this is just a temporary
### traing 
for i in range(1,48):
    input = f"""
    @log
    def test_{i}(self):
            clickToNewevent(self.driver)
            data =  self.lst[{i-1}]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)
    """
    print(input)
    
