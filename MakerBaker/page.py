
html = """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="../main.css">
    <!-- Prism CSS -->
    <link rel="stylesheet" href="../prism/prism.css">
    <!-- Google Api Fonts, then Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com"> 
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
    <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&family=Dancing+Script:wght@500&family=Indie+Flower&family=Lato:wght@300&family=Silkscreen&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
    <title>String Formatting</title>
    <div class="sticky-top">
        <nav class="navbar navbar-expand bg-light Lato shadow-sm">
            <div id="lt0"> >  </div>
            <button onclick="show('menu-python','lt0')">
                Python 
            
            <div class="menu" id="menu-python" style="display: none;">
                <p>
                    <a href="https://alecscripts.com/Python/functions">Functions</a>
                </p>
                <p>
                    <a href="https://alecscripts.com/Python/stringF">String Formatting</a>
                </p>

            </div>      
            </button>
            <div id="lt"> > </div>    
            <nav class="nav-link">
                
                
                <button onclick="show('menu','lt')">
                    String Formatting 
                
                <div id="menu" class="menu" style="display: none;">
                    <h5>
                        <p>
                            <a style="color: black;" href="#stringF">String Formatting</a>
                        </p>
                    </h5>
                     <p>
                        <a href="#basicSyntax">Basic Syntax</a>
                    </p>
                     <p>
                        <a href="#args">Arguments and Input</a>
                    </p>
                     <p>
                        <a href="#multiple-args">Multiple Positional Arguments</a>
                    </p>
                     <p>
                        <a href="#multiple-args-keyword">Multiple Keyword Arguments</a>
                    </p>
                    <p>
                        <a href="#default-args">Default Arguments</a>
                    </p>
                    <p>
                        <a href="#returningValues">Return Values</a>
                    </p>
                </div>      
                </button>
            </nav>
        </nav>
    </div>
  </head>
<body>




  <!-- Optional JavaScript -->
    <script src="../mainJs.js"></script>

    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        <!-- Prism JavaScript -->
        <script src="../prism/prism.js"></script>
  </body>

  <footer class=" bg-dark ">
    <div class="nav-link">
        <a href="https://alecscripts.com">
            alecscripts.com
          </a>
    </div>
    <div class="nav-link">
        <a  href="https://github.com/searsam1/searsam1.github.io">
            Website Repository
        </a>
    </div>
  </footer>
</html>
"""