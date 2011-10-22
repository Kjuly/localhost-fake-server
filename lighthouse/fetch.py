import sys, os

ACCOUNT		= 'theplant'
TOKEN		= 'fbc77173b4e6d050d8b8fa4184190ab91444d737'

URL_HEADER	= 'http://%s.lighthouseapp.com/' % ACCOUNT
URL_TAIL	= '?_token=%s' % TOKEN

# ---------------------------------------------------
# TOKEN
# tokens/#{token}.xml
if sys.argv[1] == '0' :
	SAVE = 'tokens/%s.xml' % TOKEN

# ---------------------------------------------------
# USER
# users/#{ID}.xml
elif sys.argv[1] == '11' :
	SAVE = 'users/%s.xml' % sys.argv[2]

# users/#{ID}/memberships.xml
elif sys.argv[1] == '12' :
	SAVE = 'users/%s/memberships.xml' % sys.argv[2]

# ---------------------------------------------------
# PROJECTs
# projects.xml
elif sys.argv[1] == '21' :
	SAVE = 'projects.xml'

# projects/#{project_id}.xml
elif sys.argv[1] == '22' :
	SAVE = 'projects/%s.xml' % sys.argv[2]

# projects/#{project_id}/memberships.xml
elif sys.argv[1] == '23' :
	SAVE = 'projects/%s/memberships.xml' % sys.argv[2]

# ---------------------------------------------------
# TICKETs
# projects/#{project_id}/tickets.xml
elif sys.argv[1] == '30' :
	SAVE = 'projects/%s/tickets.xml' % sys.argv[2]
elif sys.argv[1] == '31' :
	SAVE = 'projects/%s/tickets.xml?page=%s' % ( sys.argv[2], sys.argv[3] )

# projects/#{project_id}/tickets/#{number}.xml
elif sys.argv[1] == '32' :
	SAVE = 'projects/%s/tickets/%s.xml' % ( sys.argv[2], sys.argv[3] )

# ---------------------------------------------------
# CHANGE_SETs
# projects/#{project_id}/changesets.xml
elif sys.argv[1] == '41' :
	SAVE = 'projects/%s/changesets.xml' % sys.argv[2]

# projects/#{project_id}/changesets/#{revision}.xml +++++++++++++++++++++++++ Not Used
elif sys.argv[1] == '42' :
	SAVE = 'projects/%s/changesets/%s.xml' % ( sys.argv[2], sys.argv[3] )

# ---------------------------------------------------
# MESSAGEs
# projects/#{project_id}/messages.xml
elif sys.argv[1] == '51' :
	SAVE = 'projects/%s/messages.xml' % sys.argv[2]

# projects/#{project_id}/messages/#{ID}.xml
elif sys.argv[1] == '52' :
	SAVE = 'projects/%s/messages/%s.xml' % ( sys.argv[2], sys.argv[3] )

# ---------------------------------------------------
# MILESTONEs
# projects/#{project_id}/milestones.xml
elif sys.argv[1] == '61' :
	SAVE = 'projects/%s/milestones.xml' % sys.argv[2]

# projects/#{project_id}/milestone/#{ID}.xml
elif sys.argv[1] == '62' :
	SAVE = 'projects/%s/milestones/%s.xml' % ( sys.argv[2], sys.argv[3] )

# ---------------------------------------------------
# TICKET_BINs
# projects/#{project_id}/bins.xml
elif sys.argv[1] == '71' :
	SAVE = 'projects/%s/bins.xml' % sys.argv[2]

# projects/#{project_id}/bins/#{ID}.xml
elif sys.argv[1] == '72' :
	SAVE = 'projects/%s/bins/%s.xml' % ( sys.argv[2], sys.argv[3] )

# ---------------------------------------------------
# Process
if sys.argv[1] == '31' :
	URL = '"%s%s%s"' % ( URL_HEADER, SAVE, '&' + URL_TAIL[1:] )
else :
	URL	= '%s%s%s' % ( URL_HEADER, SAVE, URL_TAIL )
print(URL)
command = 'curl %s > %s' % ( URL, SAVE )
os.system( command )
