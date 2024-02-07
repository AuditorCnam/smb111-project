document.querySelector("html").classList.add('js');

var fileInput = document.querySelector(".input-file"),
    button = document.querySelector(".input-file-trigger"),
    the_return = document.querySelector(".file-return");


button.addEventListener("keydown", function (event) {
    if (event.keyCode == 13 || event.keyCode == 32) {
        fileInput.focus();
    }
});
button.addEventListener("click", function (event) {
    fileInput.focus();
    return false;
});
fileInput.addEventListener("change", function (event) {
    the_return.innerHTML = this.value;
    let reader = new FileReader();
    reader.onload = function (e) {
        console.log('Contenu de l\'image en base64:', e.target.result);

        // Par exemple, pour afficher l'image dans une balise img
        let imageElement = document.createElement('img');
        imageElement.src = e.target.result;
        document.body.appendChild(imageElement)
        fetch()
    }
    reader.readAsDataURL(this.files[0]);
});  
