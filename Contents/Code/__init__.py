import soundcloud

PREFIX = '/music/soundcloud2'
TITLE = 'SoundCloud2'
CLIENT_ID = '7c2d3445e3bef47d9ddbbe02d859c5f3'
CLIENT_SECRET = 'a2f4e60c71bbcd324c4c7432fe56809d'

def Start():
    ObjectContainer.title1 = NAME
    Authenticate()

def ValidatePrefs():
    Authenticate()

@handler(PREFIX, TITLE)
def MainMenu():
    oc = ObjectContainer(no_cache = True)
    if IsLoggedIn():
		oc.add(DirectoryObject(key = Callback(Stream), title='Stream'))
    	oc.add(DirectoryObject(key = Callback(MyLikes), title = 'My Likes')
        oc.add(DirectoryObject(key = Callback(MyTracks, title = 'My Tracks')

    oc.add(InputDirectoryObject(
    	key = Callback(Search, prompt='Search for...'),
    	title = 'Search'))
    oc.add(InputDirectoryObject(
    	key = Callback(SearchTracks, prompt='Search for track...'),
    	title = 'SearchTracks '))
    oc.add(InputDirectoryObject(
    	key = Callback(SearchUsers, prompt='Search for user...'),
    	title = 'SearchUsers'))
    oc.add(InputDirectoryObject(
    	key = Callback(SearchGroups, prompt='Search for group...'),
    	title = 'SearchGroups'))
    oc.add(PrefsObject(title=L('Preferences')))
	return oc

@handler(PREFIX + '/stream')
def Stream():
	if not IsLoggedIn:
		return LoginFailedMessage()

	oc = ObjectContainer(no_cache = True)
	return oc

@handler(PREFIX + '/my-likes')
def MyTracks():
	oc = ObjectContainer(no_cache = True)
	return oc

@handler(PREFIX + '/my-tracks')
def MyTracks():
	oc = ObjectContainer(no_cache = True)
	return oc

@handler(PREFIX + '/search')
def Search(query, url = None):
	pass

@handler(PREFIX + '/search-tracks')
def SearchTracks(query, url = None):
	pass

@handler(PREFIX + '/search-users')
def SearchUsers(query, url = None):
	pass

@handler(PREFIX + '/search-groups')
def SearchGroups(query, url = None):
	pass

def IsLoggedIn():
	return 'loggedIn' in Dict and Dict['loggedIn'] = True

def LoginFailedMessage():
    return ObjectContainer(
    	header = 'Login Failed',
    	message = 'Please check your username and password')

def Authenticate():
    Log.Debug('Authenticate')
    if not (Prefs['username'] and Prefs['password']):
    	return False
    try:
    	client = soundcloud.Client(
    		client_id = CLIENT_ID,
    		client_secret = CLIENT_SECRET,
    		username = Prefs['username'],
    		password = Prefs['password'])
    	
        Dict['loggedIn'] = True
        Log.Info('Login Successful')
        return True
    except Ex.HTTPError, e:
        Log.Error(e.content)
        Dict['loggedIn'] = False
        Log.Error('Login Failed')
        return False
    except:
        Dict['loggedIn'] = False
        Log.Error('Login Failed')
        return False
