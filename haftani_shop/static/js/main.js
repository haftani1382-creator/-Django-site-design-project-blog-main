document.addEventListener("DOMContentLoaded", function (event) {
  const date = new Date();
  document.querySelector(".year").innerHTML = date.getFullYear();
  const showNavbar = (toggleId, navId, bodyId, headerId, listsId) => {
    const toggle = document.getElementById(toggleId),
      nav = document.getElementById(navId),
      bodypd = document.getElementById(bodyId),
      headerpd = document.getElementById(headerId);
    listings = document.getElementById(listsId);

    // Validate that all variables exist
    if (toggle && nav && bodypd && headerpd) {
      toggle.addEventListener("click", () => {
        // show navbar
        nav.classList.toggle("show");
        // change icon
        toggle.classList.toggle("bx-x");
        // add padding to body
        bodypd.classList.toggle("body-pd");
        // add padding to header
        headerpd.classList.toggle("listings-format");
      });
    }
  };

  showNavbar("header-toggle", "nav-bar", "body-pd", "header", "listings");

  /*===== LINK ACTIVE =====*/
  const linkColor = document.querySelectorAll(".nav_link");

  function colorLink() {
    if (linkColor) {
      linkColor.forEach((l) => l.classList.remove("active1"));
      this.classList.add("active1");
    }
  }
  linkColor.forEach((l) => l.addEventListener("click", colorLink));

  // Your code to run since DOM is loaded and ready
});

setTimeout(function(){

  $('#message').fadeOut('slow');

}, 3000)  
// مسیجی که میاید بعد از 3 ثانیه خودش 
//fadeout
// بشود
