import tkinter as tk
from json import loads

def uname(fans):
    uname_list = []
    for fan in fans["data"]["list"]:
        uname_list.append(fan['uname'])
    return uname_list

def level_title(num):
    level = num // 10
    titles = [
        "宇宙级粉丝",
        "星云级粉丝",
        "星系级粉丝",
        "黑洞级粉丝",
        "中子星级粉丝",
        "蓝巨星级粉丝",
        "黑矮星级粉丝",
        "白矮星级粉丝",
        "红矮星级粉丝",
        "行星级粉丝",
        "小行星级粉丝",
    ]
    
    if level <= 9:
        return titles[level]
    else:
        return titles[10]

def command(temp):
    unames = uname(temp)
    r = 0
    for i in range(len(unames)-1,-1,-1):
        j = unames[i]
        dengji = level_title(r)
        r += 1
        print("title @a subtitle {\"text\":\"" + j + " 等级：" + dengji + " 第" + str(r) + "个关注" + "\",\"color\":\"white\",\"bold\":\"ture\"}")

def get_input():
    global input_get
    try:
        input_get = input_entry.get()
        input_get = loads(input_get)
        command(input_get)
    except:
        print('输入错了')
    window.destroy()

def windows():
    global input_entry, window

    window = tk.Tk()

    input_entry = tk.Entry(window, width=50, borderwidth=5)
    input_entry.pack() 

    button = tk.Button(window, text='获取输入(正确输入！)', command=get_input)
    button.pack()

    window.mainloop()

def main():
    print('--------------------\n无聊的解析工具 v0.1\n作者:我叫小萌新QWQ\n内部开发版\n(只可以获取前五页哦)\n--------------------\n')

    uid = input('请输入用户uid号:')
    while True:
        page = input('请输入页数1-5(前五页全部不做输入):')
        if page == '':
            page = ''
            break
        elif page >= '1' and page <= '5':
            page = int(page)
            break
    
    print(f'https://api.bilibili.com/x/relation/followers?vmid={uid}{f"&pn={page}&ps=20" if page else ""}&order=desc&jsonp=jsonp&callback=\n请全选内容并复制到下方')
    
    windows()

    input()

if __name__ == '__main__':
    main()