# class Book:
#     def __init__(self,name,authors,genre,isbn):
#         self.name=name
#         self.authors=authors
#         self.genre=genre
#         self.isbn=isbn
    
#     def display_info(self):
#         print(f"Book:{self.name}")
#         print(f"Authors: {','.join(self.authors)}")
#         print(f"Genre: {self.genre}")
#         print(f"ISBN: {self.isbn}")

# book1=Book("The Great Gatsby", ["F.Scott Fitzgerald"],"Fiction","978-3-16-148410-0")
# book2=Book("Python Crash Course",["Eric Matthes","Some Other Author"],"Programming","978-1-23-456789-0")
# book1.display_info()
# print("\n")
# book2.display_info()

class Albums:
    def __init__(self,name,artist,tracklist):
        self.name=name
        self.artist=artist
        self.tracklist=tracklist

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Artist: {self.artist}")
        for i in range(len(self.tracklist)):
            track=self.tracklist[i]
            print(f"{i+1}. {track.name} by {','.join(track.artist)}")
            

class Artist_Track:
    def __init__(self,name,artist):
        self.name=name
        self.artist=artist

    def display(self):
        print(f"{self.name} by Other Artist:{','.join(self.artist)}")
        

track=Artist_Track("Song Name",["Smith","John"])
track1=Artist_Track("Song 2",["Andrew"])
T=Albums("OEN","Kol",[track,track1])
T.display_info()