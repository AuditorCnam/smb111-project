# SMB111-project
Final project SMB111
Berthier Théo


## Create functionapp

Créer une fonction app à partir d'un resource group ainsi qu'un "storage account", l'exemple suivant est une fonctionapp qui sera fait pour fonctionner avec nodejs et du javascrpt

```bash
az functionapp create --name simple-interest --storage-account myresourcesgroupb3b7 --resource-group myResourcesGroup --consumption-plan-location eastus --runtime node
```
## Create function

Ensuite l'initialisation d'une fonction ce fait comme cela

```bash
func init
1.
2.
3. node
4. python
5. powershell

3

creation ....
```

Les fichiers concernant la fonction son initialisé il suffit de créer une nouvelle fonction 

```bash
func new <func_name>

10. http trigger
```

Un fichier est créer il suffit de modifier le fichier index.js pour ajouter sa fonction

ensuite il est possible de tester en local la fonction 
```bash
func start &> output.txt &
```
après une url est donnée dans output.txt pour requéter l'api 

```bash
curl "http://localhost:7071/api/simple-interest?principal=5000&rate=0.14&term=5"
```
Une fois vérifier on peut publier la fonction 

```bash
func azure functionapp publish simple-interest
Getting site publishing info...
Creating archive for current directory...
Uploading 1.38 KB [###############################################################################]
Upload completed successfully.
Deployment completed successfully.
Syncing triggers...
Functions in simple-interest:
    simple-interest - [httpTrigger]
        Invoke url: https://<uri>.azurewebsites.net/api/simple-interest
```
Retourver le token liée à la fonction 

```bash
az functionapp keys list --name simple-interest --resource-group myResourcesGroup   
```

Ensuite le test 

```bash
curl "https://simple-interest.azurewebsites.net/api/simple-interest?code=<token>&principal=5000&rate=0.14&term=5"
3500.0000000000005
```


## IA vision

après avoir créer les ressources nécessaire a la detection par IA, il est possible d'envoyer des requête avec le token de sa ressource IA service 

```bash
curl -H "Ocp-Apim-Subscription-Key: <token>" -H "Content-Type: application/json" "https://ia-resources-services.cognitiveservices.azure.com/computervision/imageanalysis:analyze?features=caption,read&model-version=latest&language=en&api-version=2023-10-01" -d "{'url':'https://referenseo.com/wp-content/uploads/2019/03/image-attractive-960x540.jpg'}"
```

Reponse de l'API 

```json
{
    "modelVersion": "2023-10-01",
    "captionResult": {
        "text": "an elephant flying in the sky",
        "confidence": 0.700043797492981
    },
    "metadata": {
        "width": 960,
        "height": 540
    },
    "readResult": {
        "blocks": []
    }
}
```

## Requête pour upload dans la base blob 

Groupe de ressource :
1. créer un groupe de ressource 
2. générer un jeton accès partagé avec des droits sur les conatiners
3. créer un container blob
4. gérer les droits CORS de la ressources 

Upload fichier : 
- depuis site web javascript : 
  
```js
        let file = document.getElementById('fileInput');

        const fileName = file.name ; // nom du fichier récupérer via un inputfile HTML
        const azureContainerName = <Nom-du-container>;
        const sasToken = <Token-du-groupe-de-ressource>
        const azureStorageAccountName = <Nom-compte-de-ressource>;
        
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
```

- requête curl : 

```bash

curl -H "x-ms-blob-type: BlockBlob" -H "Content-Type: image/png" https://${azureStorageAccountName}.blob.core.windows.net/${azureContainerName}/${fileName}${sasToken} -d '{"data": image.png}'

```

Objectif :
- créer un site web
- envoyer des images sur un blob
- délanchement d'un appel vers https://ia-resources-services.cognitiveservices.azure.com/computervision/imageanalysis
- obtenir la description et l'envoyer dans une base cosmodb
- afficher la description de l'image avec l'image sur le site
  
