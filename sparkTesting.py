#!/usr/bin/python

import CiscoSpark, json

# Find and replace VALUE in the script to run some basic testing

hostname = 'api.ciscospark.com'        
#token = "Bearer VALUE"
header = {"Authorization": "%s" % token}


#messageId = 'VALUE'
#roomId = 'VALUE'
#personId = 'VALUE'
#membershipId = 'VALUE'

############ Room Testing ##############
def roomTest(roomId, personId, messageId) :
    room = CiscoSpark.Room(hostname, header)
    localMessageId = messageId
    localRoomId = roomId
    localPersonId = personId

    print '+++==- Testing Room Class -==+++'

    #roomDetail = room.getDetails(localRoomId, showSipAddress=False)
    roomDetail = room.getDetails(localRoomId)
    if roomDetail :
        print '##Call to getDetails##'
        print json.dumps(roomDetail, indent=4)
    else :
        print 'No details about the room with ID: ' + str(localRoomId)

    roomList = room.listRooms(showSipAddress=True, max=5)
    #roomList = room.listRooms(showSipAddress=False)
    if roomList :
        print '##Call to listRooms##'
        print json.dumps(roomList, indent=4)
    else :
        print "No items returned in the search"

############ Person Testing ##############
def personTest(roomId, personId, messageId) :
    person = CiscoSpark.Person(hostname, header)
    localMessageId = messageId
    localRoomId = roomId
    localPersonId = personId

    print '+++==- Testing Person Class -==+++'
    
    personDetails = person.getDetails(localPersonId)
    if personDetails :
        print '##Call to getDetails##'
        print json.dumps(personDetails, indent=4)
    else :
        print 'There was an error and no details on the person were returned'

    #personSearch = person.listPeople(displayName = 'Jim')
    personSearch = person.listPeople(email = 'keorourk@cisco.com')
    if personSearch['items'] :
        print '##Call to listPeople##'
        print json.dumps(personSearch, indent=4)
    else :
        print "No items returned in the search"

############ Message Testing ##############
def messageTest(roomId, personId, messageId) :
    message = CiscoSpark.Message(hostname, header)
    localMessageId = messageId
    localRoomId = roomId
    localPersonId = personId

    print '+++==- Testing Message Class -==+++'
    messageDetail = message.getDetails(localMessageId)
    if messageDetail :
        print '##Call to getDetails##'
        print json.dumps(messageDetail, indent=4)
    else :
        print 'There was an error and no details on the message were returned'

    messageList = message.listMessages(localRoomId, max = 5)
    if messageList :
        print'##Call to listMessages##'
        print json.dumps(messageList, indent=4)
    else :
        print 'There was and error and not message listing was returned'

    text = raw_input('Enter your message: ')
    messageCreated = message.create(localRoomId, text)
    if messageCreated :
        print 'You message was created!'
    else :
        print 'No message was created.'

    loopControl = ''
    while loopControl != 'no' :
        messageDict = message.listMessages(localRoomId)
        messageList = messageDict['items']
        cnt = 0
        for dictItem in messageList :
            print str(cnt) + ') Message Id:   ' + dictItem['id']
            print str(cnt) + ') Message Text: ' + dictItem['text']
            cnt +=1
        deleteId = int(raw_input('Enter the number of the message to delete(99 to end): '))
        if deleteId != 99 :
            deleted = message.delete(messageList[deleteId]['id'])
            if deleted :
                print 'Message Deleted!'
            else :
                print 'Error Deleting message!'

        #Get user input to keep looping or end
        loopControl = raw_input('Check messages again?(YES/no):  ')
        loopControl = loopControl.lower()

############ Membership Testing ##############
def membershipTest(roomId, personId, messageId, membershipId) :
    membership = CiscoSpark.Membership(hostname, header)
    localMessageId = messageId
    localRoomId = roomId
    localPersonId = personId
    localMembershipId = membershipId

    print '+++==- Testing Membership Class -==+++'
    detailDict = membership.getDetails(localMembershipId)
    if detailDict :
        print '##Call to getDetails##'
        print json.dumps(detailDict, indent=4)
    else :
        print 'There was an error and no membership details were returned'
   
    membershipDict = membership.listMemberships(localRoomId, personEmail = 'keorourk@cisco.com', max=4)
    #membershipDict = membership.listMemberships(localRoomId, max=4)
    if membershipDict :
        print '##Call to listMemberships##'
        print json.dumps(membershipDict, indent=4)
    else :
        print 'There was and error and not memberships were listed'

    #membershipCreated = membership.create(localRoomId, '', 'keorourk@cisco.com')
    #if membershipCreated :
    #    print 'You message was created!'
    #else :
    #    print 'No message was created.'

    #membershipDeleted = membership.delete(localMembershipId)
    #if membershipDeleted :
    #    print 'Membership has been deleted!'
    #else :
    #    print 'Error: Membership has NOT been deleted'


#############


messageTest(roomId, personId, messageId)
personTest(roomId, personId, messageId)
roomTest(roomId, personId, messageId)
membershipTest(roomId, personId, messageId, membershipId)

exit()
