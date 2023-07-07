function handleCardClick(cardNumber) {
    alert("Clicked on card " + cardNumber);
  }
  
  function handleLogout() {
    alert("Logged out");
  }
  
  function toggleNav() {
    var sidenav = document.getElementById("mySidenav");
    var navbar = document.getElementsByClassName("navbar")[0];
    
    if (sidenav.style.width === "200px") {
      sidenav.style.width = "0";
      navbar.style.marginLeft = "0";
    } else {
      sidenav.style.width = "200px";
      navbar.style.marginLeft = "200px";
    }
  }
  