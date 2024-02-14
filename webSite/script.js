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
fileInput.addEventListener("change", async function (event) {
    the_return.innerHTML = this.value;
    let reader = new FileReader();
    let file = event.target.files[0];
    reader.onload = function (e) {
        console.log('Contenu de l\'image en base64:', e.target);
        // Par exemple, pour afficher l'image dans une balise img
        let imageElement = document.createElement('img');
        imageElement.src = e.target.result;
        imageElement.style.marginLeft = '25%';
        imageElement.style.marginTop = '5%';
        document.body.appendChild(imageElement)
    }
    reader.readAsDataURL(this.files[0]);

   

    // URL du Blob Storage avec SAS Token
    
        const fileName = file.name;
        const azureContainerName = 'blob-container';
        const sasToken = '?sp=raw&st=2024-02-14T11:57:39Z&se=2024-03-22T19:57:39Z&spr=https&sv=2022-11-02&sr=c&sig=%2F9v4J09q3W5sN8k2Ggy9jhgihgVPorWZ%2B3mOBS0ovP4%3D'; // Assurez-vous que le SAS est URL encoded
        const azureStorageAccountName = 'myresourcesgroupb3b7';
        const url = `https://${azureStorageAccountName}.blob.core.windows.net/${azureContainerName}/${fileName}${sasToken}`;
    
        try {
            const response = await fetch(url, {
                method: 'PUT',
                headers: {
                    'x-ms-blob-type': 'BlockBlob',
                    'Content-Type': file.type
                },
                body: file
            });
    
            if (response.status === 201) {
                console.log("File uploaded successfully");
            } else {
                console.error("Upload failed", response.statusText);
            }
        } catch (error) {
            console.error("Error uploading file", error);
        }
});