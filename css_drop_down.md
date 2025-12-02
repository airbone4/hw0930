```html
  <script>
    function toggle() {
      mymenu.classList.toggle('hidden')
      mymenu.classList.toggle('flex')
    }
  </script>
  <style>
    .menu {
      position: relative
    }

    .hidden {
      display: none
    }
    .flex{
      display:flex;
    }
    .menu-content {
      position:absolute;
      z-index: 1;
    }
  </style>
 
 
  <nav display:flex>
    <button> xx</button>

    <div class="menu">
      <button onclick="toggle()">yy</button>
      <div  id="mymenu" class="menu-content hidden ">
        <button>item1</button>
        <button>item2</button>
      </div>
    </div>
  </nav>

  <div>
```
[ref]("https://www.w3schools.com/howto/howto_css_dropdown.asp")
