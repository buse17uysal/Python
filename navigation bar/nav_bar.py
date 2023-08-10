import flet,random

def main(page: flet.Page):
    page.update(),
    page.title="NavBar"
    basarili=flet.AlertDialog(title=flet.Text("Welcome!"))
    basarisiz=flet.AlertDialog(title=flet.Text("Try Again!"))   
    
    def selected(e):
        index=e.control.selected_index  
        login.visible= True if index==0 else False
        user_name.visible= True if index==0 else False
        password.visible= True if index==0 else False
        home_page.visible= True if index==0 else False
        button.visible= True if index==0 else False
        search_label.visible= True if index==1 else False
        search.visible= True if index==1 else False
        search_button.visible= True if index==1 else False
        liste.visible= True if index==1 else False
        comment_title.visible= True if index==2 else False
        comment.visible= True if index==2 else False
        comments.visible= True if index==2 else False
        comment_label.visible= True if index==2 else False
        who.visible= True if index==2 else False
        comment_button.visible= True if index==2 else False
        notification_title.visible= True if index==3 else False
        notification.visible= True if index==3 else False
        page.update(),        
    liste=flet.ListView(auto_scroll=True,
                        visible=False) 
    comments=flet.ListView(auto_scroll=True,
                        visible=False)  
    notification=flet.ListView(visible=False)
    people=["Person 1", "Person 2", "Person 3","Person 4","Person 5"]  
    random.shuffle(people) 
    events=["liked your ploto.","commented on your photo.", "followed you.","liked your comment.", "replied to your comment."]
    random.shuffle(events)
    
    def saved(e):
        liste.controls.append(flet.Text(search.value))
        search.value=""
        page.update()
            
    def isTrue(e):
        if user_name.value=="egemen" and password.value=="yazilim":
            page.dialog=basarili
            basarili.open=True
            login.visible,user_name.visible,password.visible,button.visible= False,False,False,False
            home_page.visible=True
        else:
            page.dialog=basarisiz
            basarisiz.open=True
        page.update()         
        
    def add_comment(e):
        comments.controls.append(flet.Text(who.value + ":" +comment.value))  
        comment_label.visible=False 
        comment.value,who.value="",""
        page.update()
          
    page.navigation_bar=flet.NavigationBar(
        on_change=selected,
        destinations=[
            flet.NavigationRailDestination(
                icon=flet.icons.HOME,
                label="Home"),
             flet.NavigationRailDestination(
                icon=flet.icons.SEARCH,
                label="Search"),
              flet.NavigationRailDestination(
                icon=flet.icons.COMMENT,
                label="Comment"),
               flet.NavigationRailDestination(
                icon=flet.icons.NOTIFICATIONS,
                label="Notification")])
    login=flet.Text("Login",
                   size=50,
                   font_family="Lucida Calligraphy",
                   color=flet.colors.LIGHT_GREEN,
                   visible=True)
    home_page=flet.Image(src="homepage.png",
                         visible=False)
    user_name=flet.TextField(label="User Name",
                             prefix_icon=flet.icons.PERSON,
                             max_length=20,
                             width=400,
                             visible=True)
    password=flet.TextField(label="Password",
                             max_length=20,
                             width=400,
                             password=True,
                             can_reveal_password=True,
                             prefix_icon=flet.icons.LOCK,
                             filled=True,
                             visible=True)
    button=flet.ElevatedButton(text="Login",
                               visible=True,
                               on_click=isTrue)
    search_label=flet.Text("Search",
                   size=50,
                   font_family="Lucida Calligraphy",
                   color=flet.colors.CYAN,
                   visible=False)
    search=flet.TextField(hint_text="Search",
                          prefix_icon=flet.icons.SEARCH,
                          width=450,
                          visible=False)
    search_button=flet.ElevatedButton(text="Search",
                                      visible=False,
                                      on_click=saved)
    comment_title=flet.Text("Comment",
                   size=50,
                   font_family="Lucida Calligraphy",
                   color=flet.colors.PURPLE_ACCENT,
                   visible=False)
    comment_label=flet.Text("No Comment",
                   size=25,
                   font_family="Forte",
                   visible=False)
    who=flet.Dropdown(width=150,
                      hint_text="Select",
                      icon=flet.icons.PERSON_2,
                      options=[flet.dropdown.Option(text="Person 1"),
                               flet.dropdown.Option(text="Person 2"),
                               flet.dropdown.Option(text="Person 3"),
                               flet.dropdown.Option(text="Person 4")],
                      visible=False)
    comment=flet.TextField(hint_text="Write  your ideas",
                          prefix_icon=flet.icons.ADD_COMMENT,
                          width=450,
                          visible=False)
    comment_button=flet.ElevatedButton(text="Add",
                                      visible=False,
                                      icon=flet.icons.ADD,
                                      on_click=add_comment)
    notification_title=flet.Text("Notification",
                   size=50,
                   font_family="Lucida Calligraphy",
                   color=flet.colors.PINK,
                   visible=False)
    for i in range(0,5):
        notification.controls.append(flet.TextButton(text=people[i]+" "+events[i],
                                                     icon=flet.icons.NOTIFICATIONS_ACTIVE,
                                                     icon_color=flet.colors.RED))
        page. update()                                           
    page.add (flet.Container(
        margin=flet.margin.only(
            top=page.window_height/4,
            left=page.window_width/3,
            right=page.window_width/2.8),
        content=flet.Column(
            [login, home_page, user_name, password, button, search_label, search, 
             search_button, liste, comment_title, comment_label, comments,
             (flet.Row([who, comment])) , comment_button, notification_title,notification])))                    
flet.app(target=main)


 

