function allowDrop(ev)
{
	ev.preventDefault();
}

function drag(ev)
{	
	ev.dataTransfer.setData("task", ev.target.id);
}

function drop(ev)
{
	ev.preventDefault();
	ev.target.innerHTML = ""
	ev.target.className = "";
	var data = ev.dataTransfer.getData("task");
	ev.target.appendChild(document.getElementById(data));
	var taskid = document.getElementById(data).getAttribute("taskid");
	var task_moscow = ev.target.getAttribute("taskmoscow");
	
	$.get('/project/drag_and_drop_task', {'taskid': taskid, 'task_moscow': task_moscow}, function(data){
		//location.reload(); 
	});
}

