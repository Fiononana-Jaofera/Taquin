import tkinter as tk
import random

racine = tk.Tk()
racine.title('Taquin')

shuffling = 10
animation_delai = 500
visited = []
goal = [1,2,3,4,5,6,7,8,0]
init = [1,2,3,4,5,6,7,8,0]

class Queue:
    def __init__(self, liste = []):
        self.items = liste
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def index(self, item):
        return self.items.index(item)
    def lst_in(self):
        return self.items[0]
    def clear(self):
        return self.items.clear()

def flip(liste, id1, id2):
    result = liste.copy()
    temp = result[id1]
    result[id1] = result[id2]
    result[id2] = temp
    return result

def find_neighbours(liste):
    if liste.index(0) == 0:
        return flip(liste, 0, 1), flip(liste, 0, 3)
    elif liste.index(0) == 2:
        return flip(liste, 2, 1), flip(liste, 2, 5)
    elif liste.index(0) == 6:
        return flip(liste, 6, 3), flip(liste, 6, 7)
    elif liste.index(0) == 8:
        return flip(liste, 8, 7), flip(liste, 8, 5)
    elif liste.index(0) == 1:
        return flip(liste, 1, 0), flip(liste, 1, 4), flip(liste, 1, 2)
    elif liste.index(0) == 3:
        return flip(liste, 3, 0), flip(liste, 3, 4), flip(liste, 3, 6)
    elif liste.index(0) == 5:
        return flip(liste, 5, 2), flip(liste, 5, 4), flip(liste, 5, 8)
    elif liste.index(0) == 7:
        return flip(liste, 7, 6), flip(liste, 7, 4), flip(liste, 7, 8)
    elif liste.index(0) == 4:
        return flip(liste, 1, 4), flip(liste, 3, 4), flip(liste, 5, 4), flip(liste, 7, 4)

def bfs():
    global init
    global visited
    visited.append(init)
    q = Queue()
    q.enqueue(init)
    while q.lst_in()!=goal:
        v = q.dequeue()
        neighbours = find_neighbours(v)
        for u in neighbours:
            if u not in visited:
                visited.append(u)
                print(len(visited))
                q.enqueue(u)
                if u == goal:
                    break
    q.clear()

road = []
def find_road():
    global visited
    global init
    goal = visited.pop()
    road.append(goal)
    while goal!=init:
        for i in visited:
            if goal in find_neighbours(i):
                goal = i.copy()
                road.append(i.copy())
                break

def check_neighbours(liste, idx):
    if idx == 0:
        return liste[1], liste[3] 
    elif idx == 2:
        return liste[1], liste[5]
    elif idx == 6:
        return liste[3], liste[7]
    elif idx == 8:
        return liste[7], liste[5]
    elif idx == 1:
        return liste[0], liste[4], liste[2]
    elif idx == 3:
        return liste[0], liste[4], liste[6]
    elif idx == 5:
        return liste[2], liste[4], liste[8]
    elif idx == 7:
        return liste[6], liste[4], liste[8]
    elif idx == 4:
        return liste[1], liste[3], liste[5], liste[7]

def animation(road, i=0, lst=-1):
    if i < len(road):
        name_label = '.!frame.!frame.l'

        now = road[i].index(0)
        lst = now if lst==-1 else lst

        now_element, lst_element = road[i][now], road[i][lst]

        now_block = racine.nametowidget(f'{name_label}{now_element}')
        now_info = now_block.grid_info()

        lst_block = racine.nametowidget(f'{name_label}{lst_element}')
        lst_info = lst_block.grid_info()

        now_block.grid(row=lst_info['row'], column=lst_info['column'])
        lst_block.grid(row=now_info['row'], column=now_info['column'])

        racine.after(animation_delai, animation, road, i+1, now)

def on_label_click(event):
    global init
    clicked_label = int(str(event.widget)[-1])
    index_clicked=init.index(clicked_label)
    if clicked_label!=0:
        if 0 in check_neighbours(init, index_clicked):
            index_empty = init.index(0)
            init = flip(init, index_clicked, index_empty)

            empty_block = racine.nametowidget('.!frame.!frame.l0')
            empty_info = empty_block.grid_info()
            clicked_info = event.widget.grid_info()

            empty_block.grid(row=clicked_info['row'], column=clicked_info['column'])
            event.widget.grid(row=empty_info['row'], column=empty_info['column'])

def on_button_click(event):
    global init
    global visited
    global road
    global goal
    clicked_button = str(event.widget).split('.')[-1]
    if clicked_button == 'resolve':
        bfs()
        print('noeuds visités: ',len(visited))
        find_road()
        road.reverse()
        print('chemin trouvé: \n',road)
        print('noeuds parcourus: ', len(road))

        animation(road.copy())
        init = goal.copy()
        visited.clear()
        print('done!')

    elif clicked_button == 'shuffle':
        print('shuffling...')
        for i in range(shuffling):
            if i==0: road.append(init)
            while init in road:
                init = random.choice(find_neighbours(road[-1]))
            road.append(init.copy())
        animation(road.copy())
        
    road.clear()
