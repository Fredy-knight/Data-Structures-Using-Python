class song:
    def __init__(this,music):
        this.music = music
        this.next = None
class PlayList:
    def __init__(this):
        this.head=None
    def is_empty(this):
        return this.head is None
    def add_song_at_the_begining(this,music):
        new_song = song(music)
        if this.head is None:
            this.head = new_song
        else:
            new_song.next = this.head
            this.head = new_song
    def add_song_at_the_end(this,music):
        new_song = song(music)
        if this.head is None:
            this.head = new_song
        current = this.head
        while current.next:
            current = current.next
        current.next = new_song
    def add_song_at_middle(this,music,prev):
        new_song = song(music)
        if this.head is None:
            this.head = new_head
        current = this.head
        while current:
            if current.music ==prev:
                new_song.next = current.next
                current.next = new_song
                return
            current = current.next
        return None
    def find_the_song(this,music):
        current = this.head
        while current:
            if current.music == music:
                return True
            current = current.next
        return False
    def remove_a_song(this,music):
        if this.head.music == music:
            this.head =this.head.next
            return
        current = this.head
        while current.next:
            if current.next.music==music:
                current.next = current.next.next
                return
            current = current.next
        return False
    def display_the_playlist(this):
        current = this.head
        while current:
            print(current.music,end="\n")
            current=current.next
    
if __name__=='__main__':
    print("---------PLAY LIST---------")
    isai= PlayList()
    isai.add_song_at_the_begining("beliver-imagine_dragon")
    isai.add_song_at_the_end("wavin flag")
    isai.add_song_at_the_end("mocking bird-eminem")
    isai.add_song_at_middle("enemy-imagne_dragon","wavin flag")
    isai.display_the_playlist()
    print("----------")
    a=isai.find_the_song("wavin flag")
    print("The song : Wavin flag is ",a)
    isai.remove_a_song("wavin flag")
    print("---Playlist after removing the song wavin flag:---")
    isai.display_the_playlist()
        

    
                
    
        
        
    
