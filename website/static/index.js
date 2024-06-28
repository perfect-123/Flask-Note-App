function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deleteTodo(todoId) {
  fetch("/delete-todo", {
    method: "POST",
    body: JSON.stringify({ todoId: todoId }),
  }).then((_res) => {
    window.location.href = "/todo";
  });
}
