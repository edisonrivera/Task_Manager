# **Task Manager** 📑

App created in **Python** using **Rich** and **Typer**.

<div align="center">
  <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a>
</div>

## **Use of application** 👨‍💻

1. **Show help panel**

```bash
python main.py --help
```

![help.PNG](/assets/help.PNG)


2. **Add task**
```bash
python main.py add "[Task]" "[Category]"
```
* When you add a task the field `Task Added At` catch current date automatically.


![add.PNG](/assets/add.PNG)

3. **Update Task**
```bash
python main.py update [index] "[Task]" "[Category]"
```

![update.PNG](/assets/update.PNG)

4. **Complete Task**
```bash
python main.py complete [index]
```

* When you complete a task the field `Task Completed At` catch current date automatically.

![complete.PNG](/assets/complete.PNG)

5. **Delete Task**
```bash
python main.py delete [index]
```

![delete.PNG](/assets/delete.PNG)

6. **Show all Tasks**
```bash
python main.py show
```

![show.PNG](/assets/show.PNG)
