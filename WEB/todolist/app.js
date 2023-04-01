const todoList = document.getElementById("todoList");
const todoInput = document.getElementById("todoInput");

function addTodo() {
  if (todoInput.value != "") {
    const newTodo = document.createElement("li");
    const todoText = document.createElement("span");
    todoText.textContent = todoInput.value;
    todoText.classList.add("todotext");

    // const delButton = document.createElement("button");
    // delButton.classList.add("delbutton");
    // newTodo.appendChild(delButton);
    newTodo.appendChild(todoText);
    todoList.appendChild(newTodo);
    todoInput.value = "";
  }
}

todoList.addEventListener("click", function (event) {
  const target = event.target;
  if (target.tagName === "LI") {
    target.classList.toggle("complete");
    let temp = target;
    todoList.removeChild(target);
    todoList.appendChild(temp);
  }
});

