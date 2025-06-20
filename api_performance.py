
#This function calls an API and measures the response time.
    def get_waste(self,Istoken,Scope):
        header={"Content-Type" : "application/json"}
        url = 'http://server.alcoholanalytics.com/'; #server URL
        url += '/api/mobile/v4.php'; #API URL
        param = {'jsonrpc' : '2.0', 'method': 'getWaste', 'params': [Istoken,Scope], 'id': '1'}; #API parameters
        start = time.time()
        myJson = requests.post(url,data=json.dumps(param),headers=header) #API Call
        a=myJson.json()
        roundtrip = time.time() - start #measure the roundtrip time
        if roundtrip>5: #Send an email in case the roundtrip is bigger than 5 seconds
            mail = smtp.automated_email('techsupport@weissbeerger.com', ['meir@weissbeerger.com','omri@weissbeerger.com','dalia@weissbeerger.com','hila.fadida@weissbeerger.com'], 'getWaste API response time')
            mail.attach_text('The API response time exceeded 2 sec: '+ str(float(roundtrip))+ 'Sec')
            mail.send_email('email-smtp.eu-west-1.amazonaws.com', 587, 'AKIAIKHCZB6HSUILMQPA', 'AqMU5jqjQ55CyrKEQZInIBW0w/qTaW5LugI9x3MTPi9l')
