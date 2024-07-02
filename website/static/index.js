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

function updateGreetings(username) {
  const greetingElement = document.getElementById("greeting");
  if (greetingElement) {
    const hour = new Date().getHours();
    let greeting;
    if (hour < 12) {
      greeting = "Good Morning";
    } else if (hour < 18) {
      greeting = "Good Afternoon";
    } else {
      greeting = "Good Evening";
    }
    greetingElement.textContent = `${greeting}, ${username}`;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const username = document.getElementById("greeting").dataset.username;
  updateGreetings(username);
});
