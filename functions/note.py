# coding: utf-8

from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

def handle(mic, comamnd, profile):
	"""
	Go to link: https://dev.evernote.com/doc/start/python.php
	for guide
	"""

	auth_token = profile['evernote']['token']
	client = EvernoteClient(token=auth_token)
	note_store = client.get_note_store()
	
	note = Types.Note()
	note.title = "Ghi chú trên JarvisPi"
	#mic.speak("Nội dung ghi chú là gì?")
	tts.speak_wav("noi_dung_ghi_chu_la_gi.wav")
	content = mic.activeListen()
	note.content = '<?xml version="1.0" encoding="UTF-8"?>'
	note.content += '<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
	note.content += '<en-note>Note:<br/>'
	note.content += ('%s' % content)
	note.content += '</en-note>'
    
	created_note = note_store.createNote(note)
	#mic.speak("Ghi chú thành công")
	tts.speak_wav("ghi_chu_thanh_cong.wav")

    #TODO: Add funtions read notes

def isMatch(command):
	return command == u"GHI CHÚ" or command == r"THEEM GHI CHUS"
