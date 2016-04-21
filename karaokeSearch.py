################################################################################## 
##     This program is free software: you can redistribute it and/or modify     ## 
##     it under the terms of the GNU General Public License as published by     ## 
##     the Free Software Foundation, either version 3 of the License, or        ## 
##     (at your option) any later version.                                      ## 
##                                                                              ## 
##     This program is distributed in the hope that it will be useful,          ## 
##     but WITHOUT ANY WARRANTY; without even the implied warranty of           ## 
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            ## 
##     GNU General Public License for more details.                             ## 
##                                                                              ## 
##     You should have received a copy of the GNU General Public License        ## 
##     along with this program.  If not, see <http://www.gnu.org/licenses/>.    ## 
##                                                                              ##
##    Copyleft 2016 Victor Tinoco Horrillo                                      ##
##		correo: victor.tinoco.86@gmail.com  												              ##
##                                                                              ##
##################################################################################



#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import os
import sys
import numpy as np
from PIL import Image
import pytesseract as TESS
from apiclient.discovery import build
import youtube_dl
from PyDictionary import PyDictionary

os.chdir("/home/tincan/Documentos/KaraokeSearch")
DEVELOPER_KEY = "Usar key de google"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class searchKaraoke(object):

    def __init__(self, word, numberVideos):
        """Entrada de parametros"""

        self.word = word
        self.numberVideos = numberVideos

    def download_video(self, videos):
        """ Uso del modulo youtube-dl para descargar videos.
            Busca las URL una a una que hay almacenada en videos.
            Descargas esos vidoes en formato mp4 y le deja de nombre el identificador de youtube
            y la extension """
        
        for k in range(len(videos)):
            ydl_opts = {'format': 'mp4', 'outtmpl': '%(id)s.%(ext)s'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([videos[k]["URL"]])

    def scanOCR(self, video):  
        """Este metodo lo que hace es extraer la letra de los videos descargados y lo almacena en la
            variable lyric  que es la que devuelve. Para ello hace uso de los modulos OpenCV y pytesseract"""
        
        capture = cv2.VideoCapture(video)
        count = 0
        
        if capture.isOpened():
            rval , frame = capture.read()
        else:
            rval = False

        lyric = ""
        lyricStaging = ""
        removeLog = []
        removeLogStaging = []
        posCount = 0
        negCount = 0
        while rval:
            rval, frame = capture.read()
            if rval == True:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            count = count + 1
            # Toma 1 de cada 100 fotogramas para su analisis
            if count % 100 == 0:
                cv2.imwrite(str(count) + '.jpg',gray)
                img = TESS.image_to_string(Image.open(str(count) + ".jpg"))
                imgString = str(img)
                # Eliminamos caracteres extraños que no pertenencen a la cancion
                for ch in "ªº!|@#$~‘%½&¬=1234567890\"-+*.'¿?·:;,()}\n{[]\\ï><©_":
                    if ch in imgString:
                        imgString = imgString.replace(ch, " ")
                ' '.join(imgString.split())
                os.remove(str(count) + ".jpg")
                # Tomamos una pequeña muestra de la cancion si se repite no la pasa pues puede ser
                # que estemos en un fotograma que sea igual que el anterior. 
                if lyricStaging[1:7] != imgString[1:7]:
                    # Elimina Logos en pantalla con al menos dos letras.                    
                    if lyricStaging != "":                        
                        if removeLog == []:
                            for ch in lyricStaging.split():                                
                                if (ch in imgString) and (ch not in removeLog):
                                    removeLog.append(ch)
                        else:
                            splitImgStr = imgString.split()
                            for ch in splitImgStr:
                                if (ch in removeLog) and (ch not in removeLogStaging):
                                    removeLogStaging.append(ch)
                            for ch in removeLog:
                                if (ch not in removeLogStaging) and (len(removeLog) > 2):
                                    removeLog.remove(ch)
                            if len(removeLog) == 2:
                                if (removeLog[0] in splitImgStr) or (removeLog[1] in splitImgStr):
                                    posCount += 1
                                else:
                                    negCount += 1                                    
                    removeLogStaging = []            
                    lyricStaging = imgString
                    lyric = lyric + " " + imgString
                    
        lyric = lyric.replace("\n", " ")
        if posCount >= negCount:
            for ch in removeLog:
                lyric = lyric.replace(ch, "")
        lyric = ' '.join(lyric.split())
        capture.release()
        cv2.destroyAllWindows()
        return lyric

    def pieceOfLyric(self, video, numWord): 
        """ Para la que la Api de MusixMatch funcione solo neceisita un trozo de la letra con palabras
            relevantes, por ello se usa pieceLyric. Que se queda con las palabras mayores de tres letras"""
        
        lyric = self.scanOCR(video) 
        searchLyric = lyric[100:]
        searchLyriclist = searchLyric.split()
        listLyric = ""
        lenLyriclist = len(searchLyriclist)
        count = 0
        countlen = 0
        dictionary=PyDictionary()
        while (count <= numWord) and (countlen < lenLyriclist):
            # El numero de letras por palabra es mayor de dos
            if len(searchLyriclist[countlen]) > 2:
                if searchLyriclist[countlen] not in listLyric:
                    #Busca si la palabra existe en google
                    if dictionary.googlemeaning(searchLyriclist[countlen]):
                        listLyric = listLyric + " " + searchLyriclist[countlen]
                        count += 1
            countlen += 1
        return listLyric



import urllib2, json, io, gzip, simplejson, lxml, urllib, re
from bs4 import BeautifulSoup, NavigableString
from StringIO import StringIO
os.environ["MUSIXMATCH_API_KEY"] = "usar key de musixmatch"
from musixmatch import track
import ast
import mysql.connector
from mysql.connector import errorcode

class second(searchKaraoke):
    def getInfoLyric(self, video, numWord=10):
        """ Extraemos la informacion del API de MusixMatch. En caso de que el numero de palabras sea
            inferior a cinco devuelve la lista vacia. Aqui se define el numero maximo de palabras que
            quiere de la cancion"""
        
        trackToList = []
        words = self.pieceOfLyric(video, numWord) 
        while trackToList == []:
            # modificando esta linea se modifica el minimo para su validez
            if len(words.split()) < 3:
                break
            tracks = track.search(q = words)
            if tracks == []:
                words1 = self.didYouMean(words)
                if words != "":
                    tracks = track.search(q = words1)
            for k in range(len(tracks)):
                trackToString = str(tracks[k])[18:]
                trackToDict = ast.literal_eval(trackToString)
                trackToList.append(trackToDict)
            wordSplit = words.split()
            wordSplitLessOne = wordSplit[1:]
            words = ""
            for ch in range(len(wordSplitLessOne)):
                words += str(wordSplitLessOne[ch]) + " "        
        return trackToList
    
    
    def getPage(self, url):
        """El creador de este trozo de codigo es Virendra Rajput con una GNU GENERAL PUBLIC LICENSE web: https://github.com/bkvirendra/didyoumean"""
        request = urllib2.Request(url)
        request.add_header('Accept-encoding', 'gzip')
        request.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20')
        response = urllib2.urlopen(request)
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO( response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
        else:
            data = response.read()
        return data
    

   
    def didYouMean(self, words):
        """El creador de este trozo de codigo es Virendra Rajput con una GNU GENERAL PUBLIC LICENSE web: https://github.com/bkvirendra/didyoumean """
        q = str(str.lower(words)).strip()
        url = "http://www.google.com/search?q=" + urllib.quote(q)
        html = self.getPage(url)
        soup = BeautifulSoup(html, "lxml")
        ans = soup.find('a', attrs={'class' : 'spell'})
        try:
            result = repr(ans.contents)
            result = result.replace("u'","")
            result = result.replace("/","")
            result = result.replace("<b>","")
            result = result.replace("<i>","")
            result = re.sub('[^A-Za-z0-9\s]+', '', result)
            result = re.sub(' +',' ',result)
        except AttributeError:
            result = q
        return result

    def getInformation(self, video):  
        """ De la variable devuelta en el paso anterior se crea una lista con cadena de caracteres
            que contienen artistas y nombre de la cancion. Para su posterior coincidencia con la
            informacion del titulo y la descripcion que devuelve la api de youtube"""
        
        listInfo = []
        trackInfo = self.getInfoLyric(video) 
        for k in range(len(trackInfo)):
            stringInfo = trackInfo[k]["artist_name"], trackInfo[k]["track_name"]
            listInfo.append(stringInfo)
        return listInfo

    def compareInfo(self, videos):
        """ Tanto con la informacion aportada por la api de YouTube como con la aportada por la apis
            de MusixMatch compara si son la que concuardan mas para devolverlo como karaoke"""
        
        bestResult = []
        dataResult = {}
        dataResult["URL"] = ""
        dataResult["count"] = 0
        dataResult["cancion"] = ""
        bestResult.append(dataResult)
        for k in range(len(videos)):
            video = videos[k]["id"] + ".mp4"
            infoVideoMusix = self.getInformation(video)
            infoVideoYoutube = videos[k]["title"] + " " + videos[k]["description"]
            videoURL = videos[k]["URL"]
            countMusixMatch = 0
            infoVideoResult = ""
            infoVideoYoutubeSplit = infoVideoYoutube.split()
            for j in range(len(infoVideoMusix)): 
                countYoutube = 0
                for i in range(len(infoVideoYoutubeSplit)):
                    infoVideoLower = infoVideoMusix[j][0] + " " + infoVideoMusix[j][1]
                    if infoVideoYoutubeSplit[i].lower() in infoVideoLower.lower():
                        countYoutube += 1
                if countYoutube > countMusixMatch:
                    countMusixMatch = countYoutube
                    infoVideoArtista = infoVideoMusix[j][0]
                    infoVideoCancion = infoVideoMusix[j][1]
            if countMusixMatch > bestResult[0]["count"]:
                bestResult[0]["URL"] = videoURL
                bestResult[0]["count"] = countMusixMatch
                bestResult[0]["artista"] = infoVideoArtista
                bestResult[0]["cancion"] = infoVideoCancion
        return bestResult

    def youtubeSearch(self):
        """Buscardor en la api de youtube"""
        
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
        search_response = youtube.search().list(q=self.word, part="id,snippet", maxResults=self.numberVideos).execute()
        videos = []

        for search_result in search_response.get("items", []):
            dataVideo = {}
            if search_result["id"]["kind"] == "youtube#video":
                link = "https://www.youtube.com/watch?v=%s" % (search_result["id"]["videoId"])
                titulo = search_result["snippet"]["title"]
                descripcion = search_result["snippet"]["description"]
                ident = search_result["id"]["videoId"]
                dataVideo["URL"] = link
                dataVideo["title"] = titulo
                dataVideo["description"] = descripcion
                dataVideo["id"] = ident
                videos.append(dataVideo)
        self.download_video(videos)
        return videos
    def removeVideos(self, videos):
        """Elimina los videos guardados"""
        for k in range(len(videos)):
            video = videos[k]["id"] + ".mp4"
            os.remove(video)
            
    def __str__(self):
        """ Empieza con el analis"""
        
        videos = self.youtubeSearch()
        ocr = self.compareInfo(videos)
        self.removeVideos(videos)
         
        ocrJSON = json.dumps(ocr)
        fil.write(ocrJSON)
        fil.write("\n")
        
        return str(ocr)

try:
    cnx = mysql.connector.connect(user='', password='', database='')
    print "Conneted with Database"
    query = ("SELECT Nombre, search FROM t1")
    cursor = cnx.cursor()
    cursor.execute(query)    
    for search in cursor:
        fil = open('workfile.csv', 'a')
        fil.write(str(search[0]))
        fil.write(";")
        line = str(search[1])
        line = line + " " + "karaoke"
        s = second(line, 1)
        print s.__str__()
        fil.close()
    cursor.close()
    cnx.close()
except mysql.connector.Error as err:
	print(err)
else:
    cnx.close()
