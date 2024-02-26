function options(id, option) {
  let previousTask;
  option = "/" + option;
  editId = "edit" + id;

  if (option == "/cancel" || option == "/edit") {
    taskDivId = "tsk" + id;
    taskDiv = document.getElementById(taskDivId);

    hiddenTask = document.querySelector(`.task[style="display:none]`);
    openedEditBoxes = document.getElementsByName("edit-div");
    openedEditBox = openedEditBoxes.item(0);

    if (option == "/edit") {
      if (openedEditBox != null) {
        // hiddenTaskDivId = "tsk" + openedEditBox.id;
        hiddenTaskDivId = hiddenTask.id;
        openedEditBox.remove();

        taskDiv.style = "display:flex;";
        // hiddenTaskDiv = document.getElementById(hiddenTaskDivId);
        // hiddenTaskDiv.style = "display:flex";
        console.log(openedEditBoxes, openedEditBox, hiddenTaskDivId, taskDivId);
      }

      taskDiv.style = "display:none";
      editedTask = document.createElement("div");
      editedTask.setAttribute("name", "edit-div");
      editedTask.id = editId;
      editedTask.innerHTML = `<form method="POST" onsubmit="options(${id},'okay')" class = "task">
      <input type="text" name="updated-task" placeholder="      Update your task here ......." required />
     <button type="submit"><i class="fa-regular fa-floppy-disk" ></i></button>
      <button name="cancel" type="reset" onclick="options('${id}','cancel')"><i class="fa-regular fa-rectangle-xmark"></i></button>

        </form>`;
      taskDiv.after(editedTask);

      return;
    }
    if (option == "/cancel") {
      editedTask = document.getElementById(editId);

      taskDiv.style = "display:flex;";
      editedTask.remove();
    }
  }
  if (option == "/okay") {
    // form1 = document.getElementById(id);
    // form2 = document.getElementById(editId);
    input = document.querySelector("[name='updated-task']");
    updatedText = input.value;
    console.log("hello", updatedText);
    // form.submit(form1);
    // form.submit(form2);
  }
}