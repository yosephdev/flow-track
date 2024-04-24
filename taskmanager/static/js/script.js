document.addEventListener("DOMContentLoaded", function() {
  // sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav, {
    edge: 'left',
    inDuration: 250,
    outDuration: 200,
    draggable: true
  });
});