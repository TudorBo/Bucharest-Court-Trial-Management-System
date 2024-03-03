function searchAction(form) {
    var tip = document.getElementById('tip').value;
    console.log(tip);
    if (tip == "") {
      form.action = "/tipuri_participanti";
    }
    else
    {
      form.action = "/tip_participanti_search/name=" + tip;
    }
  }