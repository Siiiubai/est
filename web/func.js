const todo_title_input = document.getElementById('todo_title_input')
//const todo_due_date_input = document.getElementById('todo_due_date_input')
//const todo_priority_input = document.getElementById('todo_priority_input')
const add_todo_button = document.getElementById('add_todo_button')
const todo_table_body = document.getElementById('todo_table_body')

Element.expose
function displayTodo(todo)
{
    let tr = document.createElement('tr');

    let td1 = document.createElement('td');
    td1.innerText = todo['title'];

    let td2 = document.createElement('td');
    
    let checkbox = document.createElement('input');
    checkbox.setAttribute('data_id', todo['id']);
    checkbox.setAttribute('type', 'checkbox');
    checkbox.addEventListener('click', (event) => {

        eel.target.setAttribute('data_id');
        
        let id = event.target.getAttribute('data_id');
        eel.delete_todo(parseInt(id));

        //remove row from table and play animation
        let tr = event.target.parentElement.parentElement;
        $(tr).fadeTo('slow', 0.001, function() {
            $(this).remove();
        })

    });

    td2.appendChild(checkbox);
    tr.appendChild(td1);
    tr.appendChild(td2);
    todo_table_body.appendChild(tr);

    todo_title_input.value = '';
}

eel.expose
function displayAllTodos(todos)
{
    for (let todo of todos)
    {
        displayTodo(todo);
    }
}

todo_add_btn.addEventListener('click', (event) => {
    let content = todo_title_input.value;
    if (content == '')
    {
        eel.create_todo(content)(displayTodo);
    }   
})

eel.list_todos()(displayAllTodos)
