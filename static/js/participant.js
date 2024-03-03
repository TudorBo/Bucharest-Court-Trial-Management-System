function searchAction(form) {
    var participant = document.getElementById('participant').value;
    console.log(participant);
    if (participant == "") {
      form.action = "/participanti";
    }
    else
    {
      form.action = "/participant_search/name=" + participant;
    }
  }