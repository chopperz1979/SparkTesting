import requests

# disable warnings about using certificate verification
requests.packages.urllib3.disable_warnings()

class Room(object):
    def __init__(self, hostname, header):
        self.header = header
        self.get_rooms_url = "https://" + hostname + "/v1/rooms/"

    def getDetails(self, id, showSipAddress = ''):
        args = { 'showSipAddress':showSipAddress }
        params = ''
        for key in args.keys() :
            if key :
                params += key + '=' + str(args[key]) + '&'

        working_url = self.get_rooms_url + id + '?' + params
        api_response = requests.get(working_url, headers=self.header, verify=True)

        if api_response.status_code == 200 :
            response_json = api_response.json()
            detailDict = response_json
        else :
            detailDict = {}

        #Returns detailDict is a dictionary of room details or an empty dictionary
        # based on API status code
        return detailDict

    def create(self, title):
        working_url = self.get_rooms_url
        api_response = requests.post(working_url, headers=self.header, verify=True, 
                                     data = {'title':title})

        if api_response.status_code == 200 :
            response_json = api_response.json()
            roomId = response_json['id'] 
        else :
            roomId = ''
    
        #Returns a string which contains the roomId or undefined string based on API
        # status code
        return roomId
        
    def delete(self, id):
        working_url = self.get_rooms_url + id
        api_response = requests.delete(working_url, headers=self.header, verify=True)

        if api_response.status_code == 204 :
            deleted = True
        else :
            deleted = False

        #Returns a boolean based on the status_code of the API call
        return deleted

    def update(self, id, title):
        working_url = self.get_rooms_url + id
        api_response = requests.put(working_url, headers=self.header, verify=True, 
                                    data = {'title':title})

        if api_response.status_code == 200 :
            updated = True
        else :
            updated = False
    
        #Returns a boolean based on the status_code of the API call
        return updated

    def listRooms(self, showSipAddress = '' , max = '') :
        args = { 'showSipAddress':showSipAddress , 'max':str(max) }
        params = ''
        for key in args.keys() :
            if key :
                params += key + '=' + str(args[key]) + '&'

        working_url = self.get_rooms_url + '?' + params
        api_response = requests.get(working_url, headers=self.header, verify=True)

        if api_response.status_code == 200 :
            response_json = api_response.json()
            roomDict = response_json
        else :
            roomDict = {}

        #Returns roomDict is a dictionary of lists of dictionaries or an empty dictionary
        # based on API status code
        return roomDict

##################
class Person(object):
    def __init__(self, hostname, header):
        self.header = header
        self.get_people_url = "https://" + hostname + "/v1/people/"

    def getDetails(self, id):
        working_url = self.get_people_url + id
        api_response = requests.get(working_url, headers=self.header, verify=True)

        if api_response.status_code == 200 :
            response_json = api_response.json()
            detailDict = response_json 
        else :
            detailDict = {}

        #Returns a dictionary which contains the requested attributes or undefined string 
        # based on API status code
        return detailDict
    
    def listPeople(self, email = '', displayName = '', max = ''):
        args = { 'email':email, 'displayName':displayName, 'max':str(max) }
        params = ''
        for key in args.keys() :
            if args[key] :
                params += key + '=' + str(args[key]) + '&'

        working_url = self.get_people_url + '?' + params
        api_response = requests.get(working_url, headers=self.header, verify=True)

        if api_response.status_code == 200 :
            response_json = api_response.json()
            peopleDict = response_json
        else :
            peopleDict = {}

        #Returns peopleDict is a dictionary of lists of dictionaries or an empty dictionary
        # based on API status code
        return peopleDict

##################
class Message(object):
    def __init__(self, hostname, header):
        self.header = header
        self.get_message_url = "https://" + hostname + "/v1/messages/"

    def getDetails(self, id):
        working_url = self.get_message_url + id
        api_response = requests.get(working_url, headers=self.header, verify=True)

        if api_response.status_code == 200 :
            response_json = api_response.json()
            detailDict = response_json
        else :
            detailDict = {}

        #Returns a dictionary  which contains the requested attributes or undefined string 
        # based on API status code
        return detailDict

    def create(self, roomId = '', text = '', files = [], file = '', 
               toPersonId = '', toPersonEmail = ''):
        args = { 'roomId':roomId, 'text':text, 'files':files, 'file':file, 
                 'toPersonId':toPersonId, 'toPersonEmail':toPersonEmail }
        dataSet = {}
        for key in args.keys() :
            if args[key] :
                dataSet[key] = args[key]

        working_url = self.get_message_url
        api_response = requests.post(working_url, headers=self.header, verify=True, data = dataSet)
        if api_response.status_code == 200 :
            created = True
        else :
            created = False

        #Returns a boolean based on the status_code of the API call
        return created

    def delete(self, messageId):
        working_url = self.get_message_url + messageId
        api_response = requests.delete(working_url, headers=self.header, verify=True)

        if api_response.status_code == 204 :
            deleted = True
        else :
            deleted = False

        #Returns a boolean based on the status_code of the API call
        return deleted
    
    def listMessages(self, roomId, before = '', beforeMessage = '', max = '' ):
        args = {'roomId':roomId, 'before':before, 'beforeMessage':beforeMessage, 'max':str(max) }
        params = ''
        for key in args.keys() :
            if args[key] :
                params += key + '=' + str(args[key]) + '&'

        working_url = self.get_message_url + '?' + params
        api_response = requests.get(working_url, headers=self.header, verify=True)

        if api_response.status_code == 200 :
            response_json = api_response.json()
            messageDict = response_json
        else :
            messageDict = {}

        #Returns messageDict is a dictionary of lists of dictionaries or an empty dictionary
        # based on API status code
        return messageDict

##################
class Membership(object):
    def __init__(self, hostname, header):
        self.header = header
        self.get_memberships_url = "https://" + hostname + "/v1/memberships/"

    def getDetails(self, id):
        working_url = self.get_memberships_url + id
        api_response = requests.get(working_url, headers=self.header, verify=True)

        if api_response.status_code == 200 :
            response_json = api_response.json()
            detailDict = response_json
        else :
            detailDict = {}

        #Returns a dictionary  which contains the request attribute or undefined string 
        # based on API status code
        return detailDict

    def create(self, roomId, personId = '', personEmail = '', isModerator = ''):
        args = { 'roomId':roomId, 'personId':personId, 'personEmail':personEmail, 'isModerator':isModerator }
        dataSet = {}
        for key in args.keys() :
            if args[key] :
                dataSet[key] = args[key]

        working_url = self.get_memberships_url
        api_response = requests.post(working_url, headers=self.header, verify=True, 
                                     data = dataSet)

        if api_response.status_code == 200 :
            created = True 
        else :
            created = False
    
        #Returns a boolean based on the status_code of the API call
        return created
        
    def delete(self, id):
        working_url = self.get_memberships_url + id
        api_response = requests.delete(working_url, headers=self.header, verify=True)

        if api_response.status_code == 204 :
            deleted = True
        else :
            deleted = False

        #Returns a boolean based on the status_code of the API call
        return deleted

    def update(self, isModerator):
        working_url = self.get_memberships_url
        api_response = requests.put(working_url, headers=self.header, verify=True, 
                                    data = {'isModerator':isModerator})

        if api_response.status_code == 200 :
            updated = True
        else :
            updated = False
    
        #Returns a boolean based on the status_code of the API call
        return updated

    def listMemberships(self, roomId = '', personId = '', personEmail = '', max = '') :
        args = {'roomId':roomId, 'personId':personId, 'personEmail':personEmail, 'max':str(max) }
        params = ''
        for key in args.keys() :
            if args[key] :
                params += key + '=' + str(args[key]) + '&'

        working_url = self.get_memberships_url + '?' + params
        api_response = requests.get(working_url, headers=self.header, verify=True)

        if api_response.status_code == 200 :
            response_json = api_response.json()
            membershipsDict = response_json
        else :
            membershipsDict = {}

        #Returns membershipsDict is a dictionary of lists of dictionaries or an empty dictionary
        # based on API status code
        return membershipsDict


