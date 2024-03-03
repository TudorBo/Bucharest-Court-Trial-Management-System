//add modal
function showAddModal() {
    // Get the modal
    var modal = document.getElementById("addModal");
  
    // Display the modal
    modal.style.display = "block";
  }
  
  // Get the "Add" button
  var addBtn = document.getElementById("addBtn");
  
  // When the user clicks the "Add" button, call the showAddModal function
  addBtn.onclick = showAddModal;
  
  // Get the <span> element that closes the "Add" modal
  var spanAdd = document.getElementsByClassName("close-add")[0];
  
  // When the user clicks on <span> (x), close the "Add" modal
  spanAdd.onclick = function() {
    var modal = document.getElementById("addModal");
    modal.style.display = "none";
  }
  
  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    var modal = document.getElementById("addModal");
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }

  //update modal
  function showUpdateModal(id) {
      // Get the modal
      var modal = document.getElementById("updateModal");
    
      // Get the form inside the modal
      var form = modal.querySelector("form");
    
      // Set the value of the hidden input field to the id
      form.querySelector("input[name='id']").value = id;
    
      // Display the modal
      modal.style.display = "block";
    }
    
    // Get the <span> element that closes the "Update" modal
    var spanUpdate = document.getElementsByClassName("close-update")[0];
    
    // When the user clicks on <span> (x), close the "Update" modal
    spanUpdate.onclick = function() {
      var modal = document.getElementById("updateModal");
      modal.style.display = "none";
    }
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        var addModal = document.getElementById("addModal");
        if (event.target == addModal) {
          addModal.style.display = "none";
        }
      
        var updateModal = document.getElementById("updateModal");
        if (event.target == updateModal) {
          updateModal.style.display = "none";
        }
    }

    // delete modal
    function showDeleteModal(id) {
        // Get the modal
    var modal = document.getElementById("deleteModal");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close-delete")[0];

    // When the user clicks the button, open the modal 
    modal.style.display = "block";

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Update the form action URL with the id of the item to delete
    var form = document.querySelector('#deleteModal form');
    form.action = "/delete_judecator/" + id;
      }

    // When the user clicks on <span> (x), close the "Delete" modal
    spanDelete.onclick = function() {
      var modal = document.getElementById("deleteModal");
      modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        
        var addModal = document.getElementById("addModal");
        if (event.target == addModal) {
          addModal.style.display = "none";
        }

        var updateModal = document.getElementById("updateModal");
        if (event.target == updateModal) {
          updateModal.style.display = "none";
        }

        var deleteModal = document.getElementById("deleteModal");
        if (event.target == deleteModal) {
          deleteModal.style.display = "none";
        }
      
    }
