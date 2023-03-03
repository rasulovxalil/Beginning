from random import choice

class MP3player():
    def __init__(self,songlist = []):
        self.playingsong = ''
        self.sound = 100
        self.songList = songlist
        self.condition = True

    def sarkisec(self):
        pass

    def sesartir(self):
        pass

    def sesazalt(self):
        pass

    def rastgelesarkisec(self):
        pass

    def sarkiekle(self):
        pass

    def sarkisil(self):
        pass

    def shut(self):
        self.condition = False

    def showmenu(self):
        print(""""
song list : {}
now playing: {}
volume: {}

1)choose song
2)raise volume
3)minimize volume
4)choose random song
5)add song
6)delete song
7)Shut down        
 """.format(self.songList,self.playingsong,self.sound))
    def choose(self):
        choice = int(input("Enter your choice: "))
        while choice < 1 or choice > 7:
            choice = int(input("Wrong value, Please try again: "))

        return choice

    def run(self):
        self.showmenu()
        choice = self.choose()

        if choice== 1:
            counter  = 1
            for song in self.songList:
                print('{}) {}'.format(counter, song))
                counter += 1

            choosensong = int(input('Enter which song you want to choose: '))
            while choosensong > 1 or choosensong > len(self.songList):
                choosensong = int(input('Enter correct number for song, it can be:(1-{}) '.format(self.songList)))
            self.playingsong = self.songList[choosensong - 1]
        if choice == 2:
            if self.sound == 100:
                pass
            else:
                self.sound += 10
        if choice == 3:
            if self.sound ==0:
                pass
            else:
                self.sound -= 10
        if choice == 4:
            rssec = choice(self.songList)
            self.playingsong = rssec

        if choice == 5:
            artist = input("Enter the artist/group: ")
            song = input('enter the song:')

            self.songList.append(artist + '-' + song )
        if choice == 6:
            counter = 1
            for song in self.songList:
                print('{}{}'.format(counter,song))
                counter += 1

            deletedsong  = int(input('Enter which song you want to delete: '))
            while deletedsong > 1 or deletedsong > len(self.songList):
                deletedsong = int(input('Enter correct number for song, it can be:(1-{}) '.format(self.songList)))
            self.songList.pop(deletedsong-1)
        if choice == 7:
            self.shut()

mp3player = MP3player()
while mp3player.condition:
    mp3player.run()

print("Progrsm finished")