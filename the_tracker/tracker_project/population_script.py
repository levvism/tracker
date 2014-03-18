import os

def populate():
    user1 = add_user(username = "anto",
                     email = "anto@abv.bg",
                     password = "1101",
                     first_name = "Anton",
                     last_name = "Belev")
    user2 = add_user(username = "admin",
                     email = "admin@gmail.com",
                     password = "1234",
                     first_name = "Admin",
                     last_name = "Admin")
    user3 = add_user(username = "goshko",
                     email = "goshko@abv.bg",
                     password = "1234",
                     first_name = "Goshko",
                     last_name = "Toshkov")
    
    project1 = add_project(title = "DIM3 Assignment",
                           collaborators = [user1, user2, user3])
    project2 = add_project(title = "PSD3 Sprint",
                           collaborators = [user1, user3])
    project3 = add_project(title = "DB3",
                           collaborators = [user2, user3])    
    
    task1 = add_task(title = "Implement Drag and Drop",
                     description = "description1",
                     priority = 4,
                     project = project1)
    
    task2 = add_task(title = "task2",
                     description = "description2",
                     priority = 1,
                     project = project1)
    task3 = add_task(title = "task3",
                     description = "description3",
                     priority = 5,
                     project = project3)
    task4 = add_task(title = "task4",
                     description = "description4",
                     priority = 4,
                     project = project3)

    # Print out what we have added to the user.
    for u in User.objects.all():
        print u
    for p in Project.objects.all():
        s = str(p) + " -> "
        for u in p.collaborators.all():
            s += str(u) + " "
        print s
    for t in Task.objects.all():
        s = str(t) + " -> " + str(t.project)
        print s
    

def add_user(username, email, password, first_name, last_name):
    u = User.objects.get_or_create(username = username, email = email, password = password, first_name = first_name, last_name = last_name)[0]
    return u

def add_project(title, collaborators = []):
    p = Project.objects.get_or_create(title = title)[0]
    for user in collaborators:
        p.collaborators.add(user)
    return p

def add_task(title, description, project, priority = 0):
    t = Task.objects.get_or_create(title = title, description = description, priority = priority, project = project)[0]
    return t
    

# Start execution here!
if __name__ == '__main__':
    print "Starting Requirements Tracker population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_or_not_todo.settings')
    from requirements_tracker.models import Project, Task
    from django.contrib.auth.models import User
    populate()