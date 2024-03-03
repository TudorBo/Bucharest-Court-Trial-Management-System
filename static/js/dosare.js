function searchAction(form) {
  var dosar = document.getElementById('dosar').value;
  if (dosar == "") {
    form.action = "/dosare";
  }
  else
  {
    form.action = "/dosare_search/number=" + dosar;
  }
}

// Add modal
function showModal(index) {
  // Get the modal
  var modal = document.getElementById("Modal" + index);

  // Display the modal
  modal.style.display = "block";
}

// Get all "show" buttons
var btns = document.querySelectorAll(".btn-secondary");

// Attach the onclick event to each button
btns.forEach(function(btn, index) {
  btn.onclick = function() {
    showModal(index + 1); // Adding 1 because loop.index is 1-based
  };
});

// Get all <span> elements that close the modals
var spans = document.querySelectorAll(".close");

// Attach the onclick event to each span
spans.forEach(function(span, index) {
  span.onclick = function() {
    var modal = document.getElementById("Modal" + (index + 1));
    modal.style.display = "none";
  };
});

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target.classList.contains("modal")) {
    event.target.style.display = "none";
  }
};

