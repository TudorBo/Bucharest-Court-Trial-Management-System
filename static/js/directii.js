function searchAction(form) {
  var directie = document.getElementById('directie').value;
  console.log(directie);
  if (directie == "") {
    form.action = "/directii";
  }
  else
  {
    form.action = "/directie_search/name=" + directie;
  }
}

//* add modal

// Get the modal
var addModal = document.getElementById("addModal");

function showAddModal() {

  // Display the modal
  addModal.style.display = "block";
  console.log("showAddModal");
}

// Get the "Add" button
var addBtn = document.getElementById("addBtn");

// When the user clicks the "Add" button, call the showAddModal function
addBtn.onclick = showAddModal;

// Get the <span> element that closes the "Add" modal
var spanAdd = document.getElementsByClassName("close-add")[0];

// When the user clicks on <span> (x), close the "Add" modal
spanAdd.onclick = function() {
  var addModal = document.getElementById("addModal");
  addModal.style.display = "none";
  console.log("closeAddModal");
}

//* update modal

// Get the modal
var updateModal = document.getElementById("updateModal");
  
function showUpdateModal(id, nume, desc) {
    
    // Get the form inside the modal
    var form = updateModal.querySelector("form");
  
    // Set the value of the hidden input field to the id
    form.querySelector("input[name='id']").value = id;

    //Set the value of the input fields
    var numeInput = form.querySelector("input[name='Nume']");
    var descInput = form.querySelector("input[name='Descriere']");
  
    if (numeInput && descInput) {
      numeInput.value = nume;
      descInput.value = desc;

      numeInput.value = nume;
      descInput.value = desc;

      numeInput.placeholder = "Nume";
      descInput.placeholder = "Descriere";

      // Display the modal
    updateModal.style.display = "block";
    } else {
      console.log("Could not find the input fields in the form");
    }
    
  }
  
// Get the <span> element that closes the "Update" modal
var spanUpdate = document.getElementsByClassName("close-update")[0];

// When the user clicks on <span> (x), close the "Update" modal
spanUpdate.onclick = function() {
  var updateModal = document.getElementById("updateModal");
  updateModal.style.display = "none";

  console.log("closeUpdateModal");
}

//*  delete modal
// Get the modal
var deleteModal = document.getElementById("deleteModal");
function showDeleteModal(id) {

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close-delete")[0];

  // When the user clicks the button, open the modal 
  deleteModal.style.display = "block";

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
      deleteModal.style.display = "none";
      console.log("closeDeleteModal");
  }

  // Update the form action URL with the id of the item to delete
  var form = document.querySelector('#deleteModal form');
  form.action = "/delete_directie/" + id;
  }

// Get the <span> element that closes the "Delete" modal
var spanDelete = document.getElementsByClassName("close-delete")[0];

// When the user clicks on <span> (x), close the "Delete" modal
spanDelete.onclick = function() {
  var modal = document.getElementById("deleteModal");
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modals, close it
window.onclick = function(event) {
  if (event.target == deleteModal) {
    deleteModal.style.display = "none";
    console.log("closeDeleteModal from outside the modal");
  }

  if (event.target == addModal) {
    addModal.style.display = "none";
    console.log("closeAddModal from outside the modal");
  }

  if (event.target == updateModal) {
    updateModal.style.display = "none";
    console.log("closeUpdateModal from outside the modal");
  }

}

