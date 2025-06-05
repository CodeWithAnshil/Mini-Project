
import json

def load_data():
    try:
        with open('youtube.txt','r') as file :
             return json.load(file)
    except FileNotFoundError:
           return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        return json.dump(videos,file)    

def list_all_videos(videos):
   print("\n")
   print("*"*20)
   for index,video in enumerate(videos,start=1):
       print(f"{index},{video['name']},Duration: {video['time']}")
   print("*"*20)
def add_videos(videos):
    name=input("Enter yout video name : ")
    time=input("Enter your video length : ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def delete_videos(videos):
   list_all_videos(videos)
   index = int(input("Enter your number for delete : "))
   if 1<=index<=len(videos):
       del videos[index-1]
       save_data_helper(videos)
   else:
       print("Invalid index: please enter valid index number")

def update_videos(videos):
   list_all_videos(videos)
   index = int(input("Enter your video number for update "))
   if 1<= index<=len(videos):
       name=input("Enter your video name : ")
       time=input("Enter yout video length : ")
       videos[index-1]={'name':name,'time':time}
       save_data_helper(videos)
   else:
       print("Invalid index")


def main():
    videos=load_data()
    while True:
      print("\n Youtube Manager | Chooise an option ")
      print("1. List all youtube video")
      print("2. Add a youtube video")
      print("3. Delete youtube video")
      print("4. Update youtube video details")
      print("5. Exit the app")
      choice=input("Enter your choice ")

      match choice:
        case '1':
            list_all_videos(videos)
        case '2':
            add_videos(videos)  
        case '3':
            delete_videos(videos)  
        case '4':
            update_videos(videos)
        case '5':
             break
        case _:
            print("Invalid choice: Please select valide choice")


if __name__== "__main__":
    main()

      