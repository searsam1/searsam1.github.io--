
# make a new page


d = {
  "doctype" : "html",
  "lang" : "en"
}

html = f"""
<!doctype {d["doctype"]}>
<html lang={d["lang"]}>

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="../main.css">
    <!-- Prism CSS -->
    <link rel="stylesheet" href="../prism/prism.css">
    <!-- Google Api Fonts, then Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&family=Dancing+Script:wght@500&family=Indie+Flower&family=Lato:wght@300&family=Silkscreen&display=swap"
        rel="stylesheet">
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
    <title>html - Elements</title>

    <div class="sticky-top">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark  shadow-sm">
            <a class="navbar-brand" href="#">Alec Scripts</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
    
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mr-auto">
                    
                    <li class="nav-item dropdown">
                      <a class="active nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        HTML
                      </a>
                      <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="#attributes">Attributes</a>
                        <a class="dropdown-item" href="#">Colors</a>
                        <a class="dropdown-item" href="#">Comments</a>
                        <a class="dropdown-item" href="#">Elements</a>
                        <a class="dropdown-item" href="#">Email Links</a>
                        <a class="dropdown-item" href="#">Fonts</a>
                        <a class="dropdown-item" href="#">Format</a>
                        <a class="dropdown-item" href="#">Image Links</a>
                        <a class="dropdown-item" href="#">Images</a>
                        <a class="dropdown-item" href="#">Lists</a>
                        <a class="dropdown-item" href="#">Meta</a>
                        <a class="dropdown-item" href="#">Phrase Tags</a>
                        <a class="dropdown-item" href="#">Tables</a>
                      </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="active nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                          Python
                        </a>
                        <div class="dropdown-menu shadow-sm" aria-labelledby="navbarDropdown">
                          <a class="dropdown-item" href="#attributes">Classes</a>
                          <a class="dropdown-item" href="#">Containers</a>
                          <a class="dropdown-item" href="#">Functions</a>
                          <a class="dropdown-item" href="#">numbers</a>
                          <a class="dropdown-item" href="#">String Formatting</a>
                          <a class="dropdown-item" href="#">Strings</a>
                          <a class="dropdown-item" href="#">Yield</a>
                          
                        </div>
                      </li>
                  </ul>
            </div>
            
        
        </nav>
    </div>
</head>

<body>
    <div class="container-no-animation">

        <h3 class="display-4">
            HTML - Elements
        </h3>

        <p>
            Tags are used to create elements which are all
            the different parts to a website. These elements 
            are written in html and displayed as a website 
            to the web browser.
        </p>
        <pre><code class="language-html">&lt;a href="https://www.google.com"&gt; google &lt;a&gt;</code></pre>
        <p>will be displayed as <a href="https://www.google.com">google</a>.
        The link is the element and it is comprised of 
        start and end anchor tags with the text "google".
        </p>
        <b>Bold</b>
        <pre><code class="language-html">&lt;b&gt;Bold&lt;b&gt;</code></pre>
        <i>Italic</i>
        <pre><code class="language-html">&lt;i&gt;Italic&lt;i&gt;</code></pre>
        <s>Strikethrough</s>
        <pre><code class="language-html">&lt;s&gt;Strikethrough&lt;s&gt;</code></pre>
        <button onclick="clickMe()" class="btn btn-outline-danger">Clickable Button</button>
        <pre><code class="language-html">&lt;button onclick="clickMe()" class="btn btn-outline-danger"&gt;Clickable Button&lt;button&gt;</code></pre>
        
        

    </div>


    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
        crossorigin="anonymous"></script>
    <!-- Prism JavaScript -->
    <script src="../prism/prism.js"></script>
    <!-- My JavaScript -->
    <script src="../mainJs.js"></script>
</body>

<footer class=" bg-dark ">
    <div class="nav-link">
        <a href="https://alecscripts.com">
            alecscripts.com
        </a>
    </div>
    <div class="nav-link">
        <a href="https://github.com/searsam1/searsam1.github.io">
            Website Repository
        </a>
    </div>
</footer>

</html>
"""